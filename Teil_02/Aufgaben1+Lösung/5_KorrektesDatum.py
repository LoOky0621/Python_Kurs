"""
Korrektes Datum

Die Meyer GmbH benötigt ein Modul,
das ein Datum auf Korrektheit prüft.
Ist das zu prüfende Datum korrekt,
so ist die Variable datok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02.1999 - datok: 0
29.02.2000 - datok: 1
13.05.2000 - datok: 1
32.05.2000 - datok: 0
24.13.2000 - datok: 0

Für die Jahre gilt: jahr > 1900 && jahr < 2100
"""

# Funktion zur Überprüfung, ob das Datum korrekt ist
def ist_korrektes_datum(tag, monat, jahr):
    if jahr < 1900 or jahr > 2100:  # Überprüfung des Jahres
        return 0
    elif monat < 1 or monat > 12:    # Überprüfung des Monats
        return 0
    elif monat in [1, 3, 5, 7, 8, 10, 12]:  # Monate mit 31 Tagen
        return tag <= 31
    elif monat in [4, 6, 9, 11]:    # Monate mit 30 Tagen
        return tag <= 30
    elif monat == 2:    # Februar - besondere Behandlung für Schaltjahre
        if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
            return tag <= 29
        else:
            return tag <= 28
    else:
        return 0

# Beispiele testen
beispiele = [("29.02.1999", 0), ("29.02.2000", 1), ("13.05.2000", 1), ("32.05.2000", 0), ("24.13.2000", 0)]

for datum, erwartet in beispiele:
    tag, monat, jahr = map(int, datum.split('.'))
    datok = ist_korrektes_datum(tag, monat, jahr)
    print(f"{datum} - datok: {datok}, Erwartet: {erwartet}")
