import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# always check google gemini api documentation for latest release
def summarize_content(content: str):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Summarize this note in 1-2 sentences: {content}"
        )
    return response.text