import requests
import config

baseurl='http://api.openweathermap.org/data/2.5/weather?appid='+config.apikey + "&units=metric"


def get_locations():
    geocode=[] 
    lonlatonly=open('lonlatonly.txt', 'r') 
    for line in lonlatonly:
        lon, lat=line.split(',') 
        coord={} 
        coord["lat"]=lon.strip()
        coord["lon"]=lat.strip()
        geocode.append(coord) 
    return geocode 

def display_location(l,titre):
   
    print(titre)
    for item in l:
        print(item, " = ", l[item])

def get_weather(c):
    
    url = baseurl + "&lon="+c["lon"] + "&lat="+c['lat']
    weather=requests.get(url).json()
    c["temp"]=weather['main']['temp']
    return c


def main():
    
    nbligne=0
    locations = get_locations()
    for location in locations :
        location = get_weather(location)
        nbligne=nbligne+1
        sep = "=== LIGNE %d ==="  % nbligne
        display_location(location,sep)


if __name__ == "__main__":
    main()