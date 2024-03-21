#generare un milione di numeri randomici
#farne la somma e la media

import random #importo random
lista = [] #genero la lista
for i in range(1000001): #creo un ciclo for generando un milione di numeri (1 finale serve per rendere un milione incluso)
  lista_random = random.randint(1, 1000001) #rendo i numeri generati randomici
  lista.append(lista_random) #aggiungo i numeri randfomici nella lista
somma = sum(lista) #faccio la somma
print (somma)
media = somma / 1000000 #faccio la media
print (media)