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





time.sleep(2.4285714285714284)

time.sleep(5.5)

tts.say("Salut les enfants") 
time.sleep(0.5) 
tts.say("Je vais bien et je suis super content de vous voir") 
time.sleep(0.5) 

time.sleep(4.214285714285714)

tts.say("Je vais vous raconter une légende") 
time.sleep(0.5) 

time.sleep(3.142857142857143)

tts.say("Une légende, c'est une vieille histoire qu'on raconte depuis longtemps") 
time.sleep(0.5) 
tts.say("Elle peut mélanger des choses qui sont vraies avec des choses qui ne le sont pas") 
time.sleep(0.5) 
tts.say("Parfois, il y a des parties mystérieuses ou magiques") 
time.sleep(0.5) 
tts.say("Les gens aiment les légendes parce qu'elles sont amusantes et qu'elles font travailler l'imagination") 
time.sleep(0.5) 
tts.say("C'est comme une grande aventure que l'on peut raconter encore et encore") 
time.sleep(0.5) 

time.sleep(4.428571428571429)

tts.say("Oh oui, c'est celle du monstre du Loch Ness") 
time.sleep(0.5) 

time.sleep(2.4285714285714284)

time.sleep(1.5)

tts.say("Au Loch Ness, en Écosse, il y a une vieille légende sur un mystérieux monstre qui vivrait tout au fond du lac") 
time.sleep(0.5) 
tts.say("On l'appelle le monstre du Loch Ness") 
time.sleep(0.5) 

time.sleep(3.5)

tts.say("Selon la légende, il est énorme, avec un long cou et des écailles brillantes") 
time.sleep(0.5) 
tts.say("Rien que d'y penser, ça donne des frissons") 
time.sleep(0.5) 

time.sleep(3.0714285714285716)

tts.say("Oui, beaucoup de personnes disent l'avoir aperçu, surtout par des jours brumeux") 
time.sleep(0.5) 
tts.say("Il y a même des photos, mais elles sont souvent floues et mystérieuses") 
time.sleep(0.5) 

time.sleep(2.7857142857142856)

tts.say("Non, je ne l'ai jamais vu moi-même") 
time.sleep(0.5) 
tts.say("Mais je comprends pourquoi les gens sont fascinés") 
time.sleep(0.5) 
tts.say("Il y a même des chercheurs qui passent leur vie à essayer de le trouver, mais ils n'ont pas encore de preuve solide") 
time.sleep(0.5) 

time.sleep(7.428571428571429)

tts.say("Je pense que c'est probablement une légende aussi") 
time.sleep(0.5) 
tts.say("Mais c'est ça qui rend les légendes si spéciales") 
time.sleep(0.5) 
tts.say("Elles nous transportent dans un monde de mystère et d'aventure") 
time.sleep(0.5) 
tts.say("Même si elles ne sont pas vraies, elles nous font rêver et nous émerveiller") 
time.sleep(0.5) 
tts.say("C'est ce qui les rend si précieuses") 
time.sleep(0.5) 

time.sleep(7.357142857142857)

time.sleep(3.2857142857142856)

time.sleep(2.0714285714285716)

time.sleep(1.8571428571428572)

time.sleep(1.5)
# Après les importations et la déclaration des variables
animation_player = ALProxy('ALAnimationPlayer',ROBOT_IP, 9559)

# Déclencher une animation
animation_name = 	"animations/Stand/Gestures/ShowFloor_3"
animation_player.run(animation_name)

animation_name = 	"animations/Stand/Gestures/Me_4"
animation_player.run(animation_name)
animation_name ="animations/Stand/Gestures/Hey_1"
animation_player.run(animation_name)
animation_name = 	"animations/Stand/Gestures/ShowSky_1"
animation_player.run(animation_name)
animation_name =	"animations/Stand/Gestures/YouKnowWhat_1"
animation_player.run(animation_name)
animation_name ="animations/Stand/Gestures/Hey_1"
animation_player.run(animation_name)
animation_name = 	"animations/Stand/Gestures/ShowSky_1"
animation_player.run(animation_name)
animation_name =	"animations/Stand/Gestures/YouKnowWhat_1"
animation_player.run(animation_name)
animation_name ="animations/Stand/Gestures/Hey_1"
animation_player.run(animation_name)
