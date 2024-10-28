numero = int(input("Introdueix un numero entre 10 i 100: "))
if 10 <= numero <= 100:
    tupla_numeros = tuple(range(1, numero + 1))
    print("La tupla de números és:", tupla_numeros)
else:
    print("El numero no esta en l'interval especificat.")
