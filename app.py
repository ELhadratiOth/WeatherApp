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
    image_path = "./static/bg.jpeg"  # Remplacez par le chemin de votre image

    # Chargez l'image d'arrière-plan
    image = Image.open(image_path)

    # Récupérez la taille de l'écran de la fenêtre
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    # Si l'image est plus petite que l'écran, redimensionnez-la
    # Sinon, utilisez l'image d'origine
    if image.width != screen_width or image.height != screen_height:
        # Utilisez Image.Resampling.LANCZOS pour le redimensionnement de haute qualité
        image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

    # Convertissez l'image PIL en PhotoImage utilisable par tkinter
    background_image = ImageTk.PhotoImage(image)

    # Créez un Label avec l'image d'arrière-plan et placez-le dans la fenêtre
    background_label = tk.Label(top, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Assurez-vous que l'image d'arrière-plan reste accessible après la fonction
    top.background_image = background_image
def frameApp(top):
    # appFrame = tk.Frame(top,bg="#988C89" , width=1200 , height=1000)
    #
    # appFrame.place(x=150, y=100)

    pass
# Créez la fenêtre principale
top = tk.Tk()
top.state('zoomed')  # Maximisez la fenêtre

backgroundApp(top)
frameApp(top)




# Exécutez la boucle principale
top.mainloop()
