# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import filedialog
import os
import subprocess


class NaoLauncher:
    def __init__(self):
        """Initialisation de l'application NAO"""
        self.system, self.delimitations = self.detecter_systeme()
        self.current_path = self.trouver_dossier_nao()
        
        self.creches = ["La_Nanosphère", "Les_Petits_Acrobates", "Les_6_sens", "Le_Microcosme", "Vivalys", "HOME", "Rachel"]
        self.creches_ROBOT_IP = ['172.24.24.150', "192.168.55.60", "192.168.1.69", "192.168.51.159", "172.16.40.105", "10.101.0.186", "172.20.10.5"]

        self.selected_choice = None
        self.selected_choice_tasks = None
        self.volume = None

        self.demander_structure()

    @staticmethod
    def detecter_systeme():
        """Détecte le système d'exploitation et retourne le bon séparateur de fichiers."""
        systeme = platform.system()
        return ("windows", "\\") if systeme == "Windows" else ("linux", "/")

    def trouver_dossier_nao(self):
        """Trouve le répertoire racine du projet NAO."""
        current_path = os.getcwd()
        target_folder = "nao_softwarev3"

        while os.path.basename(current_path) != target_folder:
            current_path = os.path.dirname(current_path)

        return current_path

    def demander_structure(self):
        """Affiche une fenêtre pour sélectionner la crèche."""
        self.fenetre = tk.Tk()
        self.fenetre.geometry("400x250")
        self.fenetre.title("NAO")

        question_label = tk.Label(self.fenetre, text="Dans quelle structure êtes-vous ?")
        question_label.pack(pady=10)

        self.curseur = tk.StringVar()
        for i, creche in enumerate(self.creches):
            tk.Radiobutton(self.fenetre, text=creche, variable=self.curseur, value=i).pack()

        bouton_afficher = tk.Button(self.fenetre, text="Sélectionner réponse", command=self.afficher_choix)
        bouton_afficher.pack(pady=10)

        self.fenetre.mainloop()

    def afficher_choix(self):
        """Récupère le choix de la crèche et exécute le script correspondant si besoin."""
        self.selected_choice = int(self.curseur.get())
        print(f"Structure sélectionnée : {self.creches[self.selected_choice]}")
        self.fenetre.destroy()

        if self.selected_choice == 6:  # Cas spécifique pour "Défi des 10"
            fichier_output = "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/defi_10/defi_10.py"
            print(fichier_output)
            subprocess.call(["python2", fichier_output, str(self.creches_ROBOT_IP[self.selected_choice])])
            exit()

        self.demander_type_tache()

    def demander_type_tache(self):
        """Affiche une fenêtre pour sélectionner le type de tâche de NAO."""
        self.fenetre_tasks = tk.Tk()
        self.fenetre_tasks.geometry("400x200")
        self.fenetre_tasks.title("NAO")

        question_label = tk.Label(self.fenetre_tasks, text="Quel type de tâche doit-il effectuer ?")
        question_label.pack(pady=10)

        self.curseur_tasks = tk.StringVar()
        choix_taches = [("General Tasks", "general"), ("Thèmes crèches", "themes"), ("Tests", "tests"), ("Changer le Volume", "volume")]

        for texte, valeur in choix_taches:
            tk.Radiobutton(self.fenetre_tasks, text=texte, variable=self.curseur_tasks, value=valeur).pack()

        bouton_afficher = tk.Button(self.fenetre_tasks, text="Sélectionner réponse", command=self.afficher_choix_tasks)
        bouton_afficher.pack(pady=10)

        self.fenetre_tasks.mainloop()

    def afficher_choix_tasks(self):
        """Récupère le choix de la tâche et exécute l'action correspondante."""
        self.selected_choice_tasks = self.curseur_tasks.get()
        print(f"Tâche sélectionnée : {self.selected_choice_tasks}")
        self.fenetre_tasks.destroy()

        if self.selected_choice_tasks == "volume":
            self.demander_volume()
        else:
            self.executer_script()

    def demander_volume(self):
        """Affiche une fenêtre pour sélectionner le volume de NAO."""
        self.fenetre_vol = tk.Tk()
        self.fenetre_vol.geometry("400x200")
        self.fenetre_vol.title("Volume de NAO")

        self.volume_value = tk.IntVar()

        def update_percentage(val):
            volume_label.config(text=f"Volume : {self.volume_value.get()} %")

        def valider_volume():
            """Valide et applique le volume sélectionné."""
            self.volume = self.volume_value.get()
            print(f"Volume sélectionné : {self.volume} %")
            fichier_output = "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/volume/volume.py"
            subprocess.call(["python2", fichier_output, str(self.creches_ROBOT_IP[self.selected_choice]), str(self.volume)])

        curseur_volume = tk.Scale(self.fenetre_vol, from_=0, to=100, orient="horizontal", variable=self.volume_value, command=update_percentage)
        curseur_volume.pack(pady=10)

        volume_label = tk.Label(self.fenetre_vol, text="Volume : 0 %")
        volume_label.pack(pady=10)

        bouton_valider = tk.Button(self.fenetre_vol, text="Valider", command=valider_volume)
        bouton_valider.pack(pady=10)

        self.fenetre_vol.mainloop()

    def executer_script(self):
        """Exécute le script correspondant au type de tâche choisi."""
        fichier_output = os.path.join(self.current_path, "Nao_tasks", self.selected_choice_tasks, f"{self.selected_choice_tasks}.py")
        print(f"Exécution du script : {fichier_output}")
        subprocess.call(["python3", fichier_output, str(self.creches_ROBOT_IP[self.selected_choice])])


# Lancer l'application
if __name__ == "__main__":
    NaoLauncher()
