import urllib
import webbrowserdef Spam_tout_le_monde():
    a = 0
    while (a != 9):
        ap = str(a)
        b = 0        while (b != 100):
            page=urllib.urlopen('http://192.168.1.200:187'+ap+'/T/Tu te fais spam')
            b += 1        a += 1def Spam_une_personne():    a = input('Quelle personne voulez voue Spam ? : ')
    a = str(a)
    b = 0    while (b != 100):
        page=urllib.urlopen('http://192.168.1.200:187'+a+'/T/Tu te fais spam')
        b += 1print('Choix 1 --> Spam une seule personne')
print('Choix 2 --> Spam tout le monde')
print('')
var = input('Quelle est votre choix ?')if (var == 1):
    Spam_une_personne()
if (var == 2):
    Spam_tout_le_monde()if (var != 1):
    if (var != 2):
        print("Choix invalide")