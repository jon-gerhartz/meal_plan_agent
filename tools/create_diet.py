import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_diet",
        "description": "Create a new diet for a user",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "calories_per_day": {"type": "integer"},
                "protein_ratio": {"type": "number"},
                "carb_ratio": {"type": "number"},
                "fat_ratio": {"type": "number"},
                "restrictions": {"type": "array", "items": {"type": "string"}},
                "inclusions": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["name"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/diets", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"