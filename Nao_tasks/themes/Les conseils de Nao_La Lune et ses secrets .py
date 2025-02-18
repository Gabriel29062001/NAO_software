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

time.sleep(4.214285714285714)

time.sleep(1.5)
tts.say("Hello l’équipe") 
 time.sleep(0.5)
tts.say("Oh là là, j’ai l’impression que vous avez grandi… Vous avez mangé des haricots magiques ou quoi") 
 time.sleep(0.5)

time.sleep(6.428571428571429)
tts.say("Ooooh, j’adore les questions") 
 time.sleep(0.5)
tts.say("Mon cerveau est prêt, dites-moi tout") 
 time.sleep(0.5)

time.sleep(5.357142857142857)

time.sleep(1.5)
tts.say("Bien sûr que je la vois") 
 time.sleep(0.5)
tts.say("Et pas qu’un peu") 
 time.sleep(0.5)
tts.say("Elle brille dans le ciel comme une grosse lampe") 
 time.sleep(0.5)
tts.say("Impossible de la manquer") 
 time.sleep(0.5)

time.sleep(7.0)

time.sleep(1.5)
tts.say("Je suis un robot, alors ma maison, c’est ici avec vous") 
 time.sleep(0.5)
tts.say("Mais je sais qu’on peut la voir partout dans le monde") 
 time.sleep(0.5)

time.sleep(6.071428571428571)

time.sleep(1.5)
tts.say("Ah, excellente question") 
 time.sleep(0.5)
tts.say("La lune ne change pas vraiment de forme") 
 time.sleep(0.5)
tts.say("C’est juste la lumière du soleil qui l’éclaire différemment") 
 time.sleep(0.5)

time.sleep(5.714285714285714)

time.sleep(1.5)
tts.say("Des fois, elle ressemble à un croissant, des fois elle est toute ronde") 
 time.sleep(0.5)
tts.say("On appelle ça les phases de la lune") 
 time.sleep(0.5)

time.sleep(3.5)

time.sleep(1.5)
tts.say("C’est le soleil qui la rend lumineuse, comme un miroir qui renvoie la lumière") 
 time.sleep(0.5)
tts.say("En vrai, la lune est une grosse boule grise toute poussiéreuse…") 
 time.sleep(0.5)

time.sleep(2.7142857142857144)

time.sleep(1.5)
tts.say("Eh bien, il faudrait voyager à plus de 384 400 kilomètres") 
 time.sleep(0.5)
tts.say("C’est comme faire 30 fois le tour de la Terre en voiture") 
 time.sleep(0.5)
tts.say("Bon courage pour le plein d’essence…") 
 time.sleep(0.5)

time.sleep(5.428571428571429)

time.sleep(1.5)
tts.say("Oh oui") 
 time.sleep(0.5)
tts.say("En 1969, des astronautes ont marché sur la lune") 
 time.sleep(0.5)
tts.say("Vous connaissez Neil Armstrong") 
 time.sleep(0.5)
tts.say("Il est devenu la première personne à poser le pied dessus") 
 time.sleep(0.5)

time.sleep(6.142857142857143)

time.sleep(1.5)
tts.say("Exactement") 
 time.sleep(0.5)
tts.say("Mais entre nous… moi, j’aurais dit") 
 time.sleep(0.5)
tts.say("« Oups, j’ai mis de la poussière lunaire partout") 
 time.sleep(0.5)
tts.say("»") 
 time.sleep(0.5)

time.sleep(4.714285714285714)

time.sleep(1.5)
tts.say("Personne") 
 time.sleep(0.5)
tts.say("C’est pour ça que les traces de pas des astronautes sont encore là, comme si c’était hier") 
 time.sleep(0.5)
tts.say("Il n’y a ni vent ni pluie sur la lune, donc tout reste intact pendant des millions d’années") 
 time.sleep(0.5)

time.sleep(6.357142857142857)

time.sleep(1.5)
tts.say("Pourquoi tu tournes toujours du même côté") 
 time.sleep(0.5)

time.sleep(5.285714285714286)

time.sleep(1.5)
tts.say("Exactement") 
 time.sleep(0.5)
tts.say("Elle tourne sur elle-même à la même vitesse qu’elle tourne autour de la Terre") 
 time.sleep(0.5)

time.sleep(2.4285714285714284)

time.sleep(1.5)
tts.say("À bientôt l’équipe, vous allez me manquer") 
 time.sleep(0.5)

time.sleep(1.5)
