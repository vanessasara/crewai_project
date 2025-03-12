#!/usr/bin/env python
from crewai.flow import Flow, listen, start
from litellm import completion
import os 

os.environ['GEMINI_API_KEY'] = 'AIzaSyA_ZizxbIP8CRvmgKJZAzFTzpCrYO1HB1U'

class PoemFlow(Flow):

    @start()
    def generating_random_city(self):
        response = completion(
        model='gemini/gemini-1.5-flash',
        messages=[{"role":"user","content":input('Write any city name:')}]
    )
        city = response['choices'][0]['message']['content']
        # print(city)
        return city
    
    
    @listen(generating_random_city)
    def generate_funfact(self,city_name):
        response = completion(
        model='gemini/gemini-2.0-flash-exp',
        messages=[{"role":"user","content":f"write some fun fact about {city_name} city "}]
    )
        fun_fact = response['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact'] = fun_fact
    
    @listen(generate_funfact)
    def save_fun_fact(self):
        with open("fun_fact.md","w") as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']

def kickoff():
    obj = PoemFlow()
    result = obj.kickoff()
    print(result)
    
