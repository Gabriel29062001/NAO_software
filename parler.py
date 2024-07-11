# -*- coding: utf-8 -*- 
# -*- coding: utf-8 -*- 
import sys
import os
import subprocess
import Tkinter as Tk

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy

global texte




# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    argument = sys.argv[2]  # Convertir en entier
else:
    print("probleme arguments")



tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)

def valider():
    texte = zone_texte.get("1.0", "end-1c") 
    zone_texte.delete("1.0", "end")
    print("Type of texte:", type(texte))
    print(texte)
    tts.say(texte.encode('utf-8')) 



if argument == "météo":
    subprocess.call(["python3", "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/general/meteo.py",str(ROBOT_IP)])
elif argument == "actualité":
    tts.say("Cette semaine le club de hockey de Lausanne a gagne 5-3 contre l'équipe de Zurich, elle revient donc à égalité en nombre de manches gagnés dans cette finale, ce soir grande finale entre les deux equipes")

elif argument == "programmation":
    tts.say("je suis programmé grâce à Gabriel qui me donne les instructions en python pour que je puisse les éxecuter, nous verrons la semaine prochaine comment écrire votre premier code")

elif argument == "personaliser":
   
    fenetre_parole = Tk.Tk()
    fenetre_parole.geometry("400x200")
    fenetre_parole.title("Entrez le texte que vous voulez dire")

    zone_texte = Tk.Text(fenetre_parole, height=5, width=40)
    zone_texte.pack()

    bouton_valider = Tk.Button(fenetre_parole, text="Valider", command=valider)
    bouton_valider.pack()

    fenetre_parole.mainloop()



