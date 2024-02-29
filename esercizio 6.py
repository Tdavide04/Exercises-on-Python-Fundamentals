import random  #importo random

#sapendo che la funzione random.randint(start, end)
#genera un numero intero compreso tra start e end, end compreso,
#costruire una lista di numeri casuali lunga 100 e
#stampare la somma di tutti i suoi numeri

lista = [] #creo la lista
for i in range (101): #creo un ciclo for generando un centinaio di numeri
    lista_random = random.randint (1, 10) #genero una lista di numeri casuali tra 1 e 10 #randint è l'uncio che include l'estremo destro 
    lista.append(lista_random) #aggiungo i numeri casuali alla lista creata 
somma = sum(lista) #faccio la somma
print(somma)