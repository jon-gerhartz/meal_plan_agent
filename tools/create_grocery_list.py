import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_grocery_list",
        "description": "Create a new grocery list for a meal plan",
        "parameters": {
            "type": "object",
            "properties": {
                "meal_plan_id": {"type": "integer", "description": "ID of the associated meal plan"}
            },
            "required": ["meal_plan_id"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/grocery-lists", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"