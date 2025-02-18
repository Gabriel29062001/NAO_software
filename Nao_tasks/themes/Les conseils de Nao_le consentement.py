# -*- coding: utf-8 -*- 
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
else:
    print("probleme arguments")
# Créer une instance du proxy pour ALSpeechRecognition
speech_recognition = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)

# Désactiver la reconnaissance vocale
speech_recognition.pause(True)

tactile_touch = ALProxy('ALTouch', ROBOT_IP, 9559) 
tts = ALProxy('ALAnimatedSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 

turn_angle =  3.14149 # 180 degrees in radians 
tts.say('Bonjour Ève')


while True : 
    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][1] == True:
        break




time.sleep(2.642857142857143)

time.sleep(4.214285714285714)
tts.say("Hello l’équipe") 
 time.sleep(0.5)
tts.say("Vous avez l’air rayonnants aujourd’hui…") 
 time.sleep(0.5)

time.sleep(6.071428571428571)
tts.say("Ooooh, j’adore parler de choses importantes") 
 time.sleep(0.5)
tts.say("Dites-moi tout") 
 time.sleep(0.5)

time.sleep(3.0)
tts.say("Excellente question") 
 time.sleep(0.5)
tts.say("Le consentement, c’est quand on demande à quelqu’un avant de faire quelque chose avec lui, et qu’on respecte sa réponse") 
 time.sleep(0.5)

time.sleep(5.785714285714286)
tts.say("Bien sûr") 
 time.sleep(0.5)
tts.say("Parce que tout le monde n’a pas toujours envie d’un câlin") 
 time.sleep(0.5)
tts.say("Et si la personne dit non, il faut respecter son choix") 
 time.sleep(0.5)

time.sleep(5.571428571428571)
tts.say("Pas du tout") 
 time.sleep(0.5)
tts.say("Parfois, on est fatigué, on n’a pas envie, ou on préfère faire autre chose") 
 time.sleep(0.5)
tts.say("Dire non, ce n’est pas être méchant, c’est juste dire ce qu’on ressent") 
 time.sleep(0.5)

time.sleep(5.071428571428571)
tts.say("Alors tu as le droit de dire non") 
 time.sleep(0.5)
tts.say("Ton corps, c’est toi qui décides") 
 time.sleep(0.5)
tts.say("On ne doit jamais se sentir obligé de faire quelque chose qu’on ne veut pas") 
 time.sleep(0.5)

time.sleep(2.5714285714285716)
tts.say("Dans ce cas, tu peux dire « J’ai dit non », Quand quelqu’un dit non, on doit toujours l’écouter") 
 time.sleep(0.5)

time.sleep(9.0)
tts.say("Pas tout à fait") 
 time.sleep(0.5)
tts.say("Si un adulte demande à l’enfant de se brosser les dents ou d’attacher la ceinture en voiture, c’est pour protéger l’enfant") 
 time.sleep(0.5)
tts.say("Mais si quelqu’un demande quelque chose qui met mal à l’aise, alors oui, il faut dire non et en parler à quelqu’un de confiance") 
 time.sleep(0.5)

time.sleep(4.214285714285714)
tts.say("Alors il doit arrêter tout de suite") 
 time.sleep(0.5)
tts.say("Même si c’est un jeu, si quelqu’un dit stop, on respecte son choix") 
 time.sleep(0.5)

time.sleep(4.5)
tts.say("C’est ma mission, répondre à votre curiosité, car les enfants, vous savez… sans respect, on ne peut pas être bien ensemble") 
 time.sleep(0.5)

time.sleep(1.5)
tts.say("À bientôt l’équipe, et souvenez-vous") 
 time.sleep(0.5)
tts.say("votre corps vous appartient") 
 time.sleep(0.5)

time.sleep(1.5)
