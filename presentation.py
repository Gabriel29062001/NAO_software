# -*- coding: utf-8 -*- 
import Tkinter as tk
import sys
import os



path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy


try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")
    fenetre = tk.Tk()
    fenetre.geometry("400x250")
    fenetre.title("NAO")
    fenetre.mainloop
    
# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
else:
    print("probleme arguments")

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 
tts.say("Bonjour moi c'est Nao, aujourdhui je teste avec vous la nouvelle application facilitant mon utilisation")
