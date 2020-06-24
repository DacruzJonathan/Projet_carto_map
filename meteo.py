import requests 


owm_apik="1b980eb95427e4049b7e9fdd2819958b"

owm_baseurl = "http://api.openweathermap.org/data/2.5/weather?appid="+owm_apik+"&units=metric"


def get_weather(c): 
    lat = c['ltt']
    long= c['lng']
    owm_url=owm_baseurl + "&lat=" + lat +"&lon="+ long
    owm_data = requests.get(owm_url).json() 
    print(owm_data)

def get_locations():
    geocode=[]
    lonlat=open("/home/popschool/python/meteo/lonlatonly.txt","r")
    for line in lonlat:
        lat,lon=line.split(",")
        coord={
            "lng":lon.strip(),
            "ltt":lat
            }
        geocode.append(coord)
    return(geocode)

    
    

coords=get_locations()

print(coords[0]);
get_weather(coords[0])

#print(get_humidity(coords[0]['ltt'],coords[0]['lng']))





