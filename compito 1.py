import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
'''
print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])
'''

# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...


'''
quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1
        
Italia = []
for x in quantiCalciatori:
    if "Italy" in x:
       Italia.append(x)

print(len(Italia))

'''

# 1) contare quanti calciatori hanno giocato per l'Italia
giocatoriItaliani = 0
for player in worldcup:
    if player["ClubCountry"] == "Italy":
        giocatoriItaliani +=1
print("il numeri di giocatori Italiani è: ", giocatoriItaliani)

# 2) contare quanti calciatori hanno giocato per il Brasile
giocatoriBrasiliani = 0
for player in worldcup:
    if player["ClubCountry"] == "Brazil":
        giocatoriBrasiliani +=1
print("il numeri di giocatori Brasiliani è: ", giocatoriBrasiliani)

# 3) contare quanti calciatori hanno giocato per l'Argentina
giocatoriArgentini = 0
for player in worldcup:
    if player["ClubCountry"] == "Argentina":
        giocatoriArgentini +=1
print("il numeri di giocatori Argentini è: ", giocatoriArgentini)

# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
giocatori_Italia_Brasile = 0
for player in worldcup:
    if player["ClubCountry"] == "Italia" and player["ClubCountry"] == "Brazil":
        giocatori_Italia_Brasile +=1
print("il numeri di giocatori che hanno giocato sia in Italia che in Brasile è: ", giocatori_Italia_Brasile)

# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
giocatori_Italia_Argentina = 0
for player in worldcup:
    if player["ClubCountry"] == "Italia" and player["ClubCountry"] == "Argentina":
        giocatori_Italia_Argentina +=1
print("il numeri di giocatori che hanno giocato sia in Italia che in Argentina è: ", giocatori_Italia_Argentina)

# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
calciatore_piu_giovane = ""
eta_piu_giovane = 200
for player in worldcup:
    campionato = player["Year"]
    data_di_nascita = player['DateOfBirth']
    if data_di_nascita:
        anno_di_nascita = int(data_di_nascita.split('-')[0])
        eta = campionato - anno_di_nascita

        if eta < eta_piu_giovane:
            eta_piu_giovane = eta
            calciatore_piu_giovane = player['FullName']
print("Il calciatore più giovane è:", calciatore_piu_giovane)

# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
calciatore_piu_anziano = ""
eta_piu_anziano = 200

if eta > eta_piu_anziano:
            eta_piu_anziano = eta
            calciatore_piu_giovane = player['FullName']
print("Il calciatore più giovane è:", calciatore_piu_anziano)


# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
partecipazioni_giocatori = {}
for player in worldcup:
    full_name = player.get('FullName')
    if full_name:
        partecipazioni_giocatori[full_name] = partecipazioni_giocatori.get(full_name, 0) + 1
giocatore_piu_frequente = max(partecipazioni_giocatori, key=partecipazioni_giocatori.get)

print("Il giocatore che ha partecipato al maggior numero di edizioni della Coppa del Mondo è: ", giocatore_piu_frequente)

# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...