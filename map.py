import customtkinter
from tkintermapview import TkinterMapView
# import cartography as ct

customtkinter.set_default_color_theme("blue")


def create_map_app(location):
    class App(customtkinter.CTk):

        APP_NAME = "Full map"
        WIDTH = 800
        HEIGHT = 500

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.title(App.APP_NAME)
            self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
            self.minsize(App.WIDTH, App.HEIGHT)

            self.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

            self.marker_list = []

            # ============ create two CTkFrames ============

            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
            self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

            self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
            self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

            # ============ frame_left ============

            self.frame_left.grid_rowconfigure(2, weight=1)

            self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Set Marker",
                                                    command=self.set_marker_event)
            self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

            self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                    text="Clear Markers",
                                                    command=self.clear_marker_event)
            self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

            self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
            self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
            self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                           command=self.change_map)
            self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

            self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                           command=self.change_appearance_mode)
            self.appearance_mode_optionemenu.grid(row=6, column=0, padx=(20, 20), pady=(10, 20))

            # ============ frame_right ============

            self.frame_right.grid_rowconfigure(1, weight=1)
            self.frame_right.grid_rowconfigure(0, weight=0)
            self.frame_right.grid_columnconfigure(0, weight=1)
            self.frame_right.grid_columnconfigure(1, weight=0)
            self.frame_right.grid_columnconfigure(2, weight=1)

            self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
            self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

            # Set default values
            self.map_widget.set_address(location)
            self.map_option_menu.set("OpenStreetMap")
            self.appearance_mode_optionemenu.set("Dark")

        def set_marker_event(self):
            current_position = self.map_widget.get_position()
            self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

        def clear_marker_event(self):
            for marker in self.marker_list:
                marker.delete()

        def change_appearance_mode(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)

        def change_map(self, new_map: str):
            if new_map == "OpenStreetMap":
                self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
            elif new_map == "Google normal":
                self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            elif new_map == "Google satellite":
                self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        def on_closing(self, event=0):
            self.destroy()

        def start(self):
            self.mainloop()

    app = App()
    app.start()

create_map_app('rabat')