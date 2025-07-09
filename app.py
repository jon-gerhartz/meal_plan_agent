from flask import Flask, request, jsonify
from chatbot_agent import handle_user_message

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    message = data.get("message")
    token = data.get("token")
    history = data.get("history", [])

    if not isinstance(history, list):
        return jsonify({"error": "Invalid history format, must be a list"}), 400
    if not message or not token:
        return jsonify({"error": "Missing message or token"}), 400

    try:
        reply, new_history = handle_user_message(history, message, token)
        return jsonify({"reply": reply, "history": new_history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)