# -*- coding: utf-8 -*- 
import sys
import os

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy
ROBOT_IP = "172.16.40.105"
volume = 80
# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 2:
    ROBOT_IP = sys.argv[1]
    volume = int(sys.argv[2])
else:
    print("probleme arguments")

tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
print(volume)
# Connexion au proxy ALAudioDevice
audioProxy = ALProxy("ALAudioDevice", ROBOT_IP, 9559)


audioProxy.setOutputVolume(volume)

# Vérifier que le volume a été changé
new_set_volume = audioProxy.getOutputVolume()
tts.say("Voici mon nouveau niveau sonore ")


