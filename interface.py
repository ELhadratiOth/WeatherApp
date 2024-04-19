import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import app
import time



def getLocation():
    if len(searchBar.get()) == 0 :
        searchBar.focus_force()
    else :
        print(searchBar.get())

def updatetimer():
    exactTime = time.strftime("%I.%M.%S %p")
    clockLabel.configure(text=exactTime)
    exactDate= time.strftime("%A . %B . %d , %Y")
    dateLabel.configure(text=exactDate)
    root.after(1000,updatetimer)

root = tk.Tk()
root.title("Weather App")
root.state('zoomed')
root.resizable(height=False, width=False)
app.backgroundApp(root)



barFrame = ctk.CTkFrame(root,width=500 , height=60  )

#search bar
searchBar = ctk.CTkEntry(root ,width=400 , height=50 ,
                         placeholder_text="Location" , font=('Mountain' ,17 ) ,
                          fg_color='#344D59' , bg_color='#132530' , corner_radius=30 )
searchBar.place(x=738, y=86)

image_path = "./static/loupe.png"
button_image = ctk.CTkImage(Image.open(image_path), size=(35, 35))
buttonSearchBar = ctk.CTkButton(root, text="Confirmer", image=button_image ,
                                command=getLocation , width=50 , height=50 , compound="right"
                                ,font=('Mountain' ,20 )  , anchor="se"
                                ,fg_color='#004d4d' , hover_color="#001a1a" ,bg_color='#132530', corner_radius=30
                               )
buttonSearchBar.place(y=86, x=1168)

#data city

villeFrame = ctk.CTkFrame(root ,  fg_color='#132530' ,  height=100  ,bg_color='#132530' )
villeFrame.place(x=1188 ,y =235 )



villeLabel  = ctk.CTkLabel(villeFrame , font=('Mountain' ,40 ) , text="vile" , fg_color='transparent',justify='right')
villeLabel.place(relx=0.93, rely=0.35, anchor='e')
paysLabel  = ctk.CTkLabel(villeFrame , font=('Mountain' ,20 ) , text="Pays" , fg_color='transparent' , justify='right')
paysLabel.place(relx=0.93, rely=0.75, anchor='e')

#date time

clockFrame = ctk.CTkFrame(root , width=500 , height=170 , fg_color="#132530" , bg_color='#132530')
clockFrame.place(x=150 , y = 180)
clockLabel = ctk.CTkLabel(clockFrame ,text="", font=('Mountain'  ,66 ) )
clockLabel.place(relx=0.5, rely=0.3, anchor='center')

dateLabel = ctk.CTkLabel(clockFrame,text="",  font=('Mountain' ,55 ) )
dateLabel.place(relx=0.5, rely=0.75, anchor='center' )
updatetimer()




root.mainloop()







