import requests

response = requests.get(
    "https://openrouter.ai/api/v1/models"
)

models = response.json()["data"]

openai_models = [
    model for model in models
    if model["id"].startswith("openai/")
]

for model in openai_models:
    print(model["id"])