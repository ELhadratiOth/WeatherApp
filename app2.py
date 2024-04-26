import tkinter as tk
import ipywidgets
import seaborn
import matplotlib
import geopy
import folium
import customtkinter as ctk
from PIL import Image, ImageTk
import tkintermapview


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


if __name__ == '__main__':
    root= tk.Tk( )
    root.title("Weather App")
    root.geometry("1200x600")

    # root.resizable(height=False , width=False)
    backgroundApp(root)
    root.mainloop()

    import customtkinter
    from tkinter import Toplevel, Frame, Button, Label, OptionMenu
    from tkintermapview import TkinterMapView


    def set_marker_event(map_widget, marker_list):
        current_position = map_widget.get_position()
        marker_list.append(map_widget.set_marker(current_position[0], current_position[1]))


    def clear_marker_event(marker_list):
        for marker in marker_list:
            marker.delete()


    def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_map(new_map, map_widget):
        if new_map == "OpenStreetMap":
            map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


    def create_map_app(location):
        top_level = Toplevel()
        top_level.title("Full map")
        top_level.geometry("800x500")
        top_level.minsize(800, 500)
        top_level.grid_columnconfigure(0, weight=0)
        top_level.grid_columnconfigure(1, weight=1)
        top_level.grid_rowconfigure(0, weight=1)

        marker_list = []

        # Left frame

        frame_left = customtkinter.CTkFrame(master=top_level, width=150, corner_radius=0, fg_color=None)
        frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        frame_left.grid_rowconfigure(2, weight=1)

        button_1 = customtkinter.CTkButton(master=frame_left,
                                                text="Set Marker",
                                                command=set_marker_event)
        button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        button_2 = customtkinter.CTkButton(master=frame_left,
                                                text="Clear Markers",
                                                command=clear_marker_event)
        button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        map_label = customtkinter.CTkLabel(frame_left, text="Tile Server:", anchor="w")
        map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
        map_option_menu = customtkinter.CTkOptionMenu(frame_left, values=["OpenStreetMap", "Google normal",
                                                                                    "Google satellite"],
                                                           command=change_map)
        map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

        appearance_mode_label = customtkinter.CTkLabel(frame_left, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        appearance_mode_optionmenu = customtkinter.CTkOptionMenu(frame_left,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode)
        appearance_mode_optionmenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))

        # Right frame
        frame_right = customtkinter.CTkFrame(top_level, corner_radius=0)
        frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        frame_right.grid_rowconfigure(1, weight=1)
        frame_right.grid_rowconfigure(0, weight=0)
        frame_right.grid_columnconfigure(0, weight=1)
        frame_right.grid_columnconfigure(1, weight=0)
        frame_right.grid_columnconfigure(2, weight=1)
        map_widget = TkinterMapView(frame_right)
        map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        # Set default values
        map_widget.set_address(location)
        map_option_menu.set("OpenStreetMap")
        appearance_mode_optionmenu.set("Dark")

        top_level.mainloop()


    # Exemple d'utilisation :
    create_map_app("rabat")
