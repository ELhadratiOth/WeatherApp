import tkinter as tk
from PIL import Image, ImageTk

# Créez la fenêtre principale
top = tk.Tk()
top.state('zoomed')  # Maximisez la fenêtre

# Chargez l'image d'arrière-plan
image_path = "landscape-forest-trees-mist-wallpaper-preview.jpg"  # Remplacez par votre chemin d'image
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

# Démarrez la boucle principale de tkinter
top.mainloop()
