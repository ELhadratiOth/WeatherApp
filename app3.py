from tkinter import Toplevel
import app2
import customtkinter
from tkintermapview import TkinterMapView
# import cartography as ct

customtkinter.set_default_color_theme("blue")


def change_appearance_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_map(new_map: str):
    if new_map == "OpenStreetMap":
        map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
    elif new_map == "Google normal":
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    elif new_map == "Google satellite":
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

image_pa="./static/bgmap.psd"
def create_map_app(location):
    top_level = Toplevel()
    top_level.title("Full map")
    top_level.geometry("800x500")
    top_level.minsize(800, 500)
    app2.backgroundApp(top_level, 800, 500, image_pa)
    top_level.grid_columnconfigure(0, weight=0)
    top_level.grid_columnconfigure(1, weight=1)
    top_level.grid_rowconfigure(0, weight=1)

    marker_list = []

    # Left frame

    frame_left = customtkinter.CTkFrame(master=top_level, width=50,height=100, corner_radius=0, fg_color=None)
    frame_left.place(x=13,y=150)

    map_label = customtkinter.CTkLabel(frame_left, width=50,text="Tile Server:", anchor="w")
    map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
    map_option_menu = customtkinter.CTkOptionMenu(frame_left, values=["OpenStreetMap", "Google normal",
                                                                      "Google satellite"],
                                                  command=change_map)
    map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

    appearance_mode_label = customtkinter.CTkLabel(frame_left, width=50,text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
    appearance_mode_optionmenu = customtkinter.CTkOptionMenu(frame_left,
                                                             values=["Light", "Dark", "System"],
                                                             command=change_appearance_mode)
    appearance_mode_optionmenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))

    # Right frame
    frame_right = customtkinter.CTkFrame(top_level, width=570,height=435,corner_radius=0)
    frame_right.place(x=210,y=30)
    global map_widget
    map_widget = TkinterMapView(frame_right,width=570,height=435)
    map_widget.place(x=0,y=0)
    marker_1 = map_widget.set_address(location, marker=True)

    print(marker_1.position, marker_1.text)  # get position and text

    marker_1.set_text(location)  # set new text

    # Set default values
    map_widget.set_address(location)
    map_option_menu.set("OpenStreetMap")
    appearance_mode_optionmenu.set("Dark")

    return top_level
