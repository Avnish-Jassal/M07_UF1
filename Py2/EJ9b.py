assignatures = ["Matemàtiques", "Català", "Castellà", "Història", "Biologia", "Anglès"]
notes = {}
for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes[assignatura] = nota

for assignatura, nota in notes.items():
    print(f"A {assignatura} ha tret {nota}")
