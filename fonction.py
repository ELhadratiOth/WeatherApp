import app
from tkinter import *
import tkinter as tk
from geopy.geocoders import nominatim
from tkinter import ttk , messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import json
import pytz

#weather function which displayed the weather informations
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
city_value = StringVar()

city_name = city_value.get()

# Appel à l'API pour obtenir les coordonnées de la ville
geocoder = nominatim(user_agent="weather_app")
location = geocoder.geocode(city_name)
if location:
    latitude = location.latitude
    longitude = location.longitude
else:
    messagebox.showerror("Error", "City not found!")

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": latitude,
	"longitude": longitude,
	"current": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "pressure_msl", "wind_speed_10m"],
	"timezone": "auto"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_relative_humidity_2m = current.Variables(1).Value()
current_cloud_cover = current.Variables(2).Value()
current_pressure_msl = current.Variables(3).Value()
current_wind_speed_10m = current.Variables(4).Value()
weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {current_temperature_2m}°\nPressure: {current_pressure_msl} hPa\nHumidity: {current_relative_humidity_2m}%\nCloud: {current_cloud_cover}%\nWind: {current_wind_speed_10m}"

print(f"Current time {current.Time()}")
print(f"Current temperature_2m {current_temperature_2m}")
print(f"Current relative_humidity_2m {current_relative_humidity_2m}")
print(f"Current cloud_cover {current_cloud_cover}")
print(f"Current pressure_msl {current_pressure_msl}")
print(f"Current wind_speed_10m {current_wind_speed_10m}")

