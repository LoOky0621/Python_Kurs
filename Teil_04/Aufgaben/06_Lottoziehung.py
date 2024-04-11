"""
    Lottoziehung

    Lege in einer Liste (6 aus 49) sich nicht wiederholender eigener Zahlen fest (Lottoschein).
    Erzeuge eine Schleife mit 10.000 Wiederholungen.
    In der Schleife soll eine Liste aus willkürlichen, sich nicht wiederholender Zahlen (6 aus 49)
    erzeugt werden, (Gewinnzahlen) und der Lottoschein mit den Gewinnzahlen verglichen werden
    Lasse dir am Ende des Programms ausgeben wie oft 3, 4, 5 und 6 Elemente der Liste
    übereingestimmt haben.

"""
import random

# Funktion zum Erstellen eines Lottoscheins mit 6 eindeutigen Zahlen
def erstelle_lottoschein():
    return random.sample(range(1, 50), 6)

# Funktion zum Vergleich von zwei Listen und Rückgabe der Anzahl der Übereinstimmungen
def vergleiche_lottoscheine(lottoschein1, lottoschein2):
    return len(set(lottoschein1) & set(lottoschein2))

# Funktion zum Ziehen von Gewinnzahlen
def ziehe_gewinnzahlen():
    return random.sample(range(1, 50), 6)

# Hauptprogramm
def main():
    lottoschein = erstelle_lottoschein()
    ergebnisse = {3: 0, 4: 0, 5: 0, 6: 0}  # Initialisiere einen Zähler für jede Anzahl von Übereinstimmungen

    # Führe 10.000 Lottoziehungen durch
    for _ in range(10000):
        gewinnzahlen = ziehe_gewinnzahlen()
        übereinstimmungen = vergleiche_lottoscheine(lottoschein, gewinnzahlen)

        # Inkrementiere den entsprechenden Zähler basierend auf der Anzahl der Übereinstimmungen
        if übereinstimmungen in ergebnisse:
            ergebnisse[übereinstimmungen] += 1

    # Gib die Ergebnisse aus
    for übereinstimmungen, anzahl in ergebnisse.items():
        print(f"Anzahl der Übereinstimmungen von {übereinstimmungen}: {anzahl}")

if __name__ == "__main__":
    main()
