#ls= [1,3,2,2,5,6]
#lscheck=[2,3,3,6,6,4]

#scrivere una funzione alla quale passerete come parametri ls e lscheck e la funzione deve riportare due valori
#come parametri ls e lscheck e la funzione deve riportare due valori
#il primo: tutte le volte che c'è lo stesso digit
'''
ls= [1,2,5]
lscheck=[2,3,6,6,4]


ls=[1,4,1]
lscheck=[5,5,5,3,6]
uguali=2
diversi=2


ls=[6,6,5]
lscheck=[3,4,4,1,4]
uguali=3
diversi=2
'''

#Genera una lista che contiene N digit casuali tra 1 e N
import random
def GeneraLista(N):
    lista=[]
    for v in range(N):
        lista.append(random.randint(1, N))
    return lista

def ContaUguali(ls, lsCheck):
    contaUguali = 0
    for v in range(len(ls)):
        if ls[v] == lsCheck[v]:
           contaUguali +=1
    return contaUguali

ls      = [1,4,6,8,2,3,3]
lsCheck = [1,4,6,8,9,4,3]
print(ContaUguali(ls, lsCheck))

def ContaUgualiInAltroPosto(ls, lsCheck):
    stessoPosto = 0
    for v in range(len(lsCheck)):
        if ls[v] == lsCheck[v]:
           stessoPosto +=1
           ls[v] = None
           lsCheck[v] = None
    
    altroPosto = 0
    for v in range(len(lsCheck)):
        if lsCheck[v] != None and lsCheck[v] in ls:
            altroPosto += 1
            ls.remove(lsCheck[v])
    return stessoPosto, altroPosto
