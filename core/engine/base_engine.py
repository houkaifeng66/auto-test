from abc import ABC,abstractmethod

@abstractmethod
class BaseEngine(ABC):
    def send(self,method,url,**kwargs):
        pass