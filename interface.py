import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import app
import time
import function



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
def ImagAdd(img , size):
    my_image = ctk.CTkImage(light_image=Image.open(img),
                                      size=(size, size))
    return my_image



root = tk.Tk()
root.title("Weather App")
root.geometry("1200x600")
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
dateLabel.place(relx=0.5, rely=0.75, anchor='center'  )
updatetimer()

dailyFrame = ctk.CTkFrame(root , width=1320 , height=260 , bg_color='#132530' , fg_color="#132530")
dailyFrame.place(x=115 , y=510 )
currentW = ctk.CTkFrame(dailyFrame , width=300 , height=250 , bg_color='#132530', fg_color="#132530"  )
currentW.place(x=10 ,y=5)
lastT , img  = function.outputCurrentT()
print(lastT , img)


my_image=ImagAdd('./static/3.png' , 100)
currentWlabel1 = ctk.CTkLabel(currentW , image=my_image, text="" , width=200 , height=200 ,compound="left"  , bg_color='#987654'  ,font=('Mountain' ,50 )  )
currentWlabel1.place(relx=0.3, rely=0.5, anchor='center')

frameTT = ctk.CTkFrame(currentW , width=100 , height= 100)
frameTT.place(relx=0.4, rely=0.26)
currentWlabel2 = ctk.CTkLabel(frameTT , text=lastT ,compound="left"  , bg_color='#700570'  ,font=('Mountain' ,50 )  )
currentWlabel2.place(relx=0.65, rely=0.35, anchor='center')

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,compound="left"  , bg_color='#707070'  ,font=('Mountain' ,20 )  )
currentWlabel3.place(relx=0.75 , rely=0.3, anchor='center')






root.mainloop()







