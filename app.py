import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


def backgroundApp(root ,x , y ,image_path):
    image = Image.open(image_path)
    specified_width = x
    specified_height = y
    if image.width != specified_width or image.height != specified_height:
        image = image.resize((specified_width , specified_height), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.background_image = background_image






if __name__ == '__main__':
    root= tk.Tk( )
    root.title("Weather App")
    root.geometry("1200x600")

    # root.resizable(height=False , width=False)
    backgroundApp(root)
    root.mainloop()
