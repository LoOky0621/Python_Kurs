"""
Kosten kalkulieren

Erstelle einen Codeabschnitt, der die Gesamtkosten anhand des Einzelpreises,
der Anzahl der Artikel und der Währung ermittelt. Der Einzelpreis und die Währung
sollen als Variable im Code definiert werden. Die Standardanzahl der
Artikel soll 100 sein, und die Standardwährung soll Euro sein.
Das Ergebnis soll so formatiert sein, dass es zwei Dezimalstellen enthält.
"""
def user_input() -> (float, str):
    einzelpreis = float(input("Bitte geben Sie den Einzelpreis des Artikels ein: "))
    waehrung = input("Bitte geben Sie die Währung ein (Standard ist Euro): ")
    return einzelpreis, waehrung


def berechne_gesamtkosten(einzelpreis: float, waehrung: str, anzahl_artikel: int = 100) -> str:
    gesamtkosten = einzelpreis * anzahl_artikel
    return f"{gesamtkosten:.2f} {waehrung}"



einzelpreis, waehrung = user_input()
print(berechne_gesamtkosten(einzelpreis, waehrung))