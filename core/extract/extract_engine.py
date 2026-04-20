from jsonpath_ng import parse
from core.variable.variable_poll import VariablePoll


class ExtractEngine:

    def extract_engine(self,response,extract_rules):
        for key,path in extract_rules.items():
            value = self.extract_byjsonpath(response,path)
            VariablePoll.set_variable(key,value)            
            print(f"提取到的key:{key},value:{value}")



    def extract_byjsonpath(self,response,path):
        data = response.json()
        if path.startswith("body"):
            path_list = path.split(".")[1:]
            path = "$."+".".join(path_list)
            jsonpath_expr = parse(path)
            match = jsonpath_expr.find(data)
            if match:
                return match[0].value
            else:
                raise(f"❌ 提取失败：在响应体中找不到路径 {path}")