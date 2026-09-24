import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not there in .env file")

llm = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

response = llm.chat.completions.create(
    model="openai/gpt-5.4-mini", 
    temperature=0,
    max_tokens=150,
    messages = [
        {
            "role": "system",
            "content": "Consider you're an IT Trainer"
        },
        {
            "role": "user",
            "content": "Explain about Data Engineer Concepts make sure it's full completed within the max token set"
        }
    ],
    )

print("Response Usage : ",response.choices[0].message.content)
print("Response Usage : ",response.usage)