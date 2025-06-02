# Fetch weather data from OpenWeatherMap API

import requests
import datetime

API_KEY = "01d344e75b42ca730f08c0a811bf033e"

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}fetching data: {response.status_code}")

# wether api :https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def fetch_location(city, state=None, country=None):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city},{state},{country}" if state and country else city,
        "limit": 1,
        "appid": API_KEY
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]
        else:
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None
    
def fetch_weather(lat, lon):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"  # Optional: to get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None
    
def main():
    city = "stuttgart"
    state = "BW"
    country = "DE"
    weather_data = fetch_location(city, state, country) 
    if weather_data:
        print(f"Latitude: {weather_data['lat']}, Longitude: {weather_data['lon']}")
        weather = fetch_weather(weather_data['lat'], weather_data['lon'])
        if weather:
            print(f"Weather data: {weather}")
        else:
            print("Failed to fetch weather data.")

    else:
        print("Weather data not found.")

if __name__ == "__main__":
    main()
    