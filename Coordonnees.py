import requests
import smtplib
import urllib
import geopy
import json

geocode=[]

def get_location():
    lonlat=open('E:\COURS AGTECH POP SCHOOL/lonlatonly.txt', 'r')
    

    for line in lonlat:
        (lon, lat)=line.split(',')
        coord = {'lat':lat.strip(), 'lon':lon}
        geocode.append(coord)
    
    return geocode
    
    
def get_weather():
    api='1b980eb95427e4049b7e9fdd2819958b'
    
    a = 0
        
    for list in geocode:
        
        x = geocode[a]['lon']
        y = geocode[a]['lat']
    
        url='http://api.openweathermap.org/data/2.5/weather?lat='+x+'&lon='+y+'&units=metrics&appid='+api
        weather_r=requests.get(url)
        weather_j=weather_r.json()
        print(weather_j)
        
        a += 1
        

get_location()
get_weather()