# -*- coding: utf-8 -*- 
import sys
import os

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy



angle = 3.1415
try:
    from naoqi import ALProxy
except ImportError:
    print("Problème avec l'importation de naoqi.")

print(sys.argv[2])
# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    rotation = float(sys.argv[2])*angle/180  # Convertir en entier
else:
    print("probleme arguments")


tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559)


id = motion.post.moveTo(0, 0, rotation) 
motion.wait(id, 0)
