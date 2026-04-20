import re
from core.variable.variable_poll import VariablePoll
class RenderEngine():
    pattern = r"\$\{(.*?)\}"

    def render(self,runnable_case):
        if isinstance(runnable_case,list):
            return[self.render(i) for i in runnable_case]
        
        elif isinstance(runnable_case,dict):
            return{k:self.render(v) for k,v in runnable_case.items()}
        
        elif isinstance(runnable_case,str):
            return self.render_str(runnable_case)
        else:
            return runnable_case

    def render_str(self,text):
        def replace(match):
            key = match.group(1)
            value = VariablePoll.get_variable(key)
            if value is None:
                raise Exception(f"渲染变量未找到值{key}")
            return str(value)
    
        return re.sub(self.pattern,replace,text)