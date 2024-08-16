import os

WEATHER_API_KEY = os.getenv("6ff5a94f7825ba6f1bef6a64c543ec44", "your_default_key")
AI_MODEL_PATH = os.getenv("AI_MODEL_PATH", "models/ai_model.pkl")
DL_MODEL_PATH = os.getenv("DL_MODEL_PATH", "models/dl_model.h5")
