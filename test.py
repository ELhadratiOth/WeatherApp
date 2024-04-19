import tkinter as tk
from PIL import Image, ImageTk


def backgroundApp(root):
    # Chemin de l'image à utiliser comme arrière-plan
    image_path = "./static/bg.psd"

    # Charger l'image
    image = Image.open(image_path)

    # Définir la taille spécifiée pour la fenêtre
    specified_width = 1300
    specified_height = 700

    # Redimensionner l'image pour correspondre à la taille spécifiée
    if image.width != specified_width or image.height != specified_height:
        image = image.resize((specified_width , specified_height), Image.Resampling.LANCZOS)

    # Convertir l'image PIL en image Tkinter
    background_image = ImageTk.PhotoImage(image)

    # Créer un Label pour afficher l'image
    background_label = tk.Label(root, image=background_image)

    # Placer le label pour occuper toute la fenêtre (x=0, y=0) et l'étendre selon la largeur et hauteur relatives
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Conserver une référence à l'image pour éviter que l'image soit supprimée par le garbage collector
    root.background_image = background_image


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("1300x700")  # Définir la géométrie à respecter

    # Appeler la fonction pour configurer l'arrière-plan
    backgroundApp(root)

    # Démarrer la boucle principale de l'interface graphique
    root.mainloop()
