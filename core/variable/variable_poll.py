import threading

class VariablePoll:
    _local = threading.local()

    @classmethod
    def set_variable(cls,key,value):
        if not hasattr(cls._local,"var"):
            cls._local.var = {}
        cls._local.var[key] = value


    @classmethod
    def get_variable(cls,key):
        variables = getattr(cls._local,"var",{})

        return variables.get(key)