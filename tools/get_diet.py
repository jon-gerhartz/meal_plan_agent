import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_diet",
        "description": "Fetch a diet and its associated meal plans by diet ID",
        "parameters": {
            "type": "object",
            "properties": {
                "diet_id": {"type": "integer", "description": "ID of the diet to fetch"}
            },
            "required": ["diet_id"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    diet_id = args.get("diet_id")
    response = requests.get(f"{BACKEND_API_URL}/diets/{diet_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"