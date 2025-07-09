#!/usr/bin/env python3
"""
Terminal-based chat client for the Meal Planner chatbot agent.

Runs an interactive REPL: you type messages, the script calls /chat (threading history),
and prints the assistant response. Ctrl-D or Ctrl-C to exit.

Usage:
  # Ensure Flask server is running (python app.py)
  python test_chat.py
"""

import os
import requests
from requests.exceptions import HTTPError
from dotenv import load_dotenv

load_dotenv()

# URL of the chatbot endpoint (override via CHAT_URL env var)
CHAT_URL = os.getenv("CHAT_URL", "http://127.0.0.1:5000/chat")
# Bearer token to use (override via CHAT_TOKEN env var)
CHAT_TOKEN = os.getenv("CHAT_TOKEN", "test-token")


def chat(history, message):
    payload = {"history": history, "message": message, "token": CHAT_TOKEN}
    resp = requests.post(CHAT_URL, json=payload)
    try:
        resp.raise_for_status()
    except HTTPError as e:
        print(f"HTTP error: {e} - {resp.text}")
        return None, history
    data = resp.json()
    return data.get("reply"), data.get("history", [])


def main():
    print(f"Chat endpoint: {CHAT_URL}")
    print(f"Using token:  {CHAT_TOKEN}")
    print("Type your messages below (Ctrl-D to exit):\n")
    history = []
    while True:
        try:
            message = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not message:
            continue
        reply, history = chat(history, message)
        if reply is None:
            break
        print(f"{reply}\n")


if __name__ == '__main__':
    main()
