from naoqi import ALProxy

# Adresse IP et port du robot NAO
NAO_IP = "192.168.55.60"  # Remplace par l'adresse IP de ton robot NAO
NAO_PORT = 9559

# Connexion au proxy ALAudioDevice
audioProxy = ALProxy("ALAudioDevice", NAO_IP, NAO_PORT)

# Récupérer le volume actuel
current_volume = audioProxy.getOutputVolume()
print(f"Le volume actuel est : {current_volume}%")

# Définir un nouveau volume (par exemple 70%)
new_volume = 70
audioProxy.setOutputVolume(new_volume)

# Vérifier que le volume a été changé
new_set_volume = audioProxy.getOutputVolume()
print(f"Le nouveau volume est : {new_set_volume}%")
