import math
π = 3.1415     #assegno il vale di pi
r1 = 30        #assegno il valore del raggio del primo cerchio
r2 = 45        #assegno il valore del raggio del secondo cerchio
r3 = 33        #assegno il valore del raggio del terzo cerchio
h = 130        #assegno il valore dell'altezza
S1 = π*r1**2   #calcolo l'area del primo cerchio
S2 = π*r2**2   #calcolo l'area del secondo cerchio
S3 = π*r3**2   #calcolo l'area del terzo cerchio
V = (1/6)* h*(S1 + 4*S2 + S3) #calcolo il volume della botte
liters = V / 1000 #converto il volume da cm3 in litri
print(liters)  #stampo il valore del volume in litri
A = 2*π*((r1 + r2)/2)*h + π*(r1**2 + r2**2)/2 #calcolo l'area totale del cilindro (botte)
print(A) #stampo il valore dell'area
