
"""
- Unveränderbar (immutable).
- Kann verschiedene Datentypen enthalten.
- Unterstützt Duplikate.
- Geeignet für Daten, die nicht geändert werden sollen.
"""

meinTupel = (1, 2, 3, 4, 5)
print("len(meinTupel)")
# Gibt die Anzahl der Elemente im Tupel zurück
laenge = len(meinTupel)
print(laenge) # 5

print("Zugriff auf Elemente im Tupel")
print("meinTupel[0]")
# Zugriff auf das erste Element im Tupel
erstes_element = meinTupel[0]
print(erstes_element) # 1

print("Tupel können Duplikate enthalten")
dupTupel = (1, 2, 2, 3, 4)
print(dupTupel) # (1, 2, 2, 3, 4)

print("Tupel-Verkettung")
neuesTupel = meinTupel + dupTupel # Verkettet zwei Tupel
print(neuesTupel) # (1, 2, 3, 4, 5, 1, 2, 2, 3, 4)

print("Elemente in Tupel zählen")
# Zählt, wie oft das Element 2 im Tupel vorkommt
anzahl = dupTupel.count(2)
print(anzahl) # 2

print("Index eines Elements im Tupel finden")
# Findet den Index des ersten Vorkommens des Elements 3
index = meinTupel.index(3)
print(index) # 2

# Prüfen, ob ein Element im Tupel ist
print("5 in meinTupel")
ist_enthalten = 5 in meinTupel
print(ist_enthalten) # True
