import os
from crewai.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv



load_dotenv()  
gemini_api_key = os.getenv("GEMINI_API_KEY")


class SimpleFlow(Flow):
    
     @start()
     def func1(self):
        response = completion(
        model='gemini/gemini-1.5-flash',
        messages=[{"role":"user","content":'share the most trending topic title of ai world '}]
    )
        final_result = response['choices'][0]['message']['content']
        return final_result
    
   
def kickoff():
    obj = SimpleFlow()
    result = obj.kickoff()
    print(result)
    
