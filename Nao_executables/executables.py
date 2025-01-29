# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import filedialog
import os
import subprocess



def detecter_systeme():

    systeme = platform.system()
    if systeme == "Windows":
        return "windows", "\\"
    elif systeme == "Linux":
        return "linux", "/"

system, delimitations = detecter_systeme()
current_path = os.getcwd()

# Define the target folder
target_folder = "nao_softwarev3"

# Iterate until the target folder is found
while os.path.basename(current_path) != target_folder:
    current_path = os.path.dirname(current_path)

selected_choice = None
selected_choice_tasks = None


def afficher_choix():
    global selected_choice
    selected_choice = curseur.get()
    print("La réponse choisie est : " + selected_choice)
    fenetre.destroy()

def afficher_choix_tasks():
    global selected_choice_tasks
    selected_choice_tasks = curseur.get()
    print("La réponse choisie est : " + selected_choice_tasks)
    fenetre_tasks.destroy()


# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("400x250")
fenetre.title("NAO")

# Créer un label pour afficher la question
question_label = tk.Label(fenetre, text="Dans quels structure êtes vous ?")
question_label.pack(pady=10)

# Créer un curseur (Radiobutton) avec les choix possibles
curseur = tk.StringVar()

choix_a = tk.Radiobutton(fenetre, text="Nanosphère", variable=curseur, value=0)
choix_b = tk.Radiobutton(fenetre, text="Petits Acrobates", variable=curseur, value=1)
choix_c = tk.Radiobutton(fenetre, text="Les 6 sens", variable=curseur, value=2)
choix_d = tk.Radiobutton(fenetre, text="Le Microcosme", variable=curseur, value=3)
choix_e = tk.Radiobutton(fenetre, text="Vivalys", variable=curseur, value=4)
choix_f = tk.Radiobutton(fenetre, text="Home", variable=curseur, value=5)
choix_g = tk.Radiobutton(fenetre, text="Défi des 10", variable=curseur, value=6)


choix_a.pack()
choix_b.pack()
choix_c.pack()
choix_d.pack()
choix_e.pack()
choix_f.pack()
choix_g.pack()

# Créer un bouton pour afficher le choix
bouton_afficher = tk.Button(fenetre, text="Sélectionner réponse", command=afficher_choix)
bouton_afficher.pack(pady=10)


creches = ["La_Nanosphère","Les_Petits_Acrobates", "Les_6_sens", "Le_Microcosme", "Vivalys", "HOME", "Rachel"]
creches_ROBOT_IP = ['172.24.24.150', "192.168.55.60","192.168.1.69", "192.168.51.159",  "172.16.40.105", "10.101.0.186", "172.20.10.5"]

# Boucle principale
fenetre.mainloop()
print(creches[int(selected_choice)])

if (int(selected_choice))==6:
    fichier_output = "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/defi_10/defi_10.py"
    print(fichier_output)
    subprocess.call(["python2",fichier_output, str(creches_ROBOT_IP[int(selected_choice)])])
    exit()

# Créer une fenêtre
fenetre_tasks = tk.Tk()
fenetre_tasks.geometry("400x200")
fenetre_tasks.title("NAO")

# Créer un label pour afficher la question
question_label = tk.Label(fenetre_tasks, text="Quels type de tache doit-il effectuer ?")
question_label.pack(pady=10)


# Créer un curseur (Radiobutton) avec les choix possibles
curseur = tk.StringVar()

choix_a = tk.Radiobutton(fenetre_tasks, text="General Tasks", variable=curseur, value="general")
choix_b = tk.Radiobutton(fenetre_tasks, text="Thèmes crèches", variable=curseur, value="themes")
choix_c = tk.Radiobutton(fenetre_tasks, text="Tests", variable=curseur, value="tests")
choix_d = tk.Radiobutton(fenetre_tasks, text="Changer le Volume", variable=curseur, value="volume")


choix_a.pack()
choix_b.pack()
choix_c.pack()
choix_d.pack()

# Créer un bouton pour afficher le choix
bouton_afficher = tk.Button(fenetre_tasks, text="Sélectionner réponse", command=afficher_choix_tasks)
bouton_afficher.pack(pady=10)


fenetre_tasks.mainloop()

if selected_choice_tasks =="volume":

    fenetre_vol = tk.Tk()
    fenetre_vol.geometry("400x200")
    fenetre_vol.title("Volume de NAO")

    volume_value = tk.IntVar()

    # Fonction pour mettre à jour l'affichage du pourcentage
    def update_percentage(val):
        volume_label.config(text=f"Volume : {volume_value.get()} %")

    def valider_volume():
        print(f"Le volume sélectionné est : {volume_value.get()} %")
        global volume
        volume = volume_value.get()
        print(volume)
        fichier_output = "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/volume/volume.py"
        subprocess.call(["python2",fichier_output, str(creches_ROBOT_IP[int(selected_choice)]), str(volume)])

    curseur_volume = tk.Scale(fenetre_vol, from_=0, to=100, orient="horizontal", variable=volume_value, command=update_percentage)
    curseur_volume.pack(pady=10)

    volume_label = tk.Label(fenetre_vol, text="Volume : 0 %")
    volume_label.pack(pady=10)
    
    bouton_valider = tk.Button(fenetre_vol, text="Valider", command=valider_volume)
    bouton_valider.pack(pady=10)
    
    fenetre_vol.mainloop()



    
else :
    fichier_output = current_path + delimitations + "Nao_tasks" + delimitations + selected_choice_tasks + delimitations + selected_choice_tasks + ".py"
    print(fichier_output)
    subprocess.call(["python3",fichier_output, str(creches_ROBOT_IP[int(selected_choice)])])