##test de date 01
import time

now = time.localtime(time.time())
print time.asctime(now)

print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)
 
year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "%04d-%02d-%02d" % (year, month, day)
print "%02d:%02d:%02d" % (hour, minute, second)
print ("Lun", "Mar", "Mer", "Jeu", "Ven", "SAM", "Dim")[weekday], yearday

##test de date 02 simplifier
import datetime #importer la fonction date
datetime.now()  #afficher la date actuel

date = datetime.datetime.now()
       str(date)
print("date")[date.year]))






#from datetime 
#Résultat :
#datetime(2016, 9, 15, 10, 0, 0, 123456)
#datetime.now().time()
#Résultat :
#datetime.time(10, 0, 0, 123456)


#str(datetime.now())