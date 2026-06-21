import google.generativeai as genai

from app.config.settings import Config

genai.configure(
    api_key=Config.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)