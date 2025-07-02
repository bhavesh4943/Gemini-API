from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key
GOOGLE_API_KEY = "AIzaSyAZCBwvR2bKgrzbbSKpYSAXXH9TwEhjoS4"
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini 2.0 Flash Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    try:
        response = model.generate_content(f"You are a gaming expert. Answer briefly: {user_input}")
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
