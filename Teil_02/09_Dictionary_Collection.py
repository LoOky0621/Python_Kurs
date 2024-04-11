


meinDict = {"name": "Max", "alter": 30, "stadt": "Berlin"}
print("len(meinDict)")
# Gibt die Anzahl der Schlüssel-Wert-Paare im Dictionary zurück
laenge = len(meinDict)
print(laenge) # 3

print("Wert zum Dictionary hinzufügen")
print('meinDict["beruf"] = "Ingenieur"')
meinDict["beruf"] = "Ingenieur" # Fügt ein neues Schlüssel-Wert-Paar hinzu
print(meinDict) # {'name': 'Max', 'alter': 30, 'stadt': 'Berlin', 'beruf': 'Ingenieur'}

print("Wert im Dictionary aktualisieren")
print('meinDict["alter"] = 31')
meinDict["alter"] = 31 # Aktualisiert den Wert des Schlüssels "alter"
print(meinDict) # {'name': 'Max', 'alter': 31, 'stadt': 'Berlin', 'beruf': 'Ingenieur'}

print("Element aus dem Dictionary entfernen")
print('meinDict.pop("stadt")')
entfernter_wert = meinDict.pop("stadt") # Entfernt den Schlüssel "stadt" und gibt den Wert zurück
print(entfernter_wert) # Berlin
print(meinDict) # {'name': 'Max', 'alter': 31, 'beruf': 'Ingenieur'}

print('meinDict.keys(): gibt eine Liste der Keys zurück')
listOfKeys = meinDict.keys()
print(listOfKeys)

print("Alle Elemente aus dem Dictionary entfernen")
print("meinDict.clear()")
# meinDict.clear() # Entfernt alle Schlüssel-Wert-Paare aus dem Dictionary
print(meinDict) # {}

# Prüfen, ob ein Schlüssel im Dictionary ist
print('"name" in meinDict')
ist_enthalten = "name" in meinDict
print(ist_enthalten) # False

