import json

class Configurations(object):

    json_path = "Configurations.json"


    def __init__(self):
        self.configs = Configurations.LoadJson()
        self.InferenceMode()
        self.getSourcePath()
        self.Load_OpenAI()
        return None


    @classmethod
    def LoadJson(cls):
        with open(Configurations.json_path, 'r') as fh:
            configs = json.load(fh)
        return configs

    def InferenceMode(self):
        self.inference_mode = self.configs["inference_mode"]
        return None
       
    def getSourcePath(self):
        self.sourcePath = self.configs["sourcePath"]
        return None

    def Load_OpenAI(self):
        self.api_key = self.configs["OpenAI"]["Chatgpt"]["api_key"]
        self.enginekey = self.configs["OpenAI"]["Chatgpt"]["engine"]
        return None
    