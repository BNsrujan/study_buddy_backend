import os
from dotenv import load_dotenv

load_dotenv()

# Example configuration for API keys, model paths, etc.
API_KEY = os.getenv("API_KEY")
MODEL_PATH = os.getenv("MODEL_PATH", "default_model_path")
