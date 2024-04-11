"""
Quadratzahlen

Schreibe ein Programm, das alle Quadratzahlen von natürlichen
Zahlen (1, 2, 3, ...) ausgibt, die kleiner als 100 sind.
(Die Quadratzahlen sollen kleiner 100 sein!)

Zusatz: Gib auch die Anzahl der gefunden Quadratzahlen aus
"""
erg = 0
anzahl = 0
for i in range(1, 100, 1):
    erg = i * i
    if erg < 100:
        print(f"{i}:", erg)
        anzahl += 1
    else:
        break
print("Anzahl:", anzahl)
