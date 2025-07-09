import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_user",
        "description": "Fetch a user by their ID",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer", "description": "ID of the user"}
            },
            "required": ["user_id"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    user_id = args.get("user_id")
    response = requests.get(f"{BACKEND_API_URL}/users/{user_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"