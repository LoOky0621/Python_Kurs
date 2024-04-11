"""
Zwei Zahlen genau vergleichen

Schreibe ein Programm, das zwei zufällige Zahlen erzeugt.
Dann soll das Programm testen und ausgeben,
welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
"""
import random

zufallszahl1 = random.randint(1, 10)
zufallszahl2 = random.randint(1, 10)

print("Zahl1:", zufallszahl1)
print("Zahl1:", zufallszahl2)


if zufallszahl1 < zufallszahl2:
    print("Zahl",zufallszahl2,"ist größer")
elif zufallszahl1 > zufallszahl2:
    print("Zahl",zufallszahl1,"ist größer")
elif zufallszahl1 == zufallszahl2:
    print("Beide sind gleich groß")


