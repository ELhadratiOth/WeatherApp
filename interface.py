import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import app
import time
import function
from tkinter import messagebox
from geopy import Nominatim

airPdetail, aqiVal, typelabel, massagelabel, elem11, elem12, elem13, elem14, elem15, elem16  , city  = ("",) * 11


def getLocation():
    if len(searchBar.get()) == 0 :
        messagebox.showerror(title='No city Typed', message="try to type the name of a city ")
        searchBar.focus_force() 
    else :
        print(searchBar.get())
        geocoder = Nominatim(user_agent="weather_app")
        location = geocoder.geocode(searchBar.get())
        global  AirData , city 
        if location:
            latitude = location.latitude
            longitude = location.longitude
            lastT, img = function.outputCurrentT(latitude, longitude)
            dataDic = function.setImg(latitude, longitude)

            AirData = function.AirDetails(latitude, longitude)

            villeLabel.configure(text=searchBar.get())
            paysLabel.configure(text="not found")
            my_image = ImagAdd(img, 100)
            currentWlabel11.configure(image=my_image)
            currentWlabel21.configure(text=lastT)
            my_image = ImagAdd(dataDic['img'][0], 60)
            elem1.configure(image=my_image)
            currentWlabel22.configure(text=dataDic['tmp'][0])
            currentWlabel42.configure(text=dataDic['time'][0].split('T')[1])
            my_image = ImagAdd(dataDic['img'][1], 60)
            elem2.configure(image=my_image)
            currentWlabel23.configure(text=dataDic['tmp'][1])
            currentWlabel43.configure(text=dataDic['time'][1].split('T')[1])
            my_image = ImagAdd(dataDic['img'][2], 60)
            elem3.configure(image=my_image)
            currentWlabel24.configure(text=dataDic['tmp'][2])
            currentWlabel44.configure(text=dataDic['time'][2].split('T')[1])
            my_image = ImagAdd(dataDic['img'][3], 60)
            elem4.configure(image=my_image)
            currentWlabel25.configure(text=dataDic['tmp'][3])
            currentWlabel45.configure(text=dataDic['time'][3].split('T')[1])
            my_image = ImagAdd(dataDic['img'][4], 60)
            elem5.configure(image=my_image)
            currentWlabel26.configure(text=dataDic['tmp'][4])
            currentWlabel46.configure(text=dataDic['time'][4].split('T')[1])
            my_image = ImagAdd(dataDic['img'][5], 60)
            elem6.configure(image=my_image)
            currentWlabel27.configure(text=dataDic['tmp'][5])
            currentWlabel47.configure(text=dataDic['time'][5].split('T')[1])
            aqiButtun.configure(text="AQI " + str(AirData[0]))
            city = searchBar.get()
            try  :
                if toplevel_window.winfo_exists() :

                    airPdetail.configure(text=searchBar.get() + ' Published at ' + AirData[9])
                    aqiVal.configure(text=AirData[0], text_color=AirData[11])
                    typelabel.configure(text=AirData[7], text_color=AirData[11])
                    massagelabel.configure(text=AirData[8])
                    elem11.configure(text=AirData[2])
                    elem12.configure(text=AirData[1])
                    elem13.configure(text=AirData[5])
                    elem14.configure(text=AirData[4])
                    elem15.configure(text=AirData[6])
                    elem16.configure(text=AirData[3])
            except AttributeError :
                pass

        else:
            messagebox.showerror (   title='City Not Found'   , message="try to type an existing city")



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
def create_toplevel_window():
    global airPdetail , aqiVal , typelabel , massagelabel , elem11 , elem12 , elem13 , elem14 , elem15 , elem16
    toplevel_window = tk.Toplevel()
    toplevel_window.geometry("400x300")
    toplevel_window.resizable(height=False, width=False)
    app.backgroundApp(toplevel_window, 400, 300 , './static/bgwindow.psd')
    frameTop = ctk.CTkFrame(toplevel_window, width=340, height=240, bg_color='#091c25', fg_color='#091c25',
                            corner_radius=30)
    frameTop.place(x=30, y=27)
    airQ = ctk.CTkLabel(frameTop, width=100, height=15, text='Air Quality Index', font=('Davish Medium', 35))
    airQ.place(x=10, y=0)
    airPdetail = ctk.CTkLabel(frameTop, width=100, height=15, text= city+ 'Published at '+ AirData[9],
                              font=('Davish Medium', 20))
    airPdetail.place(x=10, y=43)
    aqiVal = ctk.CTkLabel(frameTop, width=100, height=15, text=AirData[0], font=('Davish Medium', 65), text_color=AirData[11])
    aqiVal.place(x=-12, y=70)
    typelabel = ctk.CTkLabel(frameTop, height=15, text=AirData[7], font=('Davish Medium', 25), text_color=AirData[11])
    typelabel.place(x=70, y=102)
    massagelabel = ctk.CTkLabel(frameTop, height=15, text=AirData[8],
                                font=('Davish Medium', 15))
    massagelabel.place(x=10, y=142)
    # block1
    framBolock1 = ctk.CTkFrame(frameTop, width=50, height=50 , bg_color='#091c25' ,  fg_color='#091c25')
    framBolock1.place(x=1, y=180)
    elem11 = ctk.CTkLabel(framBolock1, text=AirData[2], font=('Davish Medium', 20), text_color=AirData[11])
    elem11.place(x=10, y=0)
    elem21 = ctk.CTkLabel(framBolock1, text="PM2.5", font=('Davish Medium', 15))
    elem21.place(x=10, y=21)
    # block2
    framBolock2 = ctk.CTkFrame(frameTop, width=50, height=50 , bg_color='#091c25' ,  fg_color='#091c25')
    framBolock2.place(x=59, y=180)
    elem12 = ctk.CTkLabel(framBolock2, text=AirData[1], font=('Davish Medium', 20), text_color=AirData[11])
    elem12.place(x=10, y=0)
    elem22 = ctk.CTkLabel(framBolock2, text="PM10", font=('Davish Medium', 15))
    elem22.place(x=12, y=21)
    # block3
    framBolock3 = ctk.CTkFrame(frameTop, width=50, height=50 , bg_color='#091c25' ,  fg_color='#091c25')
    framBolock3.place(x=117, y=180)
    elem13 = ctk.CTkLabel(framBolock3, text=AirData[5], font=('Davish Medium', 20), text_color=AirData[11])
    elem13.place(x=15, y=0)
    elem23 = ctk.CTkLabel(framBolock3, text="SO₂", font=('Davish Medium', 15))
    elem23.place(x=17, y=21)
    # block4
    framBolock4 = ctk.CTkFrame(frameTop, width=50, height=50 , bg_color='#091c25' ,  fg_color='#091c25')
    framBolock4.place(x=176, y=180)
    elem14 = ctk.CTkLabel(framBolock4, text=AirData[4], font=('Davish Medium', 20), text_color=AirData[11])
    elem14.place(x=10, y=0)
    elem24 = ctk.CTkLabel(framBolock4, text="NO₂", font=('Davish Medium', 15))
    elem24.place(x=17, y=21)
    # block5
    framBolock5 = ctk.CTkFrame(frameTop, width=50, height=50,bg_color='#091c25' ,  fg_color='#091c25')
    framBolock5.place(x=234, y=180)
    elem15 = ctk.CTkLabel(framBolock5, text=AirData[6], font=('Davish Medium', 20), text_color=AirData[11])
    elem15.place(x=10, y=0)
    elem25 = ctk.CTkLabel(framBolock5, text="O₃", font=('Davish Medium', 15))
    elem25.place(x=20, y=21)
    # block6
    framBolock6 = ctk.CTkFrame(frameTop, width=50, height=50 , bg_color='#091c25' , fg_color='#091c25')
    framBolock6.place(x=290, y=180)
    elem16 = ctk.CTkLabel(framBolock6, text=AirData[3], font=('Davish Medium', 20), text_color=AirData[11])
    elem16.place(x=10, y=0)
    elem26 = ctk.CTkLabel(framBolock6, text="CO", font=('Davish Medium', 15))
    elem26.place(x=19, y=21)

    return toplevel_window

def open_toplevel():
    # Function to open the Toplevel window
    global toplevel_window
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = create_toplevel_window()  # Create the window if it's None or destroyed
    else:
        toplevel_window.focus()

latitude, longitude , region , city = function.actuall_dataCompli()
lastT , img  = function.outputCurrentT(latitude, longitude)
dataDic=function.setImg(latitude, longitude)
AirData=function.AirDetails(latitude, longitude)

toplevel_window = None
root = tk.Tk()
root.title("Weather App")
root.geometry("1300x700")
root.resizable(height=False, width=False)
app.backgroundApp(root,1300 , 700,'./static/bg.psd')



barFrame = ctk.CTkFrame(root,width=500 , height=60  )

#search bar
searchBar = ctk.CTkEntry(root ,width=350 , height=45 ,
                         placeholder_text="Location" , font=('Mountain' ,17 ) ,
                          fg_color='#344D59' , bg_color='#132530' , corner_radius=30 )
searchBar.place(x=630, y=76 )

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
currentWlabel11 = ctk.CTkLabel(currentW , image=my_image, text="" , width=120 , height=150   , bg_color='#263138'  ,font=('Mountain' ,50 )  )
currentWlabel11.place(relx=0.07, rely=0.02)

frameTT = ctk.CTkFrame(currentW , width=104 , height= 52 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.55, rely=0.16)
currentWlabel21 = ctk.CTkLabel(frameTT , text=lastT ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,45 ) )
currentWlabel21.place(relx=0.26, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,20 )  )
currentWlabel3.place(relx=0.7 , rely=0.1)

currentWlabel4 = ctk.CTkLabel(currentW , text="NOW" ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,45 ) )
currentWlabel4.place(relx=0.27, rely=0.6)

#other TMPS
container = ctk.CTkFrame(root , width=848 , height=215 , bg_color='#132530', fg_color="#263138" ,   corner_radius=30 )
container.place(x=370 , y=426)

#setting elems
#elem1
my_image=ImagAdd(dataDic['img'][0] , 60)
elem1 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138')
elem1.place(x=15,y=36)
frameTT = ctk.CTkFrame(elem1 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel22 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][0] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel22.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel42 = ctk.CTkLabel(elem1 , text=dataDic['time'][0].split('T')[1] ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel42.place(relx=0.3 , rely=0.75)

#elem2
my_image=ImagAdd(dataDic['img'][1] , 60)
elem2 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138')
elem2.place(x=155,y=36)
frameTT = ctk.CTkFrame(elem2 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel23 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][1] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel23.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel43 = ctk.CTkLabel(elem2 , text=dataDic['time'][1].split('T')[1] ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel43.place(relx=0.3 , rely=0.75)
#elem3
my_image=ImagAdd(dataDic['img'][2] , 60)
elem3 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138' )
elem3.place(x=295,y=36)
frameTT = ctk.CTkFrame(elem3 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel24 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][2] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel24.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel44 = ctk.CTkLabel(elem3 , text=dataDic['time'][2].split('T')[1],height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel44.place(relx=0.3 , rely=0.75)

#elem4
my_image=ImagAdd(dataDic['img'][3] , 60)
elem4 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138')
elem4.place(x=435,y=36)
frameTT = ctk.CTkFrame(elem4 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel25 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][3] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel25.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel45 = ctk.CTkLabel(elem4 , text=dataDic['time'][3].split('T')[1] ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel45.place(relx=0.3 , rely=0.75)

#elem5
my_image=ImagAdd(dataDic['img'][4] , 60)
elem5 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138')
elem5.place(x=575,y=36)
frameTT = ctk.CTkFrame(elem5 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel26 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][4] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel26.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel46 = ctk.CTkLabel(elem5 , text=dataDic['time'][4].split('T')[1] ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel46.place(relx=0.3 , rely=0.75)
#elem6
my_image=ImagAdd(dataDic['img'][5] , 60)
elem6 = ctk.CTkLabel(container , image=my_image, text="",width=120 , height=170 , bg_color='#263138')
elem6.place(x=715,y=36)
frameTT = ctk.CTkFrame(elem6 , width=84 , height= 36 , border_width=3 , border_color="#000000" ,   corner_radius=30 , fg_color='#06151e'  )
frameTT.place(relx=0.15 , rely=0.08)
currentWlabel27 = ctk.CTkLabel(frameTT , text=dataDic['tmp'][5] ,height=30  , bg_color='#06151e'
                              ,font=('Mountain' ,30 ) )
currentWlabel27.place(relx=0.2, rely=0.058)

currentWlabel3 = ctk.CTkLabel(frameTT , text="o"  ,height=1  , bg_color='#06151e'  ,font=('Mountain' ,15 )  )
currentWlabel3.place(relx=0.8 , rely=0.1)
currentWlabel47 = ctk.CTkLabel(elem6 , text=dataDic['time'][5].split('T')[1] ,height=30  , bg_color='#263138'
                              ,font=('Mountain' ,35 ) )
currentWlabel47.place(relx=0.3 , rely=0.75)


buttonChangePage  = ctk.CTkButton(root , text="24-hour forecast" , bg_color='#263138' , fg_color='#06151e' ,
                                  border_width=2 , corner_radius=10 , border_color='#000000',
                                  width=120 , height=35  , font=('Mountain' ,25 ))
buttonChangePage.place(x=390  , y=430)
my_image    =  ImagAdd("./static/air-quality.png", 24)
aqiButtun = ctk.CTkButton(currentW , image= my_image ,text="AQI "+ str(AirData[0]) , bg_color='#263138' , fg_color='#16191c'
                                ,border_width=2 , corner_radius=10 , border_color='#000000',
                                  width=100 , height=34  , font=('Mountain' ,25 ) , command=open_toplevel ,  compound="left")
aqiButtun.place(x=137 , y=170)



root.mainloop()







