valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

operacio = input("Introdueix l'operació que vols realitzar (+, -, *, /): ")

if operacio == "+":
    resultat = valor1 + valor2
    print(f"La suma de {valor1} i {valor2} és: {resultat}")
elif operacio == "-":
    resultat = valor1 - valor2
    print(f"La resta de {valor1} menys {valor2} és: {resultat}")
elif operacio == "*":
    resultat = valor1 * valor2
    print(f"La multiplicació de {valor1} per {valor2} és: {resultat}")
elif operacio == "/":
    if valor2 != 0:
        resultat = valor1 / valor2
        print(f"La divisió de {valor1} entre {valor2} és: {resultat}")
    else:
        print("Error: No es pot dividir per zero.")
else:
    print("Operació no vàlida.")
