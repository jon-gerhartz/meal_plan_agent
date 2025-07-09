import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "get_shopping_list",
        "description": "Retrieve all unpurchased items from a grocery list",
        "parameters": {
            "type": "object",
            "properties": {
                "list_id": {"type": "integer", "description": "ID of the grocery list"}
            },
            "required": ["list_id"]
        }
    }

def execute(args, token):
    list_id = args.get("list_id")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BACKEND_API_URL}/grocery-lists/{list_id}/shopping", headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return f"Error: {response.text}"