# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from automatisation import text_to_nao


class NaoApp:
    def __init__(self):
        """Initialisation de l'application principale"""
        self.chemin_fichier = None
        self.selected_choice = None
        self.output_fichier = None
        self.robots_ip = ["Nanosphère", "Petits Acrobates", "Les 6 sens", "Le Microcosme", "HOME"]
        
        self.demander_fichier()

    def demander_fichier(self):
        """Affiche une fenêtre pour sélectionner un fichier Word"""
        self.fenetre_fichier = tk.Tk()
        self.fenetre_fichier.title("Choisissez le fichier texte de NAO")

        bouton_parcourir = tk.Button(
            self.fenetre_fichier, text="Parcourir", command=self.parcourir_fichier
        )
        bouton_parcourir.pack(pady=100, padx=200, ipadx=20, ipady=10)

        self.fenetre_fichier.mainloop()

    def parcourir_fichier(self):
        """Ouvre un explorateur pour choisir un fichier Word"""
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers Word", "*.docx")])
        if fichier:
            print(f"Fichier sélectionné : {fichier}")
            self.chemin_fichier = fichier
            self.fenetre_fichier.destroy()
            self.demander_choix_creche()

    def demander_choix_creche(self):
        """Affiche une fenêtre pour sélectionner la crèche"""
        self.fenetre_choix = tk.Tk()
        self.fenetre_choix.geometry("400x200")
        self.fenetre_choix.title("NAO")

        question_label = tk.Label(self.fenetre_choix, text="Dans quelle crèche êtes-vous ?")
        question_label.pack(pady=10)

        self.curseur = tk.StringVar()
        for i, creche in enumerate(self.robots_ip):
            tk.Radiobutton(self.fenetre_choix, text=creche, variable=self.curseur, value=i).pack()

        bouton_afficher = tk.Button(self.fenetre_choix, text="Sélectionner réponse", command=self.afficher_choix)
        bouton_afficher.pack(pady=10)

        self.fenetre_choix.mainloop()

    def afficher_choix(self):
        """Récupère le choix sélectionné et génère le script NAO"""
        self.selected_choice = int(self.curseur.get())
        print(f"La réponse choisie est : {self.robots_ip[self.selected_choice]}")
        self.fenetre_choix.destroy()

        self.output_fichier = text_to_nao(self.chemin_fichier, self.selected_choice)
        print(self.output_fichier)

        self.afficher_confirmation()

    def afficher_confirmation(self):
        """Affiche un message confirmant la génération du fichier"""
        fenetre_confirmation = tk.Tk()
        fenetre_confirmation.title("Succès")
        fenetre_confirmation.geometry("1200x200")

        window_text = f"Nao est prêt à être déployé avec le fichier :\n{self.output_fichier}"

        label_message = tk.Label(fenetre_confirmation, text=window_text, font=("Helvetica", 14))
        label_message.pack(pady=20)

        fenetre_confirmation.mainloop()


# Exécution de l'application
if __name__ == "__main__":
    NaoApp()
