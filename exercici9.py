paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

if len(paraula1) < 2 or len(paraula2) < 2:
    print("Error: Ambdues paraules han de tenir almenys dos caràcters.")
else:
    nou_format_paraula1 = paraula2[:2] + paraula1[2:]  # Primeres dues lletres de la segona paraula + resta de la primera
    nou_format_paraula2 = paraula1[:2] + paraula2[2:]  # Primeres dues lletres de la primera paraula + resta de la segona

    print(f"Resultat: {nou_format_paraula1} {nou_format_paraula2}")
