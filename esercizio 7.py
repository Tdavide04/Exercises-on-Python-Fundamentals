#Costruire due liste, la prima che contiene i numeri pari fino a 1000
#la seconda che contiene i numeri dispari fino a 1000
#a partire dalle prime due liste,
#costruire una terza lista che contiene prima tutti i pari e poi tutti i dispari

lista_1 = []
for n in range(2, 1001, 2):
    lista_1.append(n)
lista_2 = []
for n in range(1, 1000, 2):
    lista_2.append(n)

lista_3 = lista_1 + lista_2
print(lista_3)