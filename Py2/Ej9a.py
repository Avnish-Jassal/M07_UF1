assignatures = ["Matemàtiques", "Català", "Castellà", "Història", "Biologia", "Anglès"]
notes = []
for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes.append(nota)

for i, assignatura in enumerate(assignatures):
    print(f"A {assignatura} ha tret {notes[i]}")
