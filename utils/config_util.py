import yaml

class ConfigUtil:
    def __init__(self):
        with open("./config/config.yaml","r",encoding="utf-8") as f:
            self.data = yaml.safe_load(f)
            self.env = self.data["env"]

    def get(self,key):
        return self.data[self.env][key]

config = ConfigUtil()