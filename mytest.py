from tkinter import *
import tkintermapview
import tkinter as tk



root=tk.Tk()
root.title('My map')
#root.iconbitmap()
icon_path = "./static/loupe.png"
icon_image = tk.PhotoImage(file=icon_path)

root.iconphoto(True, icon_image)
root.geometry('900x700')
my_label=LabelFrame(root)
my_label.pack(pady=20)
my_widget=tkintermapview.TkinterMapView(my_label,width=800,height=600,corner_radius=0)
my_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#set cordinates
#my_widget.set_position(12.7,-5.67)
# set current widget position by address
marker_1 = my_widget.set_address("colosseo, rome, italy", marker=True)

print(marker_1.position, marker_1.text)  # get position and text

marker_1.set_text("Colosseo in Rome")  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()
my_widget.set_zoom(15)
my_widget.pack()


import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": ["temperature_2m", "rain", "weather_code"],
	"timezone": "auto",
	"forecast_hours": 24
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_rain = hourly.Variables(1).ValuesAsNumpy()
hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["rain"] = hourly_rain
hourly_data["weather_code"] = hourly_weather_code

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)







root.mainloop()