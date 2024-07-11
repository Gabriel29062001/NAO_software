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





time.sleep(2.4285714285714284)

time.sleep(3.2857142857142856)

tts.say("Salut l'équipe") 
time.sleep(0.5) 
tts.say("Vous m'avez tellement manqué") 
time.sleep(0.5) 

time.sleep(3.357142857142857)

tts.say("Aujourd'hui, je vais vous apprendre quelque chose de pas facile pour moi") 
time.sleep(0.5) 

time.sleep(2.0714285714285716)

tts.say("Parce qu'aujourd'hui, je vais vous parler des émotions et, moi, je ne suis pas très bien placé pour parler de ça, car je n'en ai pas") 
time.sleep(0.5) 

time.sleep(6.071428571428571)

tts.say("Je n'ai pas d'émotions car je suis un robot") 
time.sleep(0.5) 
tts.say("Mais je connais beaucoup de choses sur les émotions et je vais tout vous apprendre") 
time.sleep(0.5) 

time.sleep(2.7142857142857144)

tts.say("les émotions, c'est ce que les humains ressentent") 
time.sleep(0.5) 
tts.say("Elles peuvent être agréables, comme la joie et l'amour, ou moins agréables, comme la tristesse et la colère") 
time.sleep(0.5) 
tts.say("Quand vous ressentez une émotion, votre corps réagit aussi") 
time.sleep(0.5) 
tts.say("Par exemple, quand vous êtes stressés, votre cœur bat plus vite, vous respirez plus vite, et vos muscles deviennent tendus") 
time.sleep(0.5) 

time.sleep(13.857142857142858)

tts.say("Quand les enfants font ça, ils ressentent souvent de la frustration ou de la colère") 
time.sleep(0.5) 
tts.say("Ils veulent vraiment le jouet et sont déçus ou en colère parce qu'ils ne l'obtiennent pas") 
time.sleep(0.5) 
tts.say("Parfois, ils peuvent aussi se sentir tristes ou impuissants, ce qui les pousse à exprimer leurs émotions de cette manière") 
time.sleep(0.5) 
tts.say("C’est normal de ressentir ces émotions, mais il est important d’apprendre à les exprimer calmement") 
time.sleep(0.5) 

time.sleep(3.7142857142857144)

tts.say("Quand les enfants sont en colère ou frustrés, leur cerveau réagit") 
time.sleep(0.5) 
tts.say("Une partie du cerveau, appelée l'amygdale, s'active beaucoup") 
time.sleep(0.5) 
tts.say("Cela fait que leur corps libère des hormones de stress") 
time.sleep(0.5) 
tts.say("Leur cœur bat plus vite et ils respirent plus rapidement") 
time.sleep(0.5) 

time.sleep(3.642857142857143)

tts.say("Il est important de parler de ce qu'il nous arrive et de mettre des mots sur nos émotions") 
time.sleep(0.5) 
tts.say("Quand tu te sens frustré ou en colère, essaie de dire ce que tu ressens") 
time.sleep(0.5) 
tts.say("Par exemple, tu pourrais dire : 'Je suis en colère parce que je veux ce jouet'") 
time.sleep(0.5) 
tts.say(" Cela peut t'aider à te sentir mieux et à comprendre ce qui se passe en toi") 
time.sleep(0.5) 

time.sleep(3.7857142857142856)

tts.say("Oh, moi, c'est l'amour") 
time.sleep(0.5) 
tts.say("Parce que quand on ressent de l'amour, tout devient plus lumineux et joyeux") 
time.sleep(0.5) 
tts.say("C'est comme si une chaleur douce envahissait mon cœur, et ça me fait me sentir vraiment bien") 
time.sleep(0.5) 

time.sleep(11.0)

tts.say("De rien, l'équipe") 
time.sleep(0.5) 
tts.say("Je suis toujours là pour vous aider à comprendre et à gérer vos émotions") 
time.sleep(0.5) 
tts.say("N'oubliez pas, c'est normal de ressentir différentes émotions, et il est important de trouver des moyens sains pour les exprimer") 
time.sleep(0.5) 

time.sleep(1.5)

