"""
Kleinste von drei UNTERSCHIEDLICHEN Zahlen

Schreibe ein Programm,
das drei Variablen mit zufälligen,
UNTERSCHIEDLICHEN Zahlen (aus dem gleichen Zahlenraum) befüllt.
Dann soll das Programm testen,
welche der Zahlen die Kleinste ist und diese ausgeben.
"""

import random

# Zufällige, unterschiedliche Zahlen generieren
zahl1 = random.randint(1, 100)
zahl2 = random.randint(1, 100)
while zahl2 == zahl1:  # sicherstellen, dass zahl2 von zahl1 unterschiedlich ist
    zahl2 = random.randint(1, 100)
zahl3 = random.randint(1, 100)
while zahl3 == zahl1 or zahl3 == zahl2:  # sicherstellen, dass zahl3 von zahl1 und zahl2 unterschiedlich ist
    zahl3 = random.randint(1, 100)

# Ausgabe der generierten Zahlen
print("Die generierten Zahlen sind:", zahl1, zahl2, zahl3)

# Kleinste Zahl ermitteln und ausgeben
kleinste = min(zahl1, zahl2, zahl3)
print("Die kleinste Zahl ist:", kleinste)
