import tkinter as tk
from PIL import Image, ImageTk

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
