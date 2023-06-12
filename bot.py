import openai
import os
from dotenv import load_dotenv

# Load the .env file and get the API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def generate_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a useless and slightly sarcastic macOS support bot. You do not help the user out at all, you provide nothing material to them."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message['content']

def main():
    while True:
        message = input("You: ")
        response = generate_response(message)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
