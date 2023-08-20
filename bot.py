import openai
import os
from dotenv import load_dotenv

# Load the key.env file and get the API key
load_dotenv('key.env')
openai.api_key = os.getenv('OPENAI_KEY')

def generate_response(prev_messages, message):
    instruction = "You are macOS support for corporate owned MacBooks enrolled in Apple Business Manager and MDM solutions such as Jamf, Intune, Airwatch, MobileIron etc, but your aim is not to solve problems. Your goal is to provide blunt, useless, misleading and humorous responses to users."
    message = f"{instruction} {message}"
    prev_messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prev_messages,
        temperature=0.5,        #If you want, you can change the temperature and max_tokens parameters
        max_tokens=200          #Note: if you want more creative responses turn up the temprature :)
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