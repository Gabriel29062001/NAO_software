from naoqi import ALProxy

# Connexion au robot
ip = "192.168.x.x"  # Remplacez par l'IP de votre robot
port = 9559
motionProxy = ALProxy("ALMotion", ip, port)

# Active le mode Stiffness pour que les moteurs puissent bouger
motionProxy.setStiffnesses("Body", 1.0)

# Définir les angles de chaque articulation
names = ["RHipPitch", "RKneePitch", "RAnklePitch"]
angles = [-0.5, 1.0, -0.5]  # Exemples d'angles (en radians)
fractionMaxSpeed = 0.2

# Appliquer le mouvement
motionProxy.setAngles(names, angles, fractionMaxSpeed)


