import os

import openai
import openai
from Configurations import Configurations

class gptquery(Configurations):

    def __init__(self):
        super().__init__()
        openai.api_key=self.api_key
        self.engine = self.enginekey


    def openAIQuery(self, query):

        response = openai.Completion.create(
        engine=self.engine,
        prompt=query,
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Opps sorry, you beat the AI this time'
        else:
            answer = 'Opps sorry, you beat the AI this time'

        return answer
