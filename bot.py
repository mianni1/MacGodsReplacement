import openai
import os
from dotenv import load_dotenv

# Load the .env file and get the API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def generate_response(prev_messages, message):
    instruction = "You are macOS support, but your aim is not to solve problems. Your goal is to provide creative, unique, and surprising responses that are humorous."
    message = f"{instruction} {message}"
    prev_messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prev_messages,
        temperature=0.5,
        max_tokens=200
    )

    return response.choices[0].message['content'], prev_messages

def main():
    prev_messages = [
        {"role": "system", "content": "You are a creative and surprising macOS support assistant. Your purpose is to provide unique and humorous responses."}
    ]
    while True:
        message = input("You: ")
        response, prev_messages = generate_response(prev_messages, message)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()