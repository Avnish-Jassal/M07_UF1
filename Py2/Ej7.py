contactes = {}
while True:
    nom = input("Introdueix un nom (o escriu 'no' per sortir): ")
    if nom.lower() == 'no':
        break
    edat = int(input(f"Introdueix l'edat de {nom}: "))
    if nom not in contactes:
        contactes[nom] = edat
    else:
        print("Aquest nom ja existeix. No s'ha afegit al diccionari.")
print("Diccionari de contactes:", contactes)
