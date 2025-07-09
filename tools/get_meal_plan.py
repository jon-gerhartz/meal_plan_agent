import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_meal_plan",
        "description": "Fetch a meal plan and its weekly schedule by meal plan ID",
        "parameters": {
            "type": "object",
            "properties": {
                "meal_plan_id": {"type": "integer"}
            },
            "required": ["meal_plan_id"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    meal_plan_id = args.get("meal_plan_id")
    response = requests.get(f"{BACKEND_API_URL}/meal-plans/{meal_plan_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"