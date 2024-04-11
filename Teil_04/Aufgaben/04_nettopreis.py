"""
    Nettopreis

    Schreibe Funktionen zum Berechnen des Nettopreises.
    Den Funktionen soll der Bruttopreis übergeben werden
    und sie sollen den Nettopreis zurückgeben.
    Der Mehrwertsteuersatz soll als zweiter Parameter
    übergeben werden können.
    Der Standardwert des Mehrwertsteuersatzes soll 19 sein.
    Der Algorithmus zum Berechnen des Nettopreises soll nur in einer Funktion vorkommen.
"""

# print(berechne_netto_preis(116, 16))  # 100.0
# print(berechne_netto_preis(119))      # 100.0


def berechne_netto_preis(brutto_preis, mehrwertsteuersatz=19):
    """
    Diese Funktion berechnet den Nettopreis basierend auf dem Bruttopreis und dem Mehrwertsteuersatz.

    Args:
        brutto_preis (float): Der Bruttopreis des Produkts.
        mehrwertsteuersatz (float, optional): Der Mehrwertsteuersatz in Prozent. Standardmäßig ist es 19.

    Returns:
        float: Der Nettopreis des Produkts.
    """
    # Berechnung des Nettopreises unter Verwendung der gegebenen Formel
    netto_preis = brutto_preis / (1 + (mehrwertsteuersatz / 100))
    return netto_preis

# Testfälle
print(berechne_netto_preis(116, 16))  # 100.0
print(berechne_netto_preis(119))      # 100.0
