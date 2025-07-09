import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_meal_plan",
        "description": "Create a new meal plan for a diet",
        "parameters": {
            "type": "object",
            "properties": {
                "diet_id": {"type": "integer"},
                "name": {"type": "string"},
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)"},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)"}
            },
            "required": ["diet_id", "name", "start_date", "end_date"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/meal-plans", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"