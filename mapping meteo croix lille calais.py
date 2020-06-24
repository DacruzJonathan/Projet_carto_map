import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=croix&appid=1b980eb95427e4049b7e9fdd2819958b""&units=metric"

weather_data = requests.get(url).json()

ville = weather_data['name']

print("Météo à %s" % (ville))
print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")
print(weather_data['main']['pressure'],"HPA")
print(weather_data['clouds']['all'],'nuage')
print(weather_data['weather'][0]['description'])
print("il fait %s" % (weather_data['weather'][0]['description']))

##Lille

url = "http://api.openweathermap.org/data/2.5/weather?q=Lille&appid=1b980eb95427e4049b7e9fdd2819958b""&units=metric"

weather_data = requests.get(url).json()

ville = weather_data['name']

print("Météo à %s" % (ville))
print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")
print(weather_data['main']['pressure'],"HPA")
print(weather_data['clouds']['all'],'nuage')
print(weather_data['weather'][0]['description'])
print("il fait %s" % (weather_data['weather'][0]['description']))

##calais
url = "http://api.openweathermap.org/data/2.5/weather?q=calais&appid=1b980eb95427e4049b7e9fdd2819958b""&units=metric"

weather_data = requests.get(url).json()

ville = weather_data['name']

print("Météo à %s" % (ville))
print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")
print(weather_data['main']['pressure'],"HPA")
print(weather_data['clouds']['all'],'nuage')
print(weather_data['weather'][0]['description'])
print("il fait %s" % (weather_data['weather'][0]['description']))
#####


