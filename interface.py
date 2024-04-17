import tkinter as tk
from PIL import Image, ImageTk
import app
top = tk.Tk()
top.title("Weather App")
top.state('zoomed')
top.resizable(height=False, width=False)
app.backgroundApp(top)

mainFrame = tk.Frame(top)





top.mainloop()







