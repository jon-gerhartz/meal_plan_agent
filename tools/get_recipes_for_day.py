import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_recipes_for_day",
        "description": "Retrieve all recipes scheduled for a given day in a meal plan",
        "parameters": {
            "type": "object",
            "properties": {
                "meal_plan_id": {"type": "integer"},
                "date": {"type": "string", "description": "Date (YYYY-MM-DD) for which to fetch"}
            },
            "required": ["meal_plan_id", "date"]
        }
    }

def execute(args, token):
    meal_plan_id = args.get("meal_plan_id")
    date = args.get("date")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BACKEND_API_URL}/meal-plans/{meal_plan_id}/day/{date}", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"