"""
    Portokosten

    Die Portokosten sind wie folgt festgelegt:
      0 - 39.99€ Bestellwert kosten 3.99€ Porto
     40 - 69.99€ Bestellwert kosten 2.99€ Porto
     70 - 99.99€ Bestellwert kosten 1.99€ Porto
    ab 100€ ist portofrei

    Es soll eine Zufallszahl (bestellwert)
    von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)
    Dann soll ermittelt werden,
    wie hoch die entsprechenden Portokosten sind.
    Am Ende sollen der Bestellwert,
    die Portokosten und der Gesamtbetrag
    ausgegeben werden:
    "Bei einem Bestellwert von 67,54 € betragen die
     Portokosten 2,99 €. Der Gesamtbetrag beträgt somit 70,53 €."
"""

import random

# Funktion zur Berechnung der Portokosten basierend auf dem Bestellwert
def berechne_portokosten(bestellwert):
    if bestellwert < 40:
        return 3.99
    elif 40 <= bestellwert < 70:
        return 2.99
    elif 70 <= bestellwert < 100:
        return 1.99
    else:
        return 0.00

# Hauptprogramm
def main():
    # Erzeuge eine Zufallszahl für den Bestellwert
    bestellwert = round(random.uniform(1.00, 130.00), 2)

    # Berechne die Portokosten
    portokosten = berechne_portokosten(bestellwert)

    # Berechne den Gesamtbetrag
    gesamtbetrag = bestellwert + portokosten

    # Gib die Ergebnisse aus
    print(f"Bei einem Bestellwert von {bestellwert:.2f} € betragen die Portokosten {portokosten:.2f} €. Der Gesamtbetrag beträgt somit {gesamtbetrag:.2f} €.")

if __name__ == "__main__":
    main()
