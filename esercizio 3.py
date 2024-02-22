#consegna
# In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
# antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
# le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
# john, alice, mary
# altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
# stampare l'elenco delle persone presenti
# per generare un numero casuale tra 10 e 20, 20 incluso: random.randint(10, 20)
# per generare un numero casuale tra 0 e 1: random.random()

stanza = ["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"] #definisco tutti i componenti della lista
stanza = stanza[2:] #impongo alla lista di escludere i primi due elemnti
stanza.extend (["john", "alice", "mary"]) #espando la lista
stanza = stanza[2:] ##impongo alla lista di escludere i primi due elemnti
stanza.sort() #metto in ordine alfabetico gli elementi della lista
print (stanza)

#stanza.remove non funziona
#per tolgliere elementi devo usare stanza[2:]