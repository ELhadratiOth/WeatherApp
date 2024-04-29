import io
import tkinter as tk
import customtkinter
import tkintermapview
import fonction
import app2
import map
import customtkinter as ctk
from PIL import Image, ImageTk
import plotly.io as pio
CONST_FAHRENHEIT=32
customtkinter.set_default_color_theme("blue")
city_names=""
# Initialisation de la fenêtre
def open_full_map():
    # Function to open the Toplevel window
    toplevel_window = tk.Toplevel()
    toplevel_window.destroy()
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = map.create_map_app(city_names)  # Create the window if it's None or destroyed
    else:
        toplevel_window.focus()

def getMoreDetails(city_name):
    global city_names
    city_names =city_name
    top = tk.Toplevel()
    top.title("Weather informations")
    #top.attributes('-fullscreen', True)
    top.geometry("1300x700")
    top.resizable(0, 0)
    icon_path = "./static/loupe.png"
    image_path="./static/bcopie.psd"
    icon_image = tk.PhotoImage(file=icon_path)

    toplevel_window= tk.Toplevel()
    toplevel_window.destroy()
    top.iconphoto(True, icon_image)
    # Appliquer l'image de fond
    app2.backgroundApp(top,1300,700,image_path)
    frame1 = tk.Frame(top, bg="#132530", width=340, height=250)
    frame1.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
    frame1.place(x=100, y=60)

    frame2 = tk.Frame(top, bg="#132530", width=800, height=290)
    frame2.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
    frame2.place(x=100, y=350)

    frame3 = tk.Frame(top, bg="#132530", width=250, height=290)
    frame3.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
    frame3.place(x=950, y=347)

    frame4 = tk.Frame(top, bg="#132530", width=600, height=250)
    frame4.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
    frame4.place(x=466, y=60)

    frame5 = tk.Frame(top, bg="#132530", width=120, height=250)
    frame5.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
    frame5.place(x=1100, y=60)
    def ImagAdd(img , size):
        my_image = ctk.CTkImage(light_image=Image.open(img),
                                          size=(size, size))
        return my_image

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

    # Bouton pour ouvrir la carte complète
    open_map_button = ctk.CTkButton(master=my_label,fg_color="#04303f", text="Open Full Map", command=open_full_map)
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
    jour = int(data["isDay"])

    weather_image_path = fonction.outputCurrentT(lastT, code_lastT, jour)  # Remplacer par le chemin de votre image météo
    print(weather_image_path)
    resized_img=ImagAdd(weather_image_path,80)
    #weather_image = tk.PhotoImage(file=weather_image_path)

    #weather_image_resized = weather_image.subsample(5, 5)  # 2 représente la moitié de la taille

    data = fonction.get_current_weather(city_name)
    # Frame pour l'image météo et l'affichage de la température
    weather_temp_frame = tk.Frame(frame1, bg="#132530")
    weather_temp_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=5, anchor="w")

    # Label pour l'image météo, aligné à gauche avec une marge à gauche
    weather_label = ctk.CTkLabel(weather_temp_frame, image=resized_img,text="", bg_color="#132530")
    weather_label.pack(side=tk.LEFT, padx=(0, 10),pady=(16,10), anchor="w")  # Alignement à gauche avec marge à droite

    # Label pour l'affichage de la température, aligné à gauche avec la même taille de police et en gras

    temperature_label = tk.Label(weather_temp_frame, text=f"{int(data['Temperature'])} °C",
                                 font=("Helvetica", 50, "bold"), fg="white", bg="#132530")
    temperature_label.pack(side=tk.LEFT, padx=(10, 0), anchor="w")

    data = fonction.get_current_weather(city_name)
    icon_values = data.drop(['Temperature','isDay', 'Weather Code', 'City', 'Current Time'], axis=1)

    # Création des labels pour chaque icône et sa valeur
    icon_frame = tk.Frame(frame1, bg="#132530")
    icon_frame.pack(anchor="w", padx=20, pady=(0, 5), fill=tk.X)

    for icon in icon_values.columns:
        icon_label = tk.Label(icon_frame, text=icon, font=("Helvetica", 10, "bold"), fg="white", bg="#132530")
        icon_label.pack(side=tk.LEFT, padx=(0, 10))

    value_frame = tk.Frame(frame1, bg="#132530")
    value_frame.pack(anchor="w", padx=20, pady=(0, 5), fill=tk.X)
    liste_value_label=[]
    for index, row in icon_values.iterrows():
        for icon in icon_values.columns:
            value_label = tk.Label(value_frame, text=str(int(row[icon])), font=("Helvetica", 12, "bold"), fg="white",
                                   bg="#132530")
            value_label.pack(side=tk.LEFT, padx=20, pady=(0, 5))
            liste_value_label.append(value_label)

    forecast_title_frame = ctk.CTkFrame(frame3, fg_color="#1a1a1a", bg_color="transparent",width=400, height=40,corner_radius=33)
    forecast_title_frame.pack_propagate(0)
    forecast_title_frame.place(x=0, y=0)
    forecast_label = tk.Label(forecast_title_frame, text="Forecast", fg="white", bg="#1a1a1a",
                              font=("Helvetica", 14, "bold"))
    forecast_label.pack(pady=5, padx=5, side="left")
    label_7 = tk.Label(forecast_title_frame, text="6 days", font=("Helvetica", 10), fg="white", bg="#1a1a1a")
    label_7.pack(side=tk.LEFT, padx=90, pady=(0, 5))

    daily_data = fonction.get_daily_weather_forecast(city_name)
    liste_temp_label=[]
    for index, row in daily_data.iterrows():
        if (index == 0):
            continue

        c_l = int(row["weather code"])

        img_weather_path = fonction.outputCurrentT(lastT, c_l,jour)
        im_resized=ImagAdd(img_weather_path,30)
        img_weather = tk.PhotoImage(file=img_weather_path)
        img_weather_re = img_weather.subsample(20, 20)
        temp_text = f"{int(row['temperature_min'])}°/{int(row['temperature_max'])}°"

        day_frame = tk.Frame(frame3, bg="#132530", width=800, height=40)
        day_frame.pack_propagate(0)
        day_frame.place(x=0, y=40 + ((index - 1) * 40))

        weather_label = ctk.CTkLabel(day_frame, image=im_resized,text="", bg_color="#132530")

        weather_label.image = img_weather_re
        weather_label.pack(pady=5, padx=10, side="left")

        temp_label = tk.Label(day_frame, text=temp_text, fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
        temp_label.pack(pady=5, padx=15, side="left")
        liste_temp_label.append(temp_label)

        date_label = tk.Label(day_frame, text=row["date"], fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
        date_label.pack(pady=5, padx=30, side="left")


    setting_label = ctk.CTkLabel(frame5, text="Settings", width=100,height=30,corner_radius=15,fg_color="#1a1a1a", bg_color="#132530", font=("Helvetica", 16, "bold"))
    setting_label.pack(pady=(10, 0), padx=5, side="left")
    setting_label.place(x=0,y=0)

    # Options pour les unités
    temp_options = ["Celsius °C", "Fahrenheit °F"]
    pres_options = ["bar", "hPa"]
    win_options = ["km/h", "m/s"]

    def update_temperature_unit(new_value:str):
        if new_value=="Celsius °C":
            temperature_label.config(text=f"{int(data['Temperature'])} °C")
            for i, r in daily_data.iterrows():
                for temp in liste_temp_label:
                    if i==0:
                        continue
                    temp.config(text=f"{int(r['temperature_min'])}°/{int(r['temperature_max'])}°")
        elif new_value=="Fahrenheit °F":
            temperature_label.config(text=f"{int(data['Temperature'])+CONST_FAHRENHEIT} °F")
            for i, r in daily_data.iterrows():
                for temp in liste_temp_label:
                    if i==0:
                        continue
                    temp.config(text=f"{int(r['temperature_min'])+CONST_FAHRENHEIT}°/{int(r['temperature_max'])+CONST_FAHRENHEIT}°")

    def update_pressure_unit(new_value:str):
        if new_value == "bar":
            for k, l in icon_values.iterrows():
                for _ in icon_values.columns:
                    for val in liste_value_label:
                        if k==2:
                            val.config(text=f"{float(l[_])+0.001}")

        elif  new_value=="hPa":
            for k, l in icon_values.iterrows():
                for _ in icon_values.columns:
                    for val in liste_value_label:
                        if k==2:
                            val.config(text=f"{int(l[_])}")




    def update_wind_speed_unit(new_value:str):
        if new_value == "Km/h":
            for m, n in icon_values.iterrows():
                for p in icon_values.columns:
                    for val in liste_value_label:
                        if m==3:
                            value_label.config(text=f"{int(n[p])}")
        elif new_value == "m/s":
            for m, n in icon_values.iterrows():
                for p in icon_values.columns:
                    for val in liste_value_label:
                        if m==3:
                            value_label.config(text=f"{float(n[p])+0.28}")
    # Labels et menus déroulants pour les unités
    temperature_unit_label = tk.Label(frame5, text="Temperature Unit:", fg="white", bg="#132530",
                                      font=("Helvetica", 10, "bold"))
    temperature_unit_label.pack(anchor="w", padx=5, pady=(35, 0))

    temperature_unit_dropdown = customtkinter.CTkOptionMenu(frame5, fg_color="#04303f",values=temp_options,
                                                            command=update_temperature_unit)
    temperature_unit_dropdown.pack(anchor="w", padx=5, pady=5)
    temperature_unit_dropdown.set("Celsius °C")

    pressure_unit_label = tk.Label(frame5, text="Pressure Unit:", fg="white", bg="#132530", font=("Helvetica", 10, "bold"))
    pressure_unit_label.pack(anchor="w", padx=5, pady=(15, 5))
    pressure_unit_dropdown = customtkinter.CTkOptionMenu(frame5,fg_color="#04303f" ,values=pres_options, command=update_pressure_unit)
    pressure_unit_dropdown.pack(anchor="w", padx=5)
    pressure_unit_dropdown.set("hPa")

    wind_speed_unit_label = tk.Label(frame5, text="Wind Speed Unit:", fg="white", bg="#132530",
                                     font=("Helvetica", 10, "bold"))
    wind_speed_unit_label.pack(anchor="w", padx=5, pady=(15, 5))
    wind_speed_unit_dropdown = customtkinter.CTkOptionMenu(frame5,fg_color="#04303f", values=win_options,
                                                           command=update_wind_speed_unit)
    wind_speed_unit_dropdown.pack(anchor="w", padx=5)
    wind_speed_unit_dropdown.set("Km/h")
    #Affichage de la variation de la temperature de la journée

    fig=fonction.variation_tmp(city_name)
    img_bytes = pio.to_image(fig, format="png")

    # Convertissez les octets en une image tkinter
    img = Image.open(io.BytesIO(img_bytes))
    width_img, height_img = img.size
    print(width_img,height_img)
    max_width = 800  # Largeur maximale du cadre
    max_height = 290  # Hauteur maximale du cadre
    resize_factor = min(max_width / width_img, max_height / height_img)
    new_width = int(width_img * resize_factor)
    new_height = int(height_img * resize_factor)
    img = img.resize((max_width, new_height))

    img_tk = ImageTk.PhotoImage(img)

    # Créez un label tkinter pour afficher l'image
    label = tk.Label(frame2,width=800,bg='#132530', image=img_tk)
    label.place(x=0,y=0)

    # Gardez une référence à l'image tkinter pour éviter la suppression de l'image
    label.image = img_tk
    return top

