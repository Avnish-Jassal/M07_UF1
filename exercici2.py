valor = float(input("Introdueix un valor en €: "))

while True:
    iva = float(input("Introdueix l'IVA a aplicar (4, 10 o 21): "))
    if iva == 4 or iva == 10 or iva == 21:
        break
    else:
        print("Per favor, introdueix un IVA correcte (4, 10 o 21).")

valor_iva = valor * (iva / 100)
valor_final = valor + valor_iva

print("Valor original: ", valor, "€")
print("IVA aplicat: ", iva, "%")
print("Valor amb IVA: ", valor_final, "€")