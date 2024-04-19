import json
from urllib.request import urlopen
import requests
import time
def getCurrentLocation():
    url="http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    print(data)
    latitude=data['loc'].split(',')[0]
    longitude=data['loc'].split(',')[1]
    weatherApiUrl = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    getting_weather= requests.get(weatherApiUrl)
    currentWeather = getting_weather.json()
    print(currentWeather)



