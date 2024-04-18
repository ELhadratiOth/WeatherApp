import customtkinter as ctk

def main():
    # Create a CTk root window
    root = ctk.CTk()
    root.title("Transparent Frame Example")

    # Set the root window size to 400x400
    root.geometry("400x400")

    # Create a parent frame with a custom background color (e.g., light gray)
    parent_frame = ctk.CTkFrame(root, bg_color="light gray")
    parent_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Create a child frame with the same background color as the parent frame
    # to achieve a transparent effect
    child_frame = ctk.CTkFrame(parent_frame, fg_color="light gray", bg_color="light gray")
    child_frame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

    # Add a label inside the child frame
    label = ctk.CTkLabel(child_frame, text="Transparent Frame", fg_color="light gray", bg_color="light gray")
    label.pack(pady=20)

    # Add a button inside the child frame
    button = ctk.CTkButton(child_frame, text="Click Me")
    button.pack(pady=20)

    # Start the CTk application
    root.mainloop()

if __name__ == "__main__":
    main()
