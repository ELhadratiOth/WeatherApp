import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


top = tk.Tk()
top.state('zoomed')  # Maximisez la fenêtre

# Chargez l'image d'arrière-plan
image_path = ".\\static\\landscape-forest-trees-mist-wallpaper-preview.jpg"  # Remplacez par votre chemin d'image
image = Image.open(image_path)

# Redimensionnez l'image pour remplir la fenêtre
window_width = top.winfo_screenwidth()
window_height = top.winfo_screenheight()
image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)

# Convertissez l'image PIL en PhotoImage utilisable par tkinter
background_image = ImageTk.PhotoImage(image)

# Créez un Label avec l'image d'arrière-plan
background_label = tk.Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

top.mainloop()