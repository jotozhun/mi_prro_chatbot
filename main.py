import openai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")