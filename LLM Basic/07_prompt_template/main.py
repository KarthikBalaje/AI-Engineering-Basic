import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not there in .env file")

llm = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

topic = "Agentic AI vs Gen AI"

prompt = f"""
Explain {topic} in simple terms.
Give one real-world example.
"""

response = llm.chat.completions.create(
    model="openai/gpt-5.4-mini", 
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ],
    )

print("Response Usage : ",response.choices[0].message.content)
# print("Response Usage : ",response.usage)