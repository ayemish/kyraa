# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# === OpenAI Config ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# === CORS ===
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# === Other constants can go here too ===
DEFAULT_TEMPERATURE = 0.0
