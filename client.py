# This is a sample Python client for the OpenAI API. 
# It demonstrates how to create a chat completion using the GPT-3.5-turbo model. 
# You need to replace the dummy API key with your own key to authenticate and use the API.

from openai import OpenAI
client = OpenAI(
    # Set the API key for authentication (its just a dummy key, you need to replace it with your own key)
    api_key="abcd1234"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role":"system", "content":"you are virtual assistant named Jarvis skilled in general tasks like Alexa and Google cloud "},
        {"role": "user", "content" :"what is coding"} 
           ]
)
print(completion.choices[0].message)