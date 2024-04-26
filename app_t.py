import tkinter as tk
import customtkinter
import tkintermapview
import fonction
import app
import map
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import cartography as ct

from tkintermapview import TkinterMapView

customtkinter.set_default_color_theme("blue")

# Initialisation de la fenêtre
top = tk.Tk()
top.title("Weather informations")
#top.attributes('-fullscreen', True)
top.geometry("1300x700")
top.resizable(0, 0)
icon_path = "./static/loupe.png"
icon_image = tk.PhotoImage(file=icon_path)
city_name ="rabat"
top.iconphoto(True, icon_image)
# Appliquer l'image de fond
app.backgroundApp(top)
frame1 = tk.Frame(top, bg="#132530", width=340, height=250)
frame1.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame1.place(x=100, y=60)

frame2 = tk.Frame(top, bg="#132530", width=800, height=290)
frame2.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame2.place(x=100, y=320)

frame3 = tk.Frame(top, bg="#132530", width=250, height=290)
frame3.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame3.place(x=950, y=320)

frame4 = tk.Frame(top, bg="#132530", width=600, height=250)
frame4.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame4.place(x=470, y=60)

frame5 = tk.Frame(top, bg="#132530", width=120, height=250)
frame5.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame5.place(x=1100, y=60)

#Affichage current informations

my_label = tk.LabelFrame(frame4)
my_label.pack(pady=0)
my_widget = tkintermapview.TkinterMapView(my_label, width=600, height=250, corner_radius=0)
my_widget.place(x=0, y=0)
# set cordinates
# my_widget.set_position(12.7,-5.67)
# set current widget position by address
marker_1 = my_widget.set_address(city_name, marker=True)

print(marker_1.position, marker_1.text)  # get position and text

marker_1.set_text(city_name)  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()
my_widget.set_zoom(15)
my_widget.pack()

def open_full_map():
    ct.map.create_map_app(city_name)


# Bouton pour ouvrir la carte complète
open_map_button = ctk.CTkButton(master=my_label, text="Open Full Map", command=open_full_map)
open_map_button.place(x=250, y=200)

# Label pour le titre "Current Weather"
title_label = tk.Label(frame1, text="Current Weather", font=("Helvetica", 14, "bold"), fg="white", bg="#132530")
title_label.pack(side=tk.TOP, padx=(20, 0), pady=(10, 0), anchor="w")  # Ajouter un petit espace en haut
data = fonction.get_current_weather(city_name)
time_label = tk.Label(frame1, text=fonction.get_current_time(), font=("Helvetica", 12, "bold"), fg="white",
                      bg="#132530")
time_label.pack(side=tk.TOP, padx=(20, 0), pady=(0, 5), anchor="w")
lastT = int(data["Temperature"])
code_lastT = int(data["Weather Code"])
print(lastT, code_lastT)
weather_image_path = fonction.outputCurrentT(lastT, code_lastT)  # Remplacer par le chemin de votre image météo
print(weather_image_path)
weather_image = tk.PhotoImage(file=weather_image_path)
image_height = weather_image.height()
weather_image_resized = weather_image.subsample(5, 5)  # 2 représente la moitié de la taille

data = fonction.get_current_weather(city_name)
# Frame pour l'image météo et l'affichage de la température
weather_temp_frame = tk.Frame(frame1, bg="#132530")
weather_temp_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5, anchor="w")

# Label pour l'image météo, aligné à gauche avec une marge à gauche
weather_label = tk.Label(weather_temp_frame, image=weather_image_resized, bg="#132530")
weather_label.pack(side=tk.LEFT, padx=(0, 10), anchor="w")  # Alignement à gauche avec marge à droite

# Label pour l'affichage de la température, aligné à gauche avec la même taille de police et en gras
font_size = int(image_height * 0.1)
temperature_label = tk.Label(weather_temp_frame, text=f"{int(data['Temperature'])} °C",
                             font=("Helvetica", font_size, "bold"), fg="white", bg="#132530")
temperature_label.pack(side=tk.LEFT, padx=(10, 0), anchor="w")

data = fonction.get_current_weather(city_name)
icon_values = data.drop(['Temperature', 'Weather Code', 'City', 'Current Time'], axis=1)

# Création des labels pour chaque icône et sa valeur
icon_frame = tk.Frame(frame1, bg="#132530")
icon_frame.pack(anchor="w", padx=20, pady=(0, 5), fill=tk.X)

for icon in icon_values.columns:
    icon_label = tk.Label(icon_frame, text=icon, font=("Helvetica", 10, "bold"), fg="white", bg="#132530")
    icon_label.pack(side=tk.LEFT, padx=(0, 10))

value_frame = tk.Frame(frame1, bg="#132530")
value_frame.pack(anchor="w", padx=20, pady=(0, 5), fill=tk.X)

for index, row in icon_values.iterrows():
    for icon in icon_values.columns:
        value_label = tk.Label(value_frame, text=str(int(row[icon])), font=("Helvetica", 12, "bold"), fg="white",
                               bg="#132530")
        value_label.pack(side=tk.LEFT, padx=20, pady=(0, 5))

forecast_title_frame = tk.Frame(frame3, bg="#1a1a1a", width=800, height=40)
forecast_title_frame.pack_propagate(0)
forecast_title_frame.place(x=0, y=0)
forecast_label = tk.Label(forecast_title_frame, text="Forecast", fg="white", bg="#1a1a1a",
                          font=("Helvetica", 14, "bold"))
forecast_label.pack(pady=5, padx=5, side="left")
label_7 = tk.Label(forecast_title_frame, text="6 days", font=("Helvetica", 10), fg="white", bg="#1a1a1a")
label_7.pack(side=tk.LEFT, padx=90, pady=(0, 5))

daily_data = fonction.get_daily_weather_forecast(city_name)

for index, row in daily_data.iterrows():
    if (index == 0):
        continue

    c_l = int(row["weather code"])

    img_weather_path = fonction.outputCurrentT(lastT, c_l)
    img_weather = tk.PhotoImage(file=img_weather_path)
    img_weather_re = img_weather.subsample(20, 20)
    temp_text = f"{int(row['temperature_min'])}°/{int(row['temperature_max'])}°"

    day_frame = tk.Frame(frame3, bg="#132530", width=800, height=40)
    day_frame.pack_propagate(0)
    day_frame.place(x=0, y=40 + ((index - 1) * 40))

    weather_label = tk.Label(day_frame, image=img_weather_re, bg="#132530")
    weather_label.image = img_weather_re
    weather_label.pack(pady=5, padx=10, side="left")

    temp_label = tk.Label(day_frame, text=temp_text, fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
    temp_label.pack(pady=5, padx=15, side="left")

    date_label = tk.Label(day_frame, text=row["date"], fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
    date_label.pack(pady=5, padx=30, side="left")

setting_title_frame = tk.Frame(frame5, bg="#1a1a1a", width=120, height=30)
setting_title_frame.pack_propagate(0)
setting_title_frame.place(x=0, y=0)
setting_label = tk.Label(setting_title_frame, text="Settings", fg="white", bg="#1a1a1a", font=("Helvetica", 16, "bold"))
setting_label.pack(pady=(10, 0), padx=5, side="left")

# Options pour les unités
temp_options = ["Celsius °C", "Fahrenheit °F"]
pres_options = ["mbar", "hPa"]
win_options = ["km/h", "m/s"]

# Labels et menus déroulants pour les unités
temperature_unit_label = tk.Label(frame5, text="Temperature Unit:", fg="white", bg="#132530",
                                  font=("Helvetica", 10, "bold"))
temperature_unit_label.pack(anchor="w", padx=5, pady=(35, 0))

temperature_unit_dropdown = customtkinter.CTkOptionMenu(frame5, values=temp_options,
                                                        command=fonction.update_temperature_unit)
temperature_unit_dropdown.pack(anchor="w", padx=5, pady=5)
temperature_unit_dropdown.set("Celsius °C")

pressure_unit_label = tk.Label(frame5, text="Pressure Unit:", fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
pressure_unit_label.pack(anchor="w", padx=5, pady=(15, 5))
pressure_unit_dropdown = customtkinter.CTkOptionMenu(frame5, values=pres_options, command=fonction.update_pressure_unit)
pressure_unit_dropdown.pack(anchor="w", padx=5)
pressure_unit_dropdown.set("hPa")

wind_speed_unit_label = tk.Label(frame5, text="Wind Speed Unit:", fg="white", bg="#132530",
                                 font=("Helvetica", 10, "bold"))
wind_speed_unit_label.pack(anchor="w", padx=5, pady=(15, 5))
wind_speed_unit_dropdown = customtkinter.CTkOptionMenu(frame5, values=win_options,
                                                       command=fonction.update_wind_speed_unit)
wind_speed_unit_dropdown.pack(anchor="w", padx=5)
wind_speed_unit_dropdown.set("Km/h")
#Affichage de forecast informatons


top.mainloop()
