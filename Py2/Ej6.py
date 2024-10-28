areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element:", areas_pis[1])
print("Últim element:", areas_pis[-1])
print("Àrea de la terrassa:", areas_pis[7])
print("Del primer al tercer element:", areas_pis[:3])
print("Del tercer a l'últim element:", areas_pis[2:])
area_habitacions = areas_pis[5] + areas_pis[13]
print("Àrea total de les dues habitacions:", area_habitacions)

areas_pis[9] = 8.5  # Nova area del lavabo
areas_pis.extend(["Pati interior", 2.78])
print("Llista amb modificacions:", areas_pis)

# Càlcul del total de l'àrea del pis
total_area = sum(areas_pis[i] for i in range(1, len(areas_pis), 2))
print("Àrea total del pis:", total_area)
