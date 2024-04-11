"""
- Veränderbar (mutable).
- Kann verschiedene Datentypen enthalten.
- Unterstützt Duplikate.
- Geeignet für Daten, die änderbar sein sollen.
"""

meineListe = [1, 5, 2, 3, 4, 5]
print("len(meineListe)")
# Gibt die Anzahl der Elemente in der Liste zurück
laenge = len(meineListe)
print(laenge) # 5

print("Element zur Liste hinzufügen")
print("meineListe.append(6)")
meineListe.append(6) # Fügt das Element 6 am Ende der Liste hinzu
print(meineListe) # [1, 2, 3, 4, 5, 6]

print("Mehrere Elemente zur Liste hinzufügen")
print("meineListe.extend([7, 8, 9])")
meineListe.extend([7, 8, 9]) # Fügt mehrere Elemente am Ende der Liste hinzu
print(meineListe) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Element an spezifischer Position einfügen")
print("meineListe.insert(0, 0)")
meineListe.insert(0, 0) # Fügt das Element 0 an der Position 0 ein
print(meineListe) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# achtung veraltet
print("Element aus der Liste entfernen")
print("meineListe.remove(9)")
meineListe.remove(9) # Entfernt das erste Vorkommen des Elements 9 aus der Liste
# meineListe.remove(9) # Programm bricht ab
print(meineListe) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print("Element an spezifischer Position entfernen und zurückgeben")
print("meineListe.pop(0)")
entferntes_element = meineListe.pop(0) # Entfernt und gibt das Element an der Position 0 zurück
print(meineListe) # [1, 2, 3, 4, 5, 6, 7, 8]

print("Alle Elemente aus der Liste entfernen")
print("meineListe.clear()")
meineListe.clear() # Entfernt alle Elemente aus der Liste
print(meineListe) # []

# Prüfen, ob ein Element in der Liste ist
print("5 in meineListe")
ist_enthalten = 5 in meineListe
print(ist_enthalten) # False


#contains
print(meineListe.__contains__(1))
print(meineListe.__contains__(1231654))
