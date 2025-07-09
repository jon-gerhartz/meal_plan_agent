import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_active_meal_plans",
        "description": "Fetch all active meal plans for the user",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BACKEND_API_URL}/meal-plans/active", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"