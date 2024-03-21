#Esempio 1
#Leggere da input una stringa, se minore di "lettera", stampare la stringa "minore", se maggiore di 
#"lettera" e minore di "tocco", stampare "intermedia", se maggiore di "tocco" e minore di "what" 
#stampare "maggiore", altrimenti stampare "massima"

'''
a = 10
b = 20
if a > b:
    print(a - b)
else:
    print(b - a)

# potrei avere
if a > b:
    print("maggiore")


# un if "breve" si può mettere sulla stessa riga. "breve" significa che c'è un solo statement dopo if
if a > b:
    print("maggiore")

# Analogamente se ho sia then, sia else con un solo statement
print(a - b) if a > b else print(b - a)


# Infine, se ho più di un if in sequenza allora posso utilizzare elif come parola chiave
if a > b:
    print(a - b)
elif a == b:
    print("Sono uguali")
elif a < b:
    print(b - a)
else:
    print("non so più cosa scrivere")


def EmettiTicket():
    pass


def EliminaTicket():
    pass

'''

# Leggere da un file (persone.txt) i nomi, cognomi e età di un gruppo di persone,
# organizzarli in un dizionario la cui chiave è il cognome e il cui valore è una tupla contenente i tre valori letti.

# Per prima cosa leggere il file persone.csv e stampare, riga per riga:
# Nome: xxx, Cognome: xxxx, Eta: xxx
# esempio: Nome: Mario, Cognome: Rossi, Eta: 35

fin = open("persone.txt", "r")
persone = fin.readlines()
fin.close

lista = []
for x in persone:
    lista.append(x.split(","))

'''
lista1=lista[0]
lista2=lista[1]
lista3=lista[2]
lista4=lista[3]

Nome = "Nome: ", lista1[0]
Cognome = "Cognome: ", lista1[1]
Età = "Età: ", lista1[2]
print(Nome, Cognome, Età)

'''

Nome = []
for x in lista:
    Nome.append(x[0])
Cognome = []
for x in lista:
    Cognome.append(x[1])
Età = []
for x in lista:
    Età.append(x[2])

for i in range(len(Nome)):
    print("Nome: " + Nome[i]+ ", "+"Cognome: " + Cognome[i]+", "+"Età: "+Età[i])