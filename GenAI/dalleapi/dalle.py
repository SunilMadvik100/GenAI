import openai
import os
from Configurations import Configurations

class dallEapi(Configurations):

    def __init__(self):
        super().__init__()
        openai.api_key=self.api_key
        self.engine = self.enginekey


    def dallEquery(self, query):
        response = openai.Image.create(
        prompt=query,
        n=1,
        size="256x256",)
        if 'data' in response:
            if len(response['data']) > 0:
                answer = response['data'][0]['url']
            else:
                answer = 'Opps sorry, you beat the AI this time'
        else:
            answer = 'Opps sorry, you beat the AI this time'

        return answer
