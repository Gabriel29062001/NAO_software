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
    ROBOT_IP = "10.101.0.183"

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

def obtenir_fichiers_py(dossier):
    fichiers_py = [fichier for fichier in os.listdir(dossier) if fichier.endswith('.py')]
    return fichiers_py

current_path = os.getcwd()

system, delimitations = detecter_systeme()
# Define the target folder
target_folder = "nao_softwarev3"

# Iterate until the target folder is found
while os.path.basename(current_path) != target_folder:
    current_path = os.path.dirname(current_path)

python2_path = python_path_detection(system, current_path)

# Obtenir la liste des fichiers .py dans le dossier "themes"
fichiers_themes = obtenir_fichiers_py(os.path.join(current_path, "Nao_tasks", "themes"))

# Créer une liste des thèmes disponibles en enlevant l'extension .py
themes_disponibles = [theme[:-3] for theme in fichiers_themes]

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("400x150")
fenetre.title("NAO")

# Créer un label pour afficher la question
question_label = tk.Label(fenetre, text="De quel thème voulez-vous parler aujourd'hui ?")
question_label.pack(pady=10)

# Créer un menu déroulant pour sélectionner le thème
theme_var = tk.StringVar(fenetre)
theme_menu = tk.OptionMenu(fenetre, theme_var, *themes_disponibles)
theme_menu.pack(pady=10)
theme_var.set(themes_disponibles[0])  # Définir la première option par défaut

# Fonction pour valider le mouvement sélectionné
def valider(mouvement):
    print("Mouvement choisi :", mouvement)
    fichier_output = os.path.join(current_path, "Nao_tasks", "themes", mouvement + ".py")
    subprocess.call([python2_path, fichier_output, str(ROBOT_IP)])

# Bouton pour valider le choix du thème
valider_button = tk.Button(fenetre, text="Valider", command=lambda: valider(theme_var.get()))
valider_button.pack(pady=10)

fenetre.mainloop()
