numero = "1"
while True:
    c = input("Digita 0-9,+-/=: ")
    if len(c) > 0:
        c = c[0]

    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        print("Il numero è: ", numero)
        
    if c == "," and numero.count(",")>=1:
        print("Errore")
        break
    else:
        # costruzione del numero...
        numero = numero + c