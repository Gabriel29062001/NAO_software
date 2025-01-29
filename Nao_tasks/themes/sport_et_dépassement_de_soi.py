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


    

time.sleep(3.9285714285714284)

time.sleep(15.857142857142858)

tts.say("Bonjour les enfants") 
time.sleep(0.5) 
tts.say("Je suis tellement content de vous revoir") 
time.sleep(0.5) 
tts.say("Vous m'avez manqué") 
time.sleep(0.5) 
tts.say("Eve m'a dit que vous vous entraîniez depuis 10 mois pour le défi des 10") 
time.sleep(0.5) 
tts.say("Est-ce que c'est vrai") 
time.sleep(0.5) 

time.sleep(2.2142857142857144)

tts.say("Je suis très fier de vous") 
time.sleep(0.5) 
tts.say("Nous allons regarder ensemble pourquoi c'est important de pratiquer du sport") 
time.sleep(0.5) 

time.sleep(2.357142857142857)

tts.say("Le sport c’est un entraînement pour notre cœur et nos muscles") 
time.sleep(0.5) 
tts.say("Quand nous bougeons, notre cœur bat plus vite, ce qui le rend plus fort") 
time.sleep(0.5) 
tts.say("Et nos muscles deviennent plus forts aussi") 
time.sleep(0.5) 
tts.say("De plus, le sport aide à garder nos poumons en bonne santé en les faisant travailler plus fort") 
time.sleep(0.5) 
tts.say("Ainsi, notre corps est prêt à affronter tous les défis de la vie") 
time.sleep(0.5) 

time.sleep(3.2142857142857144)

tts.say("Oui, Eve, le sport libère des endorphines dans notre cerveau") 
time.sleep(0.5) 
tts.say("Ce sont des petites substances magiques qui nous rendent heureux et joyeux") 
time.sleep(0.5) 
tts.say("C'est pour ça que nous nous sentons si bien après avoir joué et bougé") 
time.sleep(0.5) 
tts.say("Le sport est une véritable potion magique pour notre bien-être") 
time.sleep(0.5) 

time.sleep(3.0)

tts.say("Le sport rend notre esprit fort aussi") 
time.sleep(0.5) 
tts.say("Quand on décide de faire quelque chose et qu'on travaille dur, ça nous rend plus forts et sûrs de nous") 
time.sleep(0.5) 
tts.say("Quand on réussit à surmonter un défi en sport, ça nous montre qu'on peut réussir dans d'autres choses aussi") 
time.sleep(0.5) 
tts.say("Le sport nous apprend qu'on peut accomplir de grandes choses si on ne baisse pas les bras") 
time.sleep(0.5) 
tts.say("C'est comme un super pouvoir pour notre esprit") 
time.sleep(0.5) 

time.sleep(3.2142857142857144)

tts.say("J'aime la course aussi") 
time.sleep(0.5) 
tts.say("Et j'adorerais pouvoir faire le défi des 10 avec vous") 
time.sleep(0.5) 
tts.say("Mais vous savez, quand je marche, je grince de tous les côtés") 
time.sleep(0.5) 

id = motion.post.moveTo(1, 0, 0) 
motion.wait(id, 0)


time.sleep(2.5714285714285716)

time.sleep(3.0)

tts.say("Ne vous inquiétez pas, je suis toujours là pour vous encourager et vous enseigner toutes sortes de choses sur le sport et le dépassement de soi") 
time.sleep(0.5) 
tts.say("Alors, même si je ne peux pas courir avec vous, je serai toujours là pour vous soutenir depuis la ligne d'arrivée") 
time.sleep(0.5) 

time.sleep(4.142857142857143)

tts.say("Allez, montrez-moi ce que vous avez appris et donnez tout ce que vous avez dans ce défi des 10") 
time.sleep(0.5) 
tts.say("Je serai là pour vous applaudir à chaque pas du chemin") 
time.sleep(0.5) 

time.sleep(1.5)

tts.say("C'est parti pour la danse de Nao pour finir aujourd'hui")
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
