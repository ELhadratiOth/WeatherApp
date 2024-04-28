import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ipywidgets import interact, widgets


def plot_graph(species):
    # Charger les données
    data = sns.load_dataset("iris")
    data_filtered = data[data['species'] == species]

    # Créer le graphique
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x="species", y="sepal_length", data=data_filtered, ax=ax)
    fig.patch.set_facecolor(root.cget('bg'))  # Définir la couleur de fond transparente

    # Afficher le graphique dans la fenêtre Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Créer la fenêtre principale
root = tk.Tk()
root.title("Seaborn & Tkinter Example")
root.geometry("800x600")  # Dimensions de la fenêtre
root.config(bg="#001F3F")  # Couleur de fond bleu marine

# Ajouter un widget interactif IPywidgets
species_options = ['setosa', 'versicolor', 'virginica']
interact(plot_graph, species=widgets.Dropdown(options=species_options, value='setosa'))

# Démarrer la boucle principale de Tkinter
root.mainloop()
