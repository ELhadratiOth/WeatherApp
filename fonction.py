from geopy.geocoders import Nominatim
from openmeteo_requests import Client
import requests_cache
from retry_requests import retry
import pytz

def get_current_weather(city_name):
    # Appel à l'API pour obtenir les coordonnées de la ville
    geocoder = Nominatim(user_agent="weather_app")
    location = geocoder.geocode(city_name)
    if location:
        latitude = location.latitude
        longitude = location.longitude
    else:
        raise ValueError("City not found!")

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = Client(session=retry_session)

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

    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_cloud_cover = current.Variables(2).Value()
    current_pressure_msl = current.Variables(3).Value()
    current_wind_speed_10m = current.Variables(4).Value()

    current_time = current.Time()

    weather_dict = {
        "city_name": city_name,
        "current_time": current_time,
        "current_temperature_2m": current_temperature_2m,
        "current_relative_humidity_2m": current_relative_humidity_2m,
        "current_cloud_cover": current_cloud_cover,
        "current_pressure_msl": current_pressure_msl,
        "current_wind_speed_10m": current_wind_speed_10m
    }

    return weather_dict



import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def get_daily_weather_forecast(city_name):
    # Appel à l'API pour obtenir les coordonnées de la ville
    geocoder = Nominatim(user_agent="weather_app")
    location = geocoder.geocode(city_name)
    if location:
        latitude = location.latitude
        longitude = location.longitude
    else:
        raise ValueError("City not found!")
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ).strftime("%d-%m-%Y")
    }
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["temperature_2m_min"] = daily_temperature_2m_min

    daily_dataframe = pd.DataFrame(data=daily_data)
    return daily_dataframe

# Example usage:
city="Casablanca"
daily_weather_forecast = get_daily_weather_forecast(city)
print(daily_weather_forecast)

# Example usage:
city_name = "Casablanca"  # Set your desired city name here
weather_info = get_current_weather(city_name)
print(weather_info)
