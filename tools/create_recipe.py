import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_recipe",
        "description": "Create a new recipe",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "ingredients": {"type": "array", "items": {"type": "object"}},
                "instructions": {"type": "string"},
                "prep_time": {"type": "integer"},
                "cook_time": {"type": "integer"},
                "servings": {"type": "integer"},
                "calories_per_serving": {"type": "integer"},
                "protein": {"type": "number"},
                "carbs": {"type": "number"},
                "fat": {"type": "number"}
            },
            "required": ["name"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/recipes", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"