# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from automatisation import text_to_nao

def parcourir_fichier():
    fichier = filedialog.askopenfilename(filetypes=[("Fichiers Word", "*.docx")])
    if fichier:
        print("Fichier sélectionné : %s" % fichier)
        global chemin_fichier
        chemin_fichier = fichier
        fenetre.destroy()

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Choisissez le fichier texte de NAO")

# Créer un bouton pour parcourir le fichier
bouton_parcourir = tk.Button(fenetre, text="Parcourir", command=parcourir_fichier)
bouton_parcourir.pack(pady=100, padx=200, ipadx=20, ipady=10)  # Ajustement de la taille du bouton

# Variable pour stocker le chemin du fichier sélectionné
chemin_fichier = None

# Boucle principale
fenetre.mainloop()

# Après la boucle principale, le code continue ici
if chemin_fichier:
    print("Chemin du fichier sélectionné: %s" % chemin_fichier)
else:
    print("Aucun fichier sélectionné.")



selected_choice = None 

def afficher_choix():
    global selected_choice
    selected_choice = curseur.get()
    print("La réponse choisie est : " + selected_choice)
    fenetre.destroy()  # Quitter la boucle principale

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("400x200")
fenetre.title("NAO")

# Créer un label pour afficher la question
question_label = tk.Label(fenetre, text="Dans quels crèches êtes vous ?")
question_label.pack(pady=10)

# Créer un curseur (Radiobutton) avec les choix possibles
curseur = tk.StringVar()

choix_a = tk.Radiobutton(fenetre, text="Nanosphère", variable=curseur, value=0)
choix_b = tk.Radiobutton(fenetre, text="Petits Acrobates", variable=curseur, value=1)
choix_c = tk.Radiobutton(fenetre, text="Les 6 sens", variable=curseur, value=2)
choix_d = tk.Radiobutton(fenetre, text="Le Microcosme", variable=curseur, value=3)
choix_e = tk.Radiobutton(fenetre, text="HOME", variable=curseur, value=4)


choix_a.pack()
choix_b.pack()
choix_c.pack()
choix_d.pack()
choix_e.pack()

# Créer un bouton pour afficher le choix
bouton_afficher = tk.Button(fenetre, text="Sélectionner réponse", command=afficher_choix)
bouton_afficher.pack(pady=10)

# Boucle principale
fenetre.mainloop()

output_fichier = text_to_nao(chemin_fichier, int(selected_choice))
print(output_fichier)



fenetre2 = tk.Tk()
fenetre2.title("Success")
fenetre2.geometry("1200x200")  # Définir la taille de la fenêtre

window_text = "Nao is ready to be deployed with the file in : \n" + str(output_fichier)

# Créer un label avec le message "You are great"
label_message = tk.Label(fenetre2, text= window_text, font=("Helvetica", 14))
label_message.pack(pady=20)

fenetre2.mainloop()



