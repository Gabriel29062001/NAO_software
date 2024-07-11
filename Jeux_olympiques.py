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

time.sleep(15.5)

tts.say("Bonjour les enfants, quel plaisir de vous revoir") 
time.sleep(0.5) 
tts.say("Aujourd'hui, je vais vous parler des Jeux Olympiques") 
time.sleep(0.5) 

time.sleep(3.5)

tts.say("Les Jeux Olympiques sont une grande compétition où des athlètes du monde entier viennent pour jouer à différents sports") 
time.sleep(0.5) 
tts.say("C'est vraiment spécial") 
time.sleep(0.5) 

time.sleep(6.928571428571429)

tts.say("Les Jeux Olympiques ne sont pas seulement des jeux, ils montrent aussi comment les gens de différents pays peuvent jouer ensemble et se respecter") 
time.sleep(0.5) 

time.sleep(3.7857142857142856)

tts.say("On peut voir beaucoup de sports comme la course, la natation, le basketball et bien d'autres") 
time.sleep(0.5) 
tts.say("Les athlètes s'entraînent très dur pour montrer leurs talents") 
time.sleep(0.5) 

time.sleep(9.428571428571429)

time.sleep(3.9285714285714284)

tts.say("J'aimerais tellement y aller, mais je suis trop petit et j'ai peur de me faire écraser par la foule") 
time.sleep(0.5) 

time.sleep(2.7142857142857144)

tts.say("Oui, un athlète, c'est quelqu'un qui s'entraîne beaucoup pour jouer aux Jeux Olympiques et inspirer les autres") 
time.sleep(0.5) 

tts.say("Mais j'aurais encore plus aimé porter la flamme olympique") 
time.sleep(0.5) 

time.sleep(2.7142857142857144)

tts.say("C'est une flamme spéciale allumée en Grèce, puis transportée à travers différents pays avant d'arriver aux Jeux Olympiques") 
time.sleep(0.5) 

time.sleep(3.642857142857143)

tts.say("Ne t'inquiète pas, ils ont une flamme de secours prête à être allumée rapidement") 
time.sleep(0.5) 

time.sleep(5.428571428571429)

time.sleep(9.714285714285714)

tts.say("Moi aussi, je vous aime les enfants") 
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
