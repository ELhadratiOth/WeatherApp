import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import app
root = tk.Tk()
root.title("Weather App")
root.state('zoomed')
root.resizable(height=False, width=False)
app.backgroundApp(root)

mainFrame = tk.Frame(root , background="#ffffff" , width=1320 , height=730)
mainFrame.place(x=115 , y=50)

#search bar
searchBar = ctk.CTkEntry(mainFrame ,width=300 , height=40 , placeholder_text="Location" , font=('Poppins Medium' ,17 ) )
searchBar.place(x=1000, y=30)





root.mainloop()







