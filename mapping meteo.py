import smopy

import requests

from IPython.display import Image

import matplotlib.pyplot as plt

APIK="1b980eb95427e4049b7e9fdd2819958b""&units=metric"


base_url="http://api.openweathermap.org/data/2.5/weather?"


cities = ["Lille","Croix","calais"]

first=True


for city in cities :


    complete_url = base_url + "appid=" + APIK + "&q=" + city +"&units=metric"

    weather_data = requests.get(complete_url).json()


    print(weather_data)
    print(weather_data['main']['temp'], "°C")
    print(weather_data['main']['humidity'],"%")
    print(weather_data['main']['pressure'],"HPA")
    print(weather_data['clouds']['all'],'nuage')
    print(weather_data['weather'][0]['description'])
    posx=(weather_data['coord']['lon'])

    posy=(weather_data['coord']['lat'])

    if first:

        map = smopy.Map((posy-1, posx-1, posy+1, posx+1),z=8)

        first=False

        ax=map.show_mpl(figsize=(4,4))

    x,y=map.to_pixels(posy,posx)

    ax.plot(x,y,"or",ms=5,mew=2)

    ax.annotate(weather_data['main']['temp'],xy=(x,y),xytext=(3,3),textcoords="offset points")


plt.show()

map.save_png('/home/asthro/Projets/50-Pop/pyt/map.png')

print("Météo à %s" % (ville))
print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")
print(weather_data['main']['pressure'],"HPA")
print(weather_data['clouds']['all'],'nuage')
print(weather_data['weather'][0]['description'])

print("il fait %s" % (weather_data['weather'][0]['description']))



##
#cities = weather_data['name']



#print("il fait %s" % (weather_data['weather'][0]['description']))

##


