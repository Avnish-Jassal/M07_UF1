numero = int(input("Introdueix un número entre 1 i 10: "))
if 1 <= numero <= 10:
    taula_multiplicar = tuple(numero * i for i in range(1, 11))
    print("La taula de multiplicar de", numero, "és:", taula_multiplicar)
else:
    print("Numero fora de l'interval.")
