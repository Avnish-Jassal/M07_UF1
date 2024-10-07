numero = int(input("Introdueix un número per veure la seva taula de multiplicar: "))

print(f"\nTaula de multiplicar del {numero}:")
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")
