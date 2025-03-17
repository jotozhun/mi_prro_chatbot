import ollama
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

desired_model = os.getenv("DESIRED_AI_MODEL")
question_to_ask = "Solve the problem 10*5+5"

response = ollama.chat(model=desired_model, messages=[
    {
        'role': 'user',
        'content': question_to_ask
    }
])

ollama_response = response['message']['content']

print(ollama_response)
