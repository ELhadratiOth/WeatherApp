import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import customtkinter
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Weather informations")
root.geometry("1050x650+300+300")
root.resizable(0,0)

# Charger l'image
image_path = "./static/bac.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Créer un canevas avec une taille fixe
canvas = tk.Canvas(root, width=500, height=500)  # Remplacez 500 par la taille de votre image si nécessaire
canvas.pack(fill="both", expand=True)

# Afficher l'image en tant que fond du canevas
canvas.create_image(0, 0, image=photo, anchor="nw")

# Exécuter la boucle principale
root.mainloop()




#weather function which displayed the weather informations
city_value = StringVar()
def showWeather():

    # Get city name from user from the input field (later in the code)
    city_name = city_value.get()
    base='https://api.open-meteo.com/v1/forecast?'

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()

    #tfield.delete("1.0", "end")  #to clear the text field for every new output

    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # -----------Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    #tfield.insert(INSERT, weather)  # to insert or send value in our Text Field to display output
#function to change the time format

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


