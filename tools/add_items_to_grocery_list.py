import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "add_items_to_grocery_list",
        "description": "Add multiple items to a grocery list",
        "parameters": {
            "type": "object",
            "properties": {
                "list_id": {"type": "integer", "description": "ID of the grocery list"},
                "items": {"type": "array", "items": {"type": "object"}}
            },
            "required": ["list_id", "items"]
        }
    }

def execute(args, token):
    list_id = args.get("list_id")
    payload = {"items": args.get("items")}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/grocery-lists/{list_id}/items", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.text}"