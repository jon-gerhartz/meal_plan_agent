import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "update_grocery_item",
        "description": "Mark a grocery item as purchased or unpurchased",
        "parameters": {
            "type": "object",
            "properties": {
                "item_id": {"type": "integer", "description": "ID of the grocery item"},
                "purchased": {"type": "boolean", "description": "True if purchased"}
            },
            "required": ["item_id", "purchased"]
        }
    }

def execute(args, token):
    item_id = args.get("item_id")
    payload = {"purchased": args.get("purchased")}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.patch(f"{BACKEND_API_URL}/grocery-items/{item_id}", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"