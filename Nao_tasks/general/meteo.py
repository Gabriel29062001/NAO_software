import requests
import sys
import subprocess


# Récupérer la distance à partir des arguments de la ligne de commande
if len(sys.argv) > 1:
    ROBOT_IP = sys.argv[1]
else:
    print("probleme arguments")


def get_weather(city):
    api_key = "eea603e419c486df5f94454ff1efce3e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr"

    response = requests.get(url)
    
    if response.status_code != 200:
        return None

    data = response.json()
    temperature = data['main']['temp']
    feel_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    return temperature, feel_like, humidity, description

city_name = "Paris"
fichier_output = "/home/gabriel/Documents/nao/nao_softwarev3/Nao_tasks/general/meteo2.py"
temperature, feel_like, humidity, description = get_weather(city_name)
python2_path = "/usr/bin/python2"
subprocess.call([python2_path,fichier_output,str(ROBOT_IP), str(temperature), str(description)])


print(temperature, "°C")
print(feel_like, "°C")
print(humidity, "%")
print(description)
