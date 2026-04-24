from core.engine.sync_engine import SyncEngine
from core.loader.loader import Loader
from core.assertion.assert_engine import AssertEngine
from core.extract.extract_engine import ExtractEngine
from core.render.render_engine import RenderEngine
import allure


class CaseRunner:
    def __init__(self,engine,case_map,db=None):
        self.engine = engine
        self.case_map = case_map
        self.assert_engine = AssertEngine()
        self.extract_response = ExtractEngine()
        self.render_engine = RenderEngine()
        self.db = db


    def case_runner(self,runnable_case):

        response = None #为什么加none来着
        runnable_case = self.render_engine.render(runnable_case)
        name = runnable_case.get("name","未命名用例")

        if "scenario" in runnable_case:
            with allure.step(f"执行场景用例：{name}"):
             scenario = runnable_case["scenario"]
             if "steps" in scenario:
                for step_name in scenario["steps"]:
                    step = self.case_map[step_name]
                    self.case_runner(step)
             else:
                raise Exception(f"场景{scenario.get('name')}中的{step}不存在")
        
        

        if "request" in runnable_case:
            with allure.step(f"发送请求：{name}"):
             request_data = runnable_case["request"]
             method = request_data.get("method")
             url = request_data.get("url")
             request_json = request_data.get("json")
             params = request_data.get("params")
             headers = request_data.get("headers")
             response = self.engine.send(
                 method,
                 url,
                 json = request_json,
                 params = params,
                 headers = headers
            )
            
             
             validate_rules = runnable_case.get("validate")
             if validate_rules:
                self.assert_engine.assert_response(response,validate_rules)


             extract_rules = runnable_case.get("extract")
             if extract_rules:
                self.extract_response.extract_engine(response,extract_rules)            
             allure.attach(str(response.request.url), "请求地址", allure.attachment_type.TEXT)
             allure.attach(str(request_data),"请求数据",allure.attachment_type.JSON)
             allure.attach(str(response.text), "响应正文", allure.attachment_type.JSON)

        db_validate = runnable_case.get("db_validate") 
        if db_validate and self.db:
             with allure.step(f"数据库校验：{name}"):
                sql = db_validate.get("sql")
                db_data = self.db.query_one(sql)
                allure.attach(str(sql), "执行SQL", allure.attachment_type.TEXT)
                allure.attach(str(db_data), "查询结果", allure.attachment_type.JSON)
                if db_validate.get("expect") and db_data:
                    self.assert_engine.assert_response(db_data, db_validate["expect"], mode="db")



        return response



            

            

        
        
       
       
       
       
     
         

            

      

