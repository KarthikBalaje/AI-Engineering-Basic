# 53_security.py
import os, logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Secret management
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("Missing API key")

# Authentication
def authenticate(token):
    return token == os.getenv("USER_TOKEN")

# Authorization / least privilege
permissions = {
    "user": ["read"],
    "admin": ["read", "write", "delete"]
}

def authorize(role, action):
    return action in permissions.get(role, [])

# Input validation
def validate_customer(customer_id):
    return isinstance(customer_id, int) and customer_id > 0

token = os.getenv("USER_TOKEN")
role = "admin"
action = "write"

if authenticate(token) and authorize(role, action):
    if validate_customer(101):
        logging.info("AUTHORIZED user=101 action=read")
        print("Access granted")
else:
    print("Access denied")