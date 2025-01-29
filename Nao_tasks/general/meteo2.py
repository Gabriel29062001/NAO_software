# -*- coding: utf-8 -*- 
import sys
import os
import subprocess
import Tkinter as Tk
print("hello world")

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy

# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    temperature = sys.argv[2]  # Convertir en entier
    description = sys.argv[3]  # Convertir en entier

else:
    print("probleme arguments")


tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
tts.say("Aujourd'hui il fait ", temperature)
tts.say("et la vill est", description)
