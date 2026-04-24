from jsonpath_ng import parse
import allure
class AssertEngine:

    def assert_response(self,response,validate_rules,mode="api"):
          
        print(f"\n开始执行{mode.upper()}断言，共有{len(validate_rules)}条规则")
        for i,rules in enumerate(validate_rules,1):
              op = list(rules.keys())[0]
              args = list(rules.values())[0]

              if len(args) != 2:
                 raise Exception(f"断言规则 {rules} 格式错误，必须包含 [字段, 预期值]")
              field,expect = args

              if mode == "api":
                actual = self.get_field(response,field)

              else:
                actual = response.get(field)
              
              with allure.step(f"{mode.upper()}断言: {field} {op} {expect}"):
                   allure.attach(f"实际值: {actual}\n预期值: {expect}", 
                             name=f"断言_{i}_对比详情", 
                             attachment_type=allure.attachment_type.TEXT)
              func = getattr(self,op)
              func(actual,expect)



    def get_field(self,response,field):        
        if field == "status_code":
            return response.status_code
        
        if field.startswith("body"):
            response = response.json()
            path_list = field.split(".")[1:]
            path ="$."+ ".".join(path_list)
            jsonpath_ng = parse(path)
            match = jsonpath_ng.find(response)
            if not match:
                raise Exception(f"没有找到该路径{path}")
            actual = match[0].value
            return actual


    def eq(self,actual,expect):
            msg = f"断言失败! 实际值:{actual}({type(actual)}) != 预期值:{expect}({type(expect)})"
            assert str(actual) == str(expect), msg
        
    def contains(self,actual,expected):
            assert actual in expected , f"断言失败{actual} != {expected}"

    def gt(self,actual,expected):
            assert actual > expected , f"断言失败{actual} != {expected}"

    def lt(self,actual,expected):
             assert actual < expected , f"断言失败{actual} != {expected}"    




    # def assert_response(self,response,validate):
    #     print(f"\n本次用例共有{len(validate)}条断言")
    #     i = 1
    #     for rules in validate:
            
    #         op = list(rules.keys())[0]
    #         args = list(rules.values())[0]
    #         print(f"正在执行第{i}条断言:类型{op}，规则{args}")
    #         if len(args) != 2:
    #             raise Exception(f"{args}断言不是两个，有错误")
    #         field,expect = args
    #         actual = self.get_field(response,field)

    #         allure.attach(str(), name=f"断言_{i}_详情", attachment_type=allure.attachment_type.TEXT)

    #         func = getattr(self,op)
    #         func(actual,expect)
    #         i = i+1
          


