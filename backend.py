import openai
from pymongo import MongoClient
import os

# Set OpenAI API key (replace with your own)
openai.api_key = "snclsytvnlshtsnhvt"

# MongoDB connection
client = MongoClient("mongodb+srv://tintin:tintin@cluster0.qot4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["health_bot_db"]
chat_logs = db["chat_logs"]

def generate_response(prompt):
    """Generate response from OpenAI API using the updated interface."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful health and medical assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating response: {e}"

def save_chat(user_id, user_message, bot_response):
    """Save chat logs to MongoDB."""
    try:
        chat_logs.insert_one({
            "user_id": user_id,
            "user_message": user_message,
            "bot_response": bot_response
        })
    except Exception as e:
        print(f"Error saving chat: {e}")

def get_chat_history(user_id):
    """Retrieve chat history from MongoDB."""
    try:
        return list(chat_logs.find({"user_id": user_id}))
    except Exception as e:
        print(f"Error retrieving chat history: {e}")
        return []
