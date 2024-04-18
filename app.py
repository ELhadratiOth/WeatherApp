import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


def backgroundApp(root):
    image_path = "./static/bg.jpeg"
    image = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if image.width != screen_width or image.height != screen_height:
        image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.background_image = background_image






if __name__ == '__main__':
    root= tk.Tk( )
    root.title("Weather App")
    root.state('zoomed')
    root.resizable(height=False , width=False)
    backgroundApp(root)
    root.mainloop()
