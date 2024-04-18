import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import app


def getLocation():
    if len(searchBar.get()) == 0 :
        searchBar.focus_force()
    else :
        print(searchBar.get())



root = tk.Tk()
root.title("Weather App")
root.state('zoomed')
root.resizable(height=False, width=False)
app.backgroundApp(root)


barFrame = ctk.CTkFrame(root,width=500 , height=60 , )

#search bar
searchBar = ctk.CTkEntry(root ,width=400 , height=50 ,
                         placeholder_text="Location" , font=('Poppins Medium' ,17 ) ,
                          fg_color='#344D59' , bg_color='#f2f2f2' , corner_radius=30 )
searchBar.place(x=670, y=30)

image_path = "./static/loupe.png"
button_image = ctk.CTkImage(Image.open(image_path), size=(35, 35))
buttonSearchBar = ctk.CTkButton(root, text="Confirmer", image=button_image ,
                                command=getLocation , width=50 , height=50 , compound="right"
                                ,font=('Poppins Medium' ,20 )  , anchor="se"
                                ,fg_color='#004d4d' , hover_color="#001a1a" ,bg_color='#f2f2f2', corner_radius=30
                               )
buttonSearchBar.place(y=30, x=1090)






root.mainloop()







