import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_user",
        "description": "Create a new user with a unique email",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "User's email (unique)"}
            },
            "required": ["email"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/users", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"