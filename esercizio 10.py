'''
var= 10
nome =0
numero="altro"
ottimo=[1,2,3,4,5]
esempio = ("uno",nome,var, ottimo)
print(esempio)
nome="nome proprio"
print (esempio)
ottimo.append(1000)
print(esempio)
ottimo = 100000
print(esempio)

a=[1,2,3,4]
b=a
a=100
print(b)


a=["uno",[1,2,3]]
b=a
a[1].append(1000)
a="Ciao Ciao"
print(b)

a=[1,2,3]
b=[4,5,6]
c=[a,b]
d=[a,b,c]
a[2]=0
b[1]=1
c[0]=999
print(d)

 
exit(-1)
diz={"nome": var, "cognome": numero, "ottimo": ottimo}
doz = [diz, 1,2,3]
for i in range(7,700,7):
    print(i)
for i in range(9,9999,2):
     print(ottimo[i %len(ottimo)])
infine = [x for x in ottimo]
infine1 = [y * y for x in ottimo for y in range(y, 10 * y, 1)]
'''
'''
import math


a = 10
b = 20
c = 30
'''
# Se a è pari, stampo b+c
# Se a è dispari, stampo b-c

# Per verificare se a è pari
# if a % 2 == 0:

# Secondo modo, con & (and)
"""
010101 & 
000001 = 
==========
000001

010100 & 
000001 = 
==========
000000
"""
# if a & 1 == 0:


#######
# Terzo modo
# if math.floor(a/2)*2 == a:

# Non efficiente ma solo per
# dimostrarvi in quanti modi si
# può fare un calcolo
"""
while a>0:
    a=a-2
if a == 0: #test di parità
"""
"""
# Supponiamo di aver scelto la tecnica con il modulo
a = 10
b = 20
c = 30

if a % 2 == 0:
    print(b + c)
else:
    print(b - c)
"""
'''
#scrivere una funzione ColoreCasuale() che torna una stringa
#casuale tra "rosso","giallo", "verde", "blu", "arancio", "ciano"
import random

def ColoreCasuale():
    Colori = ("rosso","giallo", "verde", "blu", "arancio", "ciano")
    return Colori[random.randint(0, len(Colori) -1)]

print(ColoreCasuale())
'''

#Ricordate che un digit è uno tra 0,1,2,3,4,5,6,7,8,9
#Problema: scrivere una funzione che costruisce una lista
#contenente tutte le possibili combinazioni di quattro

'''
def GeneraListaDigit():
    lista = []
    for i in range(0, 10000):
        s = str(i)
        while len(s) < 4:        #si può usare anche la funzione z.fill(4) 
            s = "0" + s          #che immplementa abbasta zeri a sinistra fino ad avere un numero
        lista.append(s)          #grande quanto il numero nelle parentesi
    return lista 

print(GeneraListaDigit())
'''

#data una stringa numerica (es: "98123"), convertirla in una lista di digit [9,8,1,2,3]
import math
def StringDigitsToList(sd):
    lista=[]
    for i in sd:
        lista.append(int(i))
    return lista


print(StringDigitsToList("9563"))