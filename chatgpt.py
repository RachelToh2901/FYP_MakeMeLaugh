import openai
import re
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

def chatgpt(user_input):
    '''
    This is a function to connect to openai gpt model through API.
    It accepts a user input, passes to gpt model using API, then returns GPT model response. 
    '''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a joke generator"},
                {"role": "system", "content": "You only provide direct answer without extra desciption phrases to the answer"},
                {"role": "user", "content": user_input},
            ]
    )
    results = response.choices[0].message.content
    results = re.split(r'\d+\.\s*', results)[1:]
    results = [string.replace("\n", "").replace("\ ", "") for string in results]
    return results

if __name__ == "__main__":
    import time 
    start = time.time()
    prompt = "give me 5 joke about school for a 21 years old girl who is chinese and stays in Malaysia"
    output = chatgpt(prompt)
    end = time.time()
    print(output)
    print(end - start)
    print(len(output))