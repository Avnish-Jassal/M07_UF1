abecedari = list("abcdefghijklmnopqrstuvwxyz")

abecedari_filtrat = [lletra for index, lletra in enumerate(abecedari) if (index + 1) % 3 != 0]

tupla_abecedari = tuple(abecedari_filtrat)

print("Llista resultant:", abecedari_filtrat)
print("Tupla resultant:", tupla_abecedari)
