import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not there in .env file")

llm = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

response = llm.chat.completions.create(
    model="openai/gpt-5-mini", 
    messages = [
        {
            "role": "system",
            "content": "You're a teacher, explain in bullets"
        },
        {
            "role": "user",
            "content": "what is agentic ai ?"
        }
    ],
    )

print(response.choices[0].message.content)