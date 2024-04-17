import tkinter as tk

def create_transparent_frame():
    # Créez une fenêtre principale (root)
    root = tk.Tk()
    root.title("Frame Transparent")

    # Définissez la couleur de fond de la fenêtre principale (par exemple, blanc)
    root.config(bg='white')

    # Créez un frame (cadre) et placez-le dans la fenêtre principale
    frame = tk.Frame(root)

    # Définissez la couleur de fond du frame pour correspondre à celle de la fenêtre principale
    # Cela donnera l'illusion de transparence
    frame.config(bg=root.cget('bg'))

    # Ajoutez des widgets au frame (par exemple, un label)
    label = tk.Label(frame, text="Frame transparent", bg="white", fg="black")
    label.pack(padx=20, pady=20)

    # Placez le frame dans la fenêtre principale
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    # Exécutez la boucle principale
    root.mainloop()

# Appeler la fonction pour créer un frame transparent
create_transparent_frame()
