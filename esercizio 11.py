#Problema: ho la stringa "123", la voglio trasformare in [1, 2, 3]
#definire una funzione che risolva il problema
'''
import math
def Converti(s):
    if usaMetodo1:
        #metodo 1 (Comprension)
        return [int(i) for i in s]
    else:
        #metodo 2 (for)
        lista=[]
        for i in s:
           lista.append(int(i))
        return lista

print (Converti("123"))

###########################

fin = open("alice.txt", "r")                                                  #si possono aprire i file in 3 modi: "r" read = solo lettura,
linee =fin.readlines()                                                        #"a" append = appendere ad un altro file,
fin.close()                                                                   #"w" write = scrivere e modificare
# readlines legge tutti i caratteri incluso il carattere a capo(eol/eoln)
#come faccio a togliere queste linee?
l1 = []
for l in linee:
    l1.append(
        l.strip()
    ) #elimina spazi, tab e eol ma solo a inizio e fine della stringa
linee = l1
print(linee)


s ="alfa;beta;gamma"
# Come posso ottenere la lista ["alfa", "beta", "gamma"]?
print(s.split(";"))
'''
# Dato alice.txt, stampare, una per riga, tutte le parole che la compongono
'''
fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
l1 = []
for l in linee:
    l1.append(
      l.strip()
    )

linee = l1
parole = []
for l in linee:
    parole.append(
        l.split(" ")
    )
print(parole)


# Data una lista di stringhe, eliminare dalla lista tutte le stringhe vuote
ls = ["uno", "", "due", "tre", "", "", "", " ", "  ", "fine"]
lista=[]
#primo metodo (aggiunge solo i caratteri lunghi piu di 1)
for i in ls:
    if len(i)>0:
        lista.append(i)

#secondo metodo (aggiunge solo caratteri non vuoti)
for i in ls:
    if len(i.strip())>0:
        lista.append(i)

print(lista)

'''

# Contare quanti caratteri ci sono in alice.txt
# Contare quanti caratteri non spazi bianchi ci sono in alice.txt
# Contare quanti caratteri alfanumerici [a-zA-Z0-9] ci sono in alice.txt

fin = open("alice.txt", "r")
linee = fin.read()
fin.close()
Caratteri = len(linee)

print(Caratteri)

linee1 = []
for i in linee:
    if len(i.strip())>0:
        linee1.append(i)
SenzaSpazi = len(linee1)

print(SenzaSpazi)

linee2 = []
for i in linee:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        linee2.append(i)
Alfanumerici = len(linee2)

print(Alfanumerici)