import requests

class WeatherAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_info(self, location: str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json()
