from tkinter import *
import tkintermapview
import tkinter as tk



root=tk.Tk()
root.title('My map')
#root.iconbitmap()
icon_path = "./static/loupe.png"
icon_image = tk.PhotoImage(file=icon_path)

root.iconphoto(True, icon_image)
root.geometry('900x700')
my_label=LabelFrame(root)
my_label.pack(pady=20)
my_widget=tkintermapview.TkinterMapView(my_label,width=800,height=600,corner_radius=0)
my_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#set cordinates
#my_widget.set_position(12.7,-5.67)
# set current widget position by address
marker_1 = my_widget.set_address("colosseo, rome, italy", marker=True)

print(marker_1.position, marker_1.text)  # get position and text

marker_1.set_text("Colosseo in Rome")  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()
my_widget.set_zoom(15)
my_widget.pack()




root.mainloop()