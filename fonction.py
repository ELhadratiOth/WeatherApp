
import openmeteo_requests
from geopy.geocoders import Nominatim
from openmeteo_requests import Client
import requests_cache
from retry_requests import retry
from datetime import datetime
import pandas as pd
import plotly.express as px


def get_current_time():
    return datetime.now().strftime("%I:%M %p")
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
        "current": ["temperature_2m", "relative_humidity_2m", "is_day", "weather_code", "cloud_cover", "pressure_msl",
                    "wind_speed_10m"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_is_day = current.Variables(2).Value()
    current_weather_code = current.Variables(3).Value()
    current_cloud_cover = current.Variables(4).Value()
    current_pressure_msl = current.Variables(5).Value()
    current_wind_speed_10m = current.Variables(6).Value()

    current_time = current.Time()

    # Create a DataFrame
    data = {
        "City": [city_name],
        "Current Time": [current_time],
        "Temperature": [current_temperature_2m],
        "Humidity": [current_relative_humidity_2m],
        "isDay": [current_is_day],
        "Weather Code": [current_weather_code],
        "Cloud": [current_cloud_cover],
        "Pressure": [current_pressure_msl],
        "Wind Speed": [current_wind_speed_10m]
    }

    df = pd.DataFrame(data)

    return df


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
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()

    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ).strftime("%d-%m-%Y")
    }
    daily_data["weather code"] = daily_weather_code
    daily_data["temperature_min"] = daily_temperature_2m_min
    daily_data["temperature_max"] = daily_temperature_2m_max

    daily_dataframe = pd.DataFrame(data=daily_data)
    return daily_dataframe


def outputCurrentT(lastT, code_lastT,isday):
    img = ""
    if int(code_lastT) == 0:
        if isday == 0 :
            img = "./static/1n.png"
        else :
            img = "./static/1.png"
    elif int(code_lastT) in [1, 2, 3]:
        if isday == 0 :
            img = "./static/2n.png"
        else :
            img = "./static/2.png"
    elif int(code_lastT) in [56, 67, 51, 53, 55, 45, 48]:
        if isday == 0 :
            img = "./static/3n.png"
        else :
            img = "./static/3.png"
    elif int(code_lastT) in [61, 63, 65]:
        if isday == 0:
            img = "./static/4n.png"
        else:
            img = "./static/4.png"
    elif int(code_lastT) in [66, 67]:
         img = "./static/6710.png"
    elif int(code_lastT) in [71, 73]:
        if isday == 0:
            img = "./static/5n.png"
        else:
            img = "./static/5.png"
    elif int(code_lastT) in [75, 77]:
        if isday == 0:
            img = "./static/911n.png"
        else:
            img = "./static/911.png"
    elif int(code_lastT) in [80, 81, 82, 85, 86]:
        if isday == 0:
            img = "./static/8n.png"
        else:
            img = "./static/8.png"

    return img

def get_weather_data(city_name):
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
        "latitude":latitude,
        "longitude":longitude,
        "hourly": ["temperature_2m", "rain"],
        "timezone": "auto",
        "forecast_hours": 24
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_rain = hourly.Variables(1).ValuesAsNumpy()

    hourly_data = {
        "hour": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ).strftime("%H:%M")
    }
    hourly_data["temperature"] =hourly_temperature_2m
    hourly_data["rain"] = hourly_rain
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe



# Graphique de variation de la température par heure
hourly_data = get_weather_data("fes")



def variation_tmp(city_name):
    hourly_data = get_weather_data(city_name)
    fig = px.bar(hourly_data, x='hour', y='temperature',
                 color='rain',
                 color_continuous_scale='Viridis', title='TEMPERATURE VARIATION',text="temperature",
                 labels={'temperature': 'Temperature (° C)','hour':'Hours','rain':"Rain"}
    )

    fig.update_layout(
        xaxis=dict(showgrid=True,tickfont=dict(size=15)),
        yaxis=dict(showgrid=True,tickfont=dict(size=15)),
        title_font=dict(size=40),
        yaxis_title_font=dict(size=30), # Taille de la police pour l'axe des y
        xaxis_title_font=dict(size=30),
        #colorway=dict(title=dict(font=dict(size=14))),
        plot_bgcolor='#132530'
    )

    return fig

#print(hourly_data)