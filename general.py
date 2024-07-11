# -*- coding: utf-8 -*-

import time
import platform
import tkinter as tk
from tkinter import filedialog
import os
import sys
import subprocess

global ROBOT_IP
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1] # Convertir en entier
else:
    ROBOT_IP = ""

print("Robot IP = ", ROBOT_IP)
def detecter_systeme():

    systeme = platform.system()
    if systeme == "Windows":
        return "windows", "\\"
    elif systeme == "Linux":
        return "linux", "/"

def python_path_detection(system, current_path):
    if system == "windows":
        python2_path = current_path + "\\lib\\windows\\Python27\\python.exe"
    elif system == "linux":
        python2_path = "/usr/bin/python2"
    return python2_path

current_path = os.getcwd()

system, delimitations = detecter_systeme()
# Define the target folder
target_folder = "nao_softwarev3"

# Iterate until the target folder is found
while os.path.basename(current_path) != target_folder:
    current_path = os.path.dirname(current_path)


python2_path = python_path_detection(system, current_path)

def creer_fenetre_reponse_degrees(reponse):
    # Créer une nouvelle fenêtre
    nouvelle_fenetre_degree = tk.Toplevel(fenetre)
    nouvelle_fenetre_degree.title("Nao")
    nouvelle_fenetre_degree.geometry("400x200")

    # Ajouter un label pour afficher les détails de la réponse
    label_details = tk.Label(nouvelle_fenetre_degree, text="De combien de degrés Nao doit  " + reponse + " ?")
    label_details.pack(padx=10, pady=10)

    curseur_degrees = tk.Scale(nouvelle_fenetre_degree, from_=0, to=180, orient=tk.HORIZONTAL, label="Degrés", length= 300)
    curseur_degrees.pack(padx=10, pady=10)
    bouton_valider = tk.Button(nouvelle_fenetre_degree, text="Valider", command=lambda: valider(reponse, curseur_degrees.get()))
    bouton_valider.pack(pady=10)


def creer_fenetre_reponse_meters(reponse):

    nouvelle_fenetre_metre = tk.Toplevel(fenetre)
    nouvelle_fenetre_metre.title("Nao")
    nouvelle_fenetre_metre.geometry("400x200")

    # Ajouter un label pour afficher les détails de la réponse
    label_details = tk.Label(nouvelle_fenetre_metre, text="De combien de mètres Nao doit  " + reponse + " ?")
    label_details.pack(padx=10, pady=10)

    curseur_meters= tk.Scale(nouvelle_fenetre_metre, from_=0, to=200, orient=tk.HORIZONTAL, label="Centimètres" ,length= 300)
    curseur_meters.pack(padx=10, pady=10)
    bouton_valider = tk.Button(nouvelle_fenetre_metre, text="Valider", command=lambda: valider(reponse, curseur_meters.get()))
    bouton_valider.pack(pady=10)

def creer_fenetre_reponse_parler(reponse):
    nouvelle_fenetre_parler = tk.Toplevel(fenetre)
    nouvelle_fenetre_parler.title("Nao")
    nouvelle_fenetre_parler.geometry("400x200")

    label_details = tk.Label(nouvelle_fenetre_parler, text="Que doit dire Nao ?")
    label_details.pack(padx=10, pady=10)

    # Ajoutez vos boutons ici
    bouton_a = tk.Button(nouvelle_fenetre_parler, text="Donner la météo", command=lambda: valider(reponse, "météo"))
    bouton_a.pack(pady=5)

    bouton_b = tk.Button(nouvelle_fenetre_parler, text="Parler de l'actualité", command=lambda: valider(reponse, "actualité"))
    bouton_b.pack(pady=5)

    bouton_c = tk.Button(nouvelle_fenetre_parler, text="Expliquer comment Nao est programmé", command=lambda: valider(reponse, "programmation"))
    bouton_c.pack(pady=5)

    bouton_d = tk.Button(nouvelle_fenetre_parler, text="Personaliser", command=lambda: valider(reponse, "personaliser"))
    bouton_d.pack(pady=5)


def creer_fenetre_reponse_autre(reponse):

    nouvelle_fenetre_autre = tk.Toplevel(fenetre)
    nouvelle_fenetre_autre.title("Nao")
    nouvelle_fenetre_autre.geometry("400x100")

    # Ajouter un label pour afficher les détails de la réponse
    label_details = tk.Label(nouvelle_fenetre_autre, text="Nao doit " + reponse + " ?")
    label_details.pack(padx=10, pady=10)

    bouton_valider = tk.Button(nouvelle_fenetre_autre, text="Valider", command=lambda: valider(reponse, 0))
    bouton_valider.pack(pady=10)


def creer_fonction_callback(choix, valeur):
    return lambda: afficher_choix(choix, valeur)

def afficher_choix(choix, valeur):
    global selected_choice
    selected_choice = choix
    print("La réponse choisie est :", selected_choice)
    print("La valeur associée est :", valeur)
    if valeur <= 1:
        creer_fenetre_reponse_meters(selected_choice)
    elif valeur == 2:
        creer_fenetre_reponse_degrees(selected_choice)
    elif valeur == 7:
        creer_fenetre_reponse_parler(selected_choice)
    else:
        creer_fenetre_reponse_autre(selected_choice)

    

def parcourir_fichier(dossier):
    fichier = filedialog.askopenfilename(initialdir=dossier)
    if fichier:
        print("Fichier sélectionné :", fichier)
        global chemin_fichier
        chemin_fichier = fichier
        fenetre.destroy()

def valider(mouvement, valeur):
    print("Mouvement choisi :", mouvement)
    print("Valeur du curseur :", valeur)
    fichier_output = current_path + delimitations + "Nao_tasks" + delimitations + "general" + delimitations+ mouvement + ".py"
    subprocess.call([python2_path,fichier_output,str(ROBOT_IP), str(valeur)])


# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("400x650")
fenetre.title("NAO")

# Créer un label pour afficher la question
question_label = tk.Label(fenetre, text="Quelles actions voulez-vous faire ?")
question_label.pack(pady=10)

# Créer des boutons avec les choix possibles
boutons_choix = [
    ("Avancer", "avancer", 0),
    ("Reculer", "reculer", 1),
    ("Tourner", "tourner", 2),
    ("Lever le bras droit", "lever_droit", 3),
    ("Lever le bras gauche", "lever_gauche", 4),
    ("Voir un obstacle", "obstacle", 5),
    ("Danser", "danser", 6),
    ("Parler", "parler", 7)
]

for texte, choix, valeur in boutons_choix:
    bouton = tk.Button(fenetre, text=texte, command=creer_fonction_callback(choix, valeur), width=20, height=3)
    bouton.pack(pady=5)


fenetre.mainloop()