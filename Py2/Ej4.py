numeros = input("Introdueix 10 números separats per espais: ")
tupla_numeros = tuple(sorted(map(int, numeros.split())))
print("Tupla ordenada:", tupla_numeros)
