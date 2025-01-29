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





time.sleep(2.9285714285714284)

time.sleep(5.071428571428571)

tts.say("Est-ce qu’on peut dire que je tombe à pic") 
time.sleep(0.5) 

time.sleep(9.285714285714286)

tts.say("Bien sûr") 
time.sleep(0.5) 
tts.say("Les enfants, le système digestif est comme une usine spéciale dans votre corps qui transforme la nourriture en énergie") 
time.sleep(0.5) 
tts.say("Imaginez que votre corps a une travailleuse très forte qui s'occupe de tout ça") 
time.sleep(0.5) 

time.sleep(6.0)

tts.say("Bien sûr") 
time.sleep(0.5) 
tts.say("Quand vous mangez, la nourriture commence par aller dans votre bouche") 
time.sleep(0.5) 
tts.say("Vous utilisez vos dents pour bien mâcher la nourriture, puis vous l'avalez") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("Ensuite, la nourriture passe par un tuyau secret appelé l'œsophage") 
time.sleep(0.5) 
tts.say("L'œsophage aide la nourriture à descendre jusqu'à votre estomac, qui est comme une poche magique dans votre ventre") 
time.sleep(0.5) 

time.sleep(3.857142857142857)

tts.say("L'estomac est spécial parce qu'il utilise des liquides spéciaux pour mélanger la nourriture") 
time.sleep(0.5) 
tts.say("C'est comme si votre estomac faisait une grande soupe pour que votre corps puisse l'utiliser") 
time.sleep(0.5) 

time.sleep(5.071428571428571)

tts.say("Après l'estomac, la nourriture passe dans un long chemin appelé l'intestin") 
time.sleep(0.5) 
tts.say("L'intestin est très long et il absorbe toutes les bonnes choses de la nourriture, comme les vitamines et les minéraux") 
time.sleep(0.5) 

time.sleep(4.857142857142857)

tts.say("Ce que votre corps n'utilise pas devient des déchets") 
time.sleep(0.5) 
tts.say("Les déchets passent par un autre chemin appelé le rectum, et c'est là que vous allez aux toilettes") 
time.sleep(0.5) 

time.sleep(3.357142857142857)

tts.say("C’est exactement ça") 
time.sleep(0.5) 
tts.say("On appelle ça le caca, mais le mot savant est les selles") 
time.sleep(0.5) 

time.sleep(7.214285714285714)

tts.say("De rien") 
time.sleep(0.5) 
tts.say("Le système digestif est très important pour que votre corps reste fort et en bonne santé") 
time.sleep(0.5) 
tts.say("Alors, mangez bien vos légumes, fruits et céréales pour aider votre corps à fonctionner") 
time.sleep(0.5) 

time.sleep(7.071428571428571)

tts.say("Avec plaisir") 
time.sleep(0.5) 
tts.say("Si vous avez d'autres questions sur le corps humain, n'hésitez pas à me demander") 
time.sleep(0.5) 
tts.say("À bientôt") 
time.sleep(0.5) 

time.sleep(1.5)

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
