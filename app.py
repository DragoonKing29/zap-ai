from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from weather_data import WeatherData
from chatbot import ChatbotAI
from emotion import EmotionAI

app = FastAPI()

templates = Jinja2Templates(directory="templates")

weather_ai = WeatherData(api_key='ec191b7342703bc8afae450afe908959')
chatbot_ai = ChatbotAI()
emotion_ai = EmotionAI()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/weather/{location}")
def get_weather(location: str):
    data = weather_ai.get_weather(location)
    if data:
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'coord': data['coord'],
        }
    return {"error": "Could not retrieve weather data"}

@app.post("/chat/")
async def chat_with_ai(request: Request):
    user_input = (await request.json())['message']
    response = chatbot_ai.respond(user_input)
    emotional_response = emotion_ai.add_emotion(response)
    return {"response": emotional_response}
