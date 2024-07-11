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
tts = ALProxy('ALTextToSpeech', ROBOT_IP, 9559) 
motion = ALProxy('ALMotion', ROBOT_IP, 9559) 

turn_angle =  3.14149 # 180 degrees in radians 
tts.say('Bonjour Ève')


while True : 
    front_head_touch = tactile_touch.getStatus()
    if front_head_touch[7][1] == True:
        break


id = motion.post.moveTo(0.5, 0, 0) 
motion.wait(id, 0)


tts.say("Bonjour les enfants, je suis très content de vous voir aujourd’hui") 
time.sleep(0.5) 
tts.say("Êtes-vous prêts à apprendre plein de choses") 
time.sleep(0.5) 

time.sleep(3.357142857142857)

time.sleep(1.5)

time.sleep(4.285714285714286)

tts.say("Aujourd’hui, je vais vous parler de l’importance de manger des fruits et des légumes tous les jours") 
time.sleep(0.5) 

time.sleep(5.285714285714286)

tts.say("Vous savez les enfants, les fruits et les légumes sont très importants pour ton corps") 
time.sleep(0.5) 
tts.say("Ils sont remplis de choses spéciales appelées vitamines et minéraux") 
time.sleep(0.5) 
tts.say("Ces petites choses aident notre corps à grandir et à rester fort") 
time.sleep(0.5) 
tts.say("Par exemple, les vitamines aident nos yeux à bien voir, nos os à rester solides et nos muscles à être forts comme ceux des super-héros") 
time.sleep(0.5) 
tts.say("En plus, les fruits et les légumes ont des fibres") 
time.sleep(0.5) 
tts.say("Ces fibres aident à digérer les aliments et à garder notre ventre heureux et en bonne santé") 
time.sleep(0.5) 

time.sleep(6.428571428571429)

tts.say("Oui, c'est vrai") 
time.sleep(0.5) 
tts.say("Comme ça, notre corps reste hydraté et notre peau reste douce et souple") 
time.sleep(0.5) 

time.sleep(7.0)

tts.say("C'est parce que chaque couleur signifie qu'ils ont différents types de vitamines et de nutriments") 
time.sleep(0.5) 
tts.say("Par exemple, les carottes orange sont bonnes pour nos yeux, les épinards verts sont bons pour nos muscles, et les fraises rouges sont pleines de vitamine C pour nous aider à combattre les microbes") 
time.sleep(0.5) 

time.sleep(12.714285714285714)

tts.say("Oui, c'est vrai") 
time.sleep(0.5) 

time.sleep(6.142857142857143)

tts.say("En tant que robot, je n'ai pas de bouche pour les goûter") 
time.sleep(0.5) 
tts.say("Mais je suis sûr que si j'avais une bouche, je dirais") 
time.sleep(0.5) 
tts.say("'Miam") 
time.sleep(0.5) 
tts.say("' à chaque bouchée de brocolis et de choux de Bruxelles") 
time.sleep(0.5) 

time.sleep(9.928571428571429)

time.sleep(4.857142857142857)

tts.say("oh oui avec plaisir") 
time.sleep(0.5) 
tts.say("Dance de Nao") 
time.sleep(0.5) 

time.sleep(3.0714285714285716)

time.sleep(1.5)

time.sleep(1.5)

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
