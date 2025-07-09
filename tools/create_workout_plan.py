import requests
from config import BACKEND_API_URL

def get_function_spec():
    return {
        "name": "create_workout_plan",
        "description": "Create a new workout plan for a user",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)"},
                "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)"},
                "summary_of_activity": {"type": "string", "description": "Free text summary of activities"}
            },
            "required": ["start_date", "end_date"]
        }
    }

def execute(args, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BACKEND_API_URL}/workout-plans", json=args, headers=headers)
    if response.status_code == 200:
        return response.json().get("message")
    else:
        return f"Error: {response.text}"