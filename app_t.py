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
    image_path = "./static/josh.psd"
    image = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if image.width != screen_width or image.height != screen_height:
        image = image.resize((screen_width, screen_height), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.background_image = background_image


# Initialisation de la fenêtre
top = tk.Tk()
top.title("Weather informations")
top.attributes('-fullscreen', True)
# icon_path = "./static/loupe.png"
# icon_image = tk.PhotoImage(file=icon_path)

# top.iconphoto(True, icon_image)
# Appliquer l'image de fond
backgroundApp(top)
frame1 = tk.Frame(top, bg="#132530", width=340, height=300)
frame1.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame1.place(x=100, y=75)

frame2 = tk.Frame(top, bg="#132530", width=800, height=300)
frame2.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame2.place(x=100, y=395)

frame3 = tk.Frame(top, bg="#132530", width=340, height=300)
frame3.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame3.place(x=940, y=395)

frame4 = tk.Frame(top, bg="#132530", width=650, height=300)
frame4.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame4.place(x=470, y=75)

frame5 = tk.Frame(top, bg="#132530", width=80, height=300)
frame5.pack_propagate(0)  # Empêche le cadre de redimensionner son contenu
frame5.place(x=900, y=75)
top.mainloop()

