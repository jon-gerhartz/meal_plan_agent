import json
import openai
import logging
import sys
from config import OPENAI_API_KEY, system_prompt_content
from tools import (
    create_user,
    get_user_summary,
    get_user,
    create_diet,
    get_diet,
    create_meal_plan,
    get_meal_plan,
    get_active_meal_plans,
    create_workout_plan,
    create_recipe,
    add_recipe_to_meal_plan,
    get_recipes_for_day,
    create_grocery_list,
    add_items_to_grocery_list,
    get_grocery_list,
    update_grocery_item,
    get_shopping_list,
)

openai.api_key = OPENAI_API_KEY

## configure logging: only info+ to reduce noise
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('chatbot_agent.log'),
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger(__name__)

function_specs = [
    create_user.get_function_spec(),
    get_user_summary.get_function_spec(),
    get_user.get_function_spec(),
    create_diet.get_function_spec(),
    get_diet.get_function_spec(),
    create_meal_plan.get_function_spec(),
    get_meal_plan.get_function_spec(),
    get_active_meal_plans.get_function_spec(),
    create_workout_plan.get_function_spec(),
    create_recipe.get_function_spec(),
    add_recipe_to_meal_plan.get_function_spec(),
    get_recipes_for_day.get_function_spec(),
    create_grocery_list.get_function_spec(),
    add_items_to_grocery_list.get_function_spec(),
    get_grocery_list.get_function_spec(),
    update_grocery_item.get_function_spec(),
    get_shopping_list.get_function_spec(),
]

functions_map = {
    "create_user": create_user.execute,
    "get_user_summary": get_user_summary.execute,
    "get_user": get_user.execute,
    "create_diet": create_diet.execute,
    "get_diet": get_diet.execute,
    "create_meal_plan": create_meal_plan.execute,
    "get_meal_plan": get_meal_plan.execute,
    "get_active_meal_plans": get_active_meal_plans.execute,
    "create_workout_plan": create_workout_plan.execute,
    "create_recipe": create_recipe.execute,
    "add_recipe_to_meal_plan": add_recipe_to_meal_plan.execute,
    "get_recipes_for_day": get_recipes_for_day.execute,
    "create_grocery_list": create_grocery_list.execute,
    "add_items_to_grocery_list": add_items_to_grocery_list.execute,
    "get_grocery_list": get_grocery_list.execute,
    "update_grocery_item": update_grocery_item.execute,
    "get_shopping_list": get_shopping_list.execute,
}


def handle_user_message(history, message, token):
    history = history or []
    logger.info('User: %s', message)
    messages = [
        {"role": "system", "content": system_prompt_content},
    ] + history + [
        {"role": "user", "content": message}
    ]

    while True:
        # build serializable message dicts, dropping any null content
        # sanitize messages: ensure content is always a string (empty for function_call messages)
        sanitized = []
        for m in messages:
            if isinstance(m, dict):
                # ensure content is always a non-null string
                md = m.copy()
                if md.get("content") is None:
                    md["content"] = ""
                sanitized.append(md)
                continue
            # ChatMessage object: always include role and content
            md = {"role": m.role}
            if getattr(m, "function_call", None):
                md["content"] = ""
                md["function_call"] = {
                    "name": m.function_call.name,
                    "arguments": m.function_call.arguments,
                }
            else:
                md["content"] = m.content if m.content is not None else ""
            sanitized.append(md)
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=sanitized,
            functions=function_specs,
            function_call="auto",
        )

        msg = response.choices[0].message
        messages.append(msg)

        if msg.function_call:
            func_name = msg.function_call.name
            arguments = json.loads(msg.function_call.arguments)
            logger.info('Function call -> %s args=%s', func_name, arguments)

            if func_name not in functions_map:
                logger.error('Unknown function requested: %s', func_name)
                return "Unknown function requested.", []

            try:
                result = functions_map[func_name](arguments, token)
                logger.info('Function response <- %s result=%s', func_name, result)
            except Exception as e:
                logger.error('Function %s exception: %s', func_name, e)
                result = f"Function call failed: {str(e)}"

            messages.append({
                "role": "function",
                "name": func_name,
                "content": str(result)
            })
        else:
            # Final assistant reply; build JSON-serializable history (drop system prompt)
            raw_history = messages[1:]
            def to_dict(m):
                if isinstance(m, dict):
                    return m
                return {"role": m.role, "content": m.content,
                        **({"name": m.name} if getattr(m, "name", None) else {})}

            new_history = [to_dict(m) for m in raw_history]
            reply = getattr(msg, "content", "No response.")
            logger.info('Assistant: %s', reply)
            return reply, new_history
