import openai
from helper import*
from train import *
from openai import OpenAI
from load_dotenv import load_dotenv

load_dotenv('configs.env')
file_path = 'median_zillow.csv'
rmse = train_and_evaluate(file_path)
print(f'RMSE: {rmse}')


client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
     "content": f"what is the meaning of this rmse: {rmse}"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)
rmse_response=(response.choices[0].message.content)


with open('RMSE Summary.txt','w')as file:
    file.write(rmse_response)
    