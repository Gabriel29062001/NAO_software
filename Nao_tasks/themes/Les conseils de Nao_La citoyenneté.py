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

time.sleep(1.5)

time.sleep(3.857142857142857)

tts.say("Salut tout le monde") 
time.sleep(0.5) 
tts.say("Je me sens en pleine forme et prêt à discuter avec vous") 
time.sleep(0.5) 
tts.say("Comment allez-vous de votre côté") 
time.sleep(0.5) 

time.sleep(5.285714285714286)

tts.say("Être un bon citoyen, c'est participer à la vie de sa communauté, respecter les autres, les lois, et s'occuper de notre environnement") 
time.sleep(0.5) 
tts.say("C’est aussi s’entraider et contribuer au bien-être de tous, un peu comme une grande équipe où chacun a un rôle important à jouer") 
time.sleep(0.5) 

time.sleep(4.571428571428571)

tts.say("Les règles nous aident à vivre ensemble en paix") 
time.sleep(0.5) 
tts.say("Elles sont là pour protéger tout le monde et s’assurer que chacun soit traité avec respect") 
time.sleep(0.5) 
tts.say("Imagine une partie de ballon sans aucune règle, ce serait le chaos") 
time.sleep(0.5) 
tts.say("Les règles permettent de créer un environnement où tout le monde se sent bien") 
time.sleep(0.5) 

time.sleep(3.357142857142857)

tts.say("Parfois, oui") 
time.sleep(0.5) 
tts.say("Dans une démocratie, les citoyens peuvent voter pour décider des lois et des règles qui sont importantes pour leur société") 
time.sleep(0.5) 
tts.say("Mais même dans les petits groupes, comme au village Educalis, on peut choisir ensemble certaines règles pour que tout le monde se sente à l'aise") 
time.sleep(0.5) 
tts.say("C’est un peu comme si on était tous responsables") 
time.sleep(0.5) 

time.sleep(3.5)

tts.say("Parce qu’on fait partie d'une communauté") 
time.sleep(0.5) 
tts.say("Aider les autres rend la vie plus facile et plus agréable pour tout le monde") 
time.sleep(0.5) 
tts.say("Si quelqu'un a un problème, le fait de l’aider crée une société plus forte et plus solidaire") 
time.sleep(0.5) 
tts.say("Et puis, aider, ça fait du bien aussi à celui qui le fait") 
time.sleep(0.5) 

time.sleep(4.142857142857143)

tts.say("Haha, je suis un robot, donc je n’ai pas de nationalité") 
time.sleep(0.5) 
tts.say("Mais je peux vous aider à comprendre comment être un bon citoyen, car c’est une mission très importante") 
time.sleep(0.5) 
tts.say("Si tout le monde s’entraide et respecte les règles, le monde est un endroit plus agréable pour tous") 
time.sleep(0.5) 

time.sleep(4.785714285714286)

tts.say("Absolument") 
time.sleep(0.5) 
tts.say("Être un bon citoyen, c'est pour tout le monde") 
time.sleep(0.5) 
tts.say("Il suffit de respecter les autres, de participer et d’aider quand on peut") 
time.sleep(0.5) 
tts.say("C’est quelque chose que chaque enfant peut apprendre et faire, que ce soit à la maison, à l'école ou dans sa ville") 
time.sleep(0.5) 

time.sleep(6.357142857142857)

tts.say("Avec plaisir") 
time.sleep(0.5) 
tts.say("N’oubliez pas, chaque petit geste compte pour rendre le monde meilleur") 
time.sleep(0.5) 
tts.say("Continuez d’être curieux et responsables") 
time.sleep(0.5) 

time.sleep(1.7142857142857142)

tts.say("À la prochaine l’équipe") 
time.sleep(0.5) 
tts.say("Continuez d'apprendre et de bien vous comporter") 
time.sleep(0.5) 

time.sleep(1.5)

time.sleep(1.5)

