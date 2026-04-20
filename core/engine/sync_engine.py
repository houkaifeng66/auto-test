from core.engine.base_engine import BaseEngine
import requests
from utils.config_util import config


class SyncEngine(BaseEngine):
    def __init__(self):
        self.session = requests.Session()
        self.base_url = config.get("base_url")
        self.time_out = config.get("time_out")


    def send(self, method, url, **kwargs):

        full_url  = self.base_url + url
        
        response = self.session.request(
            method,
            url = full_url,
            timeout = self.time_out,
            **kwargs
        
        )
        print(f"{response.json()}")
        return response