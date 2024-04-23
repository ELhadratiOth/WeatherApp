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

latitude, longitude , region , city = function.actuall_dataCompli()
lastT , img  = function.outputCurrentT(latitude, longitude)
dataDic=function.setImg(latitude, longitude)

root = tk.Tk()
root.title("Weather App")
root.geometry("1300x700")
root.resizable(height=False, width=False)
app.backgroundApp(root)



barFrame = ctk.CTkFrame(root,width=500 , height=60  )

#search bar
searchBar = ctk.CTkEntry(root ,width=350 , height=45 ,
                         placeholder_text="Location" , font=('Mountain' ,17 ) ,
                          fg_color='#344D59' , bg_color='#132530' , corner_radius=30 )
searchBar.place(x=630, y=76)

image_path = "./static/loupe.png"
button_image = ImagAdd(image_path , 35)
buttonSearchBar = ctk.CTkButton(root, text="Confirmer", image=button_image ,
                                command=getLocation , width=30 , height=45 , compound="right"
                                ,font=('Mountain' ,25 )  , anchor="se"
                                ,fg_color='#004d4d' , hover_color="#001a1a" ,bg_color='#132530', corner_radius=30
                               )
buttonSearchBar.place(y=76, x=994)

#data city

villeFrame = ctk.CTkFrame(root ,  fg_color='#132530' ,  height=80 , width=130 ,bg_color='#132530' )
villeFrame.place(x=1045 ,y =197 )
villeLabel  = ctk.CTkLabel(villeFrame , font=('Mountain' ,40 ) , text=city , fg_color='transparent',justify='right')
villeLabel.place(relx=0.93, rely=0.35, anchor='e')
paysLabel  = ctk.CTkLabel(villeFrame , font=('Mountain' ,20 ) , text=region , fg_color='transparent' , justify='right')
paysLabel.place(relx=0.93, rely=0.75, anchor='e')

#date time

clockFrame = ctk.CTkFrame(root , width=420 , height=150 , fg_color="#132530" , bg_color='#132530')
clockFrame.place(x=130 , y = 144)
clockLabel = ctk.CTkLabel(clockFrame ,text="", font=('Mountain'  ,56 ) )
clockLabel.place(relx=0.5, rely=0.3, anchor='center')

dateLabel = ctk.CTkLabel(clockFrame,text="",  font=('Mountain' ,45 ) )
dateLabel.place(relx=0.5, rely=0.75, anchor='center'  )
updatetimer()

#currentW

currentW = ctk.CTkFrame(root , width=250 , height=215 , bg_color='#132530', fg_color="#263138" ,   corner_radius=30   )
currentW.place(x=100 ,y=426)



my_image=ImagAdd(img , 100)
currentWlabel1 = ctk.CTkLabel(currentW , image=my_image, text="" , width=120 , height=150   , bg_color='#263138'  ,font=('Mountain' ,50 )  )
currentWlabel1.place(relx=0.07, rely=0.02)

frameTT = ctk.CTkFrame(currentW , width=104 , height= 52 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.55, rely=0.16)
currentWlabel2 = ctk.CTkLabel(frameTT , text=lastT ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,45 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,20 )  )
currentWlabel3.place(relx=0.7 , rely=0.1)

currentWlabel4 = ctk.CTkLabel(currentW , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,45 ) )
currentWlabel4.place(relx=0.2, rely=0.63)

#other TMPS
container = ctk.CTkFrame(root , width=848 , height=215 , bg_color='#132530', fg_color="#263138" ,   corner_radius=30 )
container.place(x=370 , y=426)

#setting elems
#elem1
my_image=ImagAdd(dataDic['img'][0] , 60)
elem1 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem1.place(x=15,y=6)
frameTT = ctk.CTkFrame(elem1 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][0] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem1 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)

#elem2
my_image=ImagAdd(dataDic['img'][1] , 60)
elem2 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem2.place(x=155,y=6)
frameTT = ctk.CTkFrame(elem2 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][1] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem2 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)
#elem3
my_image=ImagAdd(dataDic['img'][2] , 60)
elem3 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem3.place(x=295,y=6)
frameTT = ctk.CTkFrame(elem3 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][2] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem3 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)

#elem4
my_image=ImagAdd(dataDic['img'][3] , 60)
elem4 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem4.place(x=435,y=6)
frameTT = ctk.CTkFrame(elem4 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][3] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem4 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)

#elem5
my_image=ImagAdd(dataDic['img'][4] , 60)
elem5 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem5.place(x=575,y=6)
frameTT = ctk.CTkFrame(elem5 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][4] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem5 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)
#elem6
my_image=ImagAdd(dataDic['img'][5] , 60)
elem6 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=200 , bg_color='#343234')
elem6.place(x=715,y=6)
frameTT = ctk.CTkFrame(elem6 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.10)
currentWlabel2 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][5] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel2.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel4 = ctk.CTkLabel(elem6 , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel4.place(relx=0.3 , rely=0.75)





root.mainloop()







