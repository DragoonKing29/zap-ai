from tensorflow.keras.models import load_model
import numpy as np

model = load_model("models/dl_model.h5")

def generate_weather_forecast(location):
    # Assuming weather data for the location is pre-processed and loaded
    data = np.array([location_specific_data])
    forecast = model.predict(data)
    return {"forecast": forecast.tolist()}
