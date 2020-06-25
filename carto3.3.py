import requests
import config

baseurl='http://api.openweathermap.org/data/2.5/weather?appid='+config.apikey + "&units=metric"


def get_locations(lonlatonly):
    geocode=[]
    lonlatonly=open(lonlatonly, 'r')
    for line in lonlatonly:
        lon, lat=line.strip(',')
        coord={}
        coord["lat"]=lon.strip()
        coord["lon"]=lat.strip()
        geocode.append(coord)
    return geocode

def get_area(locations):
    lat_min=lat_max=(locations[0]['lat'])
    lon_max=lon_max=(locations[0]['lon'])
    for location in locations:
        lat_min=min(lat_min,(location['lat']))
        lat_max=max(lat_max,(location['lat']))
        lon_min=min(lon_min,(location['lon']))
        lon_max=max(lon_max,(loncation['lon']))
        
    o_lat = ((lat_max - lat_min)/100)*10
    o_lon = ((lon_max - lon_min)/100)*10
    lat_min=lat_min-o_lat
    lat_max=lat_max+o_lat
    lon_min=lon_min-o_lat
    lon_max=lon_max+o_lat
    return {'lat_min':lat_min, 'lat_max':lat_max, 'lon_min':lon_min,'lon_max':lon_max}
    url = baseurl + "&lon="+c["lon"] + "&lat="+c['lat']
    weather=requests.get(url).json()
    print(weather)
    c["temp"]=weather['main']['temp']
    return c
def main():
    locations = get_locations('lonlatonly.txt')
    for location in locations :
        location = get_weather(location)
    area = get_area(locations)
    print_dict(area,"AREA")
    nbligne=0
    
    for location in locations :
        nbligne=nbligne+1
        sep = "LIGNE %d"  % nbligne
        print_dict(location,sep)



if __name__ == "__main__":
    main()