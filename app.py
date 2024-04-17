import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


def load_background_image(canvas, image_path):
    # Ouvrir l'image à partir du chemin
    image = Image.open(image_path)

    # Redimensionner l'image pour correspondre à la taille du canevas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Utilisez Image.Resampling.LANCZOS pour redimensionner l'image avec une bonne qualité
    image = image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)

    # Convertir l'image PIL en une image que tkinter peut utiliser
    background_image = ImageTk.PhotoImage(image)

    # Afficher l'image comme arrière-plan dans le canevas
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    # Stocker la référence à l'image pour éviter qu'elle ne soit collectée par le garbage collector
    canvas.background_image = background_image


# Créez la fenêtre principale
root = tk.Tk()

# Maximisez la fenêtre
root.state('zoomed')

# Créez un canevas et placez-le dans la fenêtre
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Chemin de l'image d'arrière-plan
image_path = ".\\static\\landscape-forest-trees-mist-wallpaper-preview.jpg"  # Remplacez par le chemin de votre image

load_background_image(canvas, image_path)

root.mainloop()