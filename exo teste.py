n = int(input("entrez une valeur n : "))
for i in range(1,n+1):
    if(n%i==0):
        print("Le nombre ",i," est un diviseur de  ",n)

u= int(input("entre un nombre u"))
j=0
for i in range(1,u+1):
    j = j*i
    print("fact de u est :",u," = :",j)



rayon = int(input("rayon= :"))
aire = math.pi * rayon * rayon; #R*R*3.14
circonference = 2 * math.pi * rayon;
diametre = 2*rayon;

print("le diametre =", diametre)
print("aire d'un cercle =", aire)
print("circonference est = :", circonference)
print("le rayon =", rayon)

