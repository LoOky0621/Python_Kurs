"""
Teilersumme

    Dein Ziel ist es, ein Skript zu schreiben, das eine Zahl nimmt und überprüft,
    ob die Summe aller Teiler dieser Zahl kleiner als die Zahl selbst ist.
    Beachte dabei, dass die Zahl selbst nicht als Teiler zählt.

    Beispiel 1:
    Bei der Zahl 81 sollte dein Programm "True" ausgeben, da die Summe der Teiler
    (1 + 3 + 9 + 27) gleich 40 ist, und 40 ist kleiner als 81.

    Beispiel 2:
    Bei der Zahl 80 sollte dein Programm "False" ausgeben, da die Summe der Teiler
    (1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40) gleich 106 ist, und 106 ist nicht kleiner als 80.
"""

eingabe = input("Bitte eine Zahl eingeben: ")
zahl = int(eingabe)
summe_teiler = 0

# Schleife, um die Teilersumme zu berechnen
for i in range(1, zahl):
    if zahl % i == 0:  # Überprüfen, ob i ein Teiler von zahl ist
        summe_teiler += i

# Vergleich, ob die Teilersumme kleiner als die Zahl selbst ist
if summe_teiler < zahl:
    print(f"Die Summe der Teiler ({summe_teiler}) ist kleiner als {zahl} = TRUE")
else:
    print(f"Die Summe der Teiler ({summe_teiler}) ist größer als {zahl} = FALSE")
