mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

while True:
    num_mes = int(input("Introdueix un número entre 1 i 12 per veure el mes corresponent o 0 per sortir: "))
    if num_mes == 0:
        print("Fi del programa.")
        break
    elif 1 <= num_mes <= 12:
        print("El mes es:", mesos[num_mes - 1])
    else:
        print("Número no vàlid.")
