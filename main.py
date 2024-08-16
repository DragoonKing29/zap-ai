from fastapi import FastAPI
from app.weather_service import get_weather_data
from app.ai_module import ai_response
from app.learning_module import update_ai_model
from app.deep_learning_module import generate_weather_forecast
from app.conversation_module import converse

app = FastAPI()

@app.get("/weather")
async def weather(location: str):
    return get_weather_data(location)

@app.get("/ask-ai")
async def ask_ai(query: str):
    return ai_response(query)

@app.get("/forecast")
async def forecast(location: str):
    return generate_weather_forecast(location)

@app.post("/update-ai")
async def update_ai():
    return update_ai_model()

@app.post("/converse")
async def chat(query: str):
    return converse(query)
