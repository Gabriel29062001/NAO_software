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





time.sleep(3.2857142857142856)

time.sleep(7.142857142857143)

tts.say("Salut l'équipe, je vais bien et je suis content de vous voir") 
time.sleep(0.5) 
tts.say("Je suis avec vous pour vous parler des hommes de nos ancêtres, les hommes de Cro-Magnon") 
time.sleep(0.5) 

time.sleep(4.0)

tts.say("Ahahaha, non, les hommes de Cro-Magnon sont nos ancêtres très anciens") 
time.sleep(0.5) 
tts.say("Ils ont vécu il y a longtemps, pendant la Préhistoire") 
time.sleep(0.5) 

time.sleep(5.0)

tts.say("Les hommes de Cro-Magnon vivaient principalement en Europe, dans des cavernes naturelles qu'ils utilisaient comme abris") 
time.sleep(0.5) 

time.sleep(2.4285714285714284)

tts.say("Ils chassaient des animaux comme les bisons et les cerfs, et ils cueillaient des baies et des racines pour compléter leur alimentation") 
time.sleep(0.5) 

time.sleep(2.642857142857143)

tts.say("Oui, les femmes de Cro-Magnon participaient aussi à la chasse et à la cueillette pour nourrir leur famille") 
time.sleep(0.5) 

time.sleep(2.857142857142857)

tts.say("Hahaha, non, ils portaient des vêtements fabriqués à partir de peaux d'animaux pour se protéger du froid") 
time.sleep(0.5) 

time.sleep(3.2142857142857144)

tts.say("Les hommes de Cro-Magnon avaient leur propre langue pour se parler, différente du français que nous utilisons aujourd'hui") 
time.sleep(0.5) 

time.sleep(5.285714285714286)

tts.say("ahaha, C'est normal, les hommes de Cro-Magnon ont vécu il y a très longtemps, avant même que les villes et les technologies comme moi existent") 
time.sleep(0.5) 

time.sleep(2.857142857142857)

tts.say("Moi, je suis très différent des hommes de Cro-Magnon") 
time.sleep(0.5) 
tts.say("Je suis un robot moderne, fait par les humains pour vous aider et vous raconter notre histoire") 
time.sleep(0.5) 
tts.say("Moi, je n'ai jamais vu d'hommes de Cro-Magnon, et eux non plus n'ont jamais vu de robots comme moi") 
time.sleep(0.5) 
tts.say("Gabriel m’apprend beaucoup de chose et c’est lui qui m’a tout appris sur la préhistoire") 
time.sleep(0.5) 
tts.say("Si je rencontrais un homme de Cro-Magnon, il aurait sûrement très peur de moi") 
time.sleep(0.5) 

time.sleep(3.0)

tts.say("Oh, c'est gentil") 
time.sleep(0.5) 
tts.say("C'est normal") 
time.sleep(0.5) 
tts.say("Vous vivez dans une époque pleine de technologie") 
time.sleep(0.5) 
tts.say("Votre but est de continuer à m'utiliser pour devenir encore plus forts et plus intelligents") 
time.sleep(0.5) 
tts.say("Je suis là pour être votre ami et vous aider") 
time.sleep(0.5) 

time.sleep(5.0)

tts.say("Bien sûr, comme toujours") 
time.sleep(0.5) 
tts.say("À bientôt, l'équipe") 
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
