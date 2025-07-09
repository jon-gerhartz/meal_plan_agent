# Meal Planner Chatbot Agent

This Flask‑based agent wraps OpenAI GPT‑4 function‑calling to interact with your Meal Planner API.
It supports adding meals, diets, workout plans, recipes, grocery lists, and fetching a unified user summary.

## Quickstart (Local Development)

1. **Clone the repo**
   ```bash
   git clone <repo_url>
   cd chatbot_agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   Create a `.env` file in this directory:
   ```dotenv
   OPENAI_API_KEY=your_openai_api_key
   BACKEND_API_URL=https://your-backend-api.com/api
   ```

4. **Run the app**
   ```bash
   python app.py
   ```
   The server will listen on `http://127.0.0.1:5000` by default.

5. **Chat via HTTP**
   Send a POST to `/chat`:
   ```bash
   curl -X POST http://127.0.0.1:5000/chat \
        -H 'Content-Type: application/json' \
        -d '{"message":"Hello, agent!","token":"dummy-token"}'
   ```

6. **Interactive REPL**
   Alternatively, you can run the built‑in REPL client:
   ```bash
   python test_chat.py
   ```

## Deployment (Railway/Heroku)

This repo includes a `Procfile` and uses `gunicorn` in `requirements.txt` for production.

1. Push to a Git remote.
2. Create a new Railway (or Heroku) project and link your repo.
3. Add environment variables (`OPENAI_API_KEY`, `BACKEND_API_URL`, etc.) via the dashboard.
4. Railway will auto‑deploy and run `web: gunicorn app:app`.

## Logging

By default, logs are output to both console and `chatbot_agent.log`. Only essential user, assistant, and function‑call events are logged.

---

If you run into any issues, please check the logs or open an issue.