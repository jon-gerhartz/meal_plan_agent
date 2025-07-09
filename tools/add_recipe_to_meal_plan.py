import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "add_recipe_to_meal_plan",
        "description": "Associate an existing recipe with a meal plan",
        "parameters": {
            "type": "object",
            "properties": {
                "meal_plan_id": {"type": "integer"},
                "recipe_id": {"type": "integer"},
                "day": {"type": "string", "description": "Date for the meal (YYYY-MM-DD)"},
                "meal_type": {"type": "string", "description": "Type of meal, e.g., breakfast, lunch, dinner"}
            },
            "required": ["meal_plan_id", "recipe_id", "day", "meal_type"]
        }
    }

def execute(args, token):
    meal_plan_id = args.get("meal_plan_id")
    payload = {
        "recipe_id": args.get("recipe_id"),
        "day": args.get("day"),
        "meal_type": args.get("meal_type")
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/meal-plans/{meal_plan_id}/recipes", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"