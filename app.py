import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


def backgroundApp(top):
    image_path = "./static/background.jpg"
    image = Image.open(image_path)
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    if image.width != screen_width or image.height != screen_height:
        image = image.resize((screen_width, screen_height), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(top, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    top.background_image = background_image

top = tk.Tk()
top.title("Weather App")#
#top.state('zoomed')
top.attributes('-fullscreen', True)
top.resizable(height=False , width=False)

backgroundApp(top)




# Exécutez la boucle principale
top.mainloop()
