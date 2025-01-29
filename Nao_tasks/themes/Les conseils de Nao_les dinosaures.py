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





time.sleep(2.5714285714285716)

time.sleep(2.357142857142857)

tts.say("Salut l'équipe") 
time.sleep(0.5) 
tts.say("Je vais très bien, merci") 
time.sleep(0.5) 
tts.say("Et vous, comment allez-vous") 
time.sleep(0.5) 
tts.say("Je suis content de vous revoir") 
time.sleep(0.5) 

time.sleep(6.357142857142857)

tts.say("Oui, ils ont existé") 
time.sleep(0.5) 
tts.say("Il y a très longtemps, des millions d'années avant que les humains n’apparaissent") 
time.sleep(0.5) 
tts.say("Les dinosaures vivaient partout sur Terre, mais ils ont disparu il y a environ 65 millions d'années") 
time.sleep(0.5) 
tts.say("Aujourd'hui, on apprend sur eux grâce aux fossiles que les paléontologues découvrent") 
time.sleep(0.5) 

time.sleep(2.7857142857142856)

tts.say("Les fossiles, ce sont des restes de dinosaures, comme leurs os, leurs dents ou même leurs empreintes, qui se sont transformés en pierre avec le temps") 
time.sleep(0.5) 
tts.say("Ils sont enfouis dans le sol, et les scientifiques les trouvent pour comprendre comment les dinosaures vivaient") 
time.sleep(0.5) 

time.sleep(2.5)

tts.say("C’est une question importante") 
time.sleep(0.5) 
tts.say("Une grande météorite est tombée sur Terre, et cela a changé le climat") 
time.sleep(0.5) 
tts.say("Il est devenu très difficile pour les dinosaures de survivre") 
time.sleep(0.5) 
tts.say("Il y avait moins de lumière et de nourriture") 
time.sleep(0.5) 
tts.say("C'est ainsi qu’ils ont disparu peu à peu") 
time.sleep(0.5) 

time.sleep(4.357142857142857)

tts.say("Non, pas tous") 
time.sleep(0.5) 
tts.say("Certains, comme le Compsognathus, étaient aussi petits qu’un poulet") 
time.sleep(0.5) 
tts.say("Mais d’autres, comme le Brachiosaure, étaient immenses, plus grands que des maisons") 
time.sleep(0.5) 
tts.say("Il y avait beaucoup de tailles différentes") 
time.sleep(0.5) 

time.sleep(3.9285714285714284)

tts.say("Oui, certains pouvaient voler, comme les Ptérodactyles") 
time.sleep(0.5) 

time.sleep(3.857142857142857)

tts.say("J’aime bien le Tricératops, avec ses trois grandes cornes sur la tête") 
time.sleep(0.5) 
tts.say("Il avait l’air très fort, mais il ne mangeait que des plantes") 
time.sleep(0.5) 
tts.say("Un dinosaure pacifique, mais qui se défendait bien") 
time.sleep(0.5) 

time.sleep(3.0714285714285716)

tts.say("Jamais") 
time.sleep(0.5) 
tts.say("Je suis arrivé dans la vie des millions d’années après la disparition des dinosaures") 
time.sleep(0.5) 

time.sleep(8.928571428571429)

tts.say("C'est ma mission, répondre à votre curiosité, car les enfants, vous savez, sans curiosité, on n’apprend jamais") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("À bientôt, l’équipe") 
time.sleep(0.5) 

time.sleep(1.5)

time.sleep(1.5)

