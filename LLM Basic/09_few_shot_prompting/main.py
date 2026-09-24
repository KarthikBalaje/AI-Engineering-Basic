import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not there in .env file")

llm = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

zero_shot_prompt = """
        Classify the following review as Positive or Negative.

        Review:
        "The camera quality is poor"
        """


few_shot_prompt = """
        Classify the following review as Positive or Negative.

        Review:
        "The camera quality is poor -> Negative"
        "The camera quality is excellent -> Positive"
        "The camera quality is terrible -> ?"
        """

response = llm.chat.completions.create(
    model="openai/gpt-5.4-mini", 
    messages = [
        {
        "role": "user",
        "content": few_shot_prompt
            }
    ],
    )

print("Response Usage : ",response.choices[0].message.content)
# print("Response Usage : ",response.usage)