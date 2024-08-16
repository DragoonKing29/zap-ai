import requests
from cachetools import TTLCache

API_KEY = "6ff5a94f7825ba6f1bef6a64c543ec44"
cache = TTLCache(maxsize=100, ttl=300)

def get_weather_data(location):
    if location in cache:
        return cache[location]
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cache[location] = data
        return data
    else:
        return {"error": "Unable to fetch weather data"}
