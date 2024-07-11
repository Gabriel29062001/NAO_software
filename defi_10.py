# -*- coding: utf-8 -*- 

import sys
import time

import os

path_to_add = "~/Documents/nao/nao_softwarev3/lib/linux/naoqi/pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages"

path_to_add = os.path.expanduser(path_to_add)

sys.path.append(path_to_add)

# Maintenant vous pouvez importer naoqi
import naoqi
from naoqi import ALProxy



# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
    print(ROBOT_IP)
else:
    print("probleme arguments")

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 

turn_angle =  3.14149 # 180 degrees in radians 
tts.say('Bonjour Rachel')

while True : 
    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][1] == True:
        tts.say("Je savais que tu y parviendrais !")
        time.sleep(0.5)
        tts.say("tu as demontré une grande persévérance et tu t'es surpassé")
        time.sleep(0.5)
        tts.say("Toutes mes félicitaions")

    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][2] == True:
        break
