import pickle

# Beispielklasse
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# # Ein Person-Objekt erstellen
# person = Person("Max Mustermann", 30)
#
# # Objekt serialisieren und in einer Datei speichern
# with open('person.pkl', 'wb') as datei:
#     pickle.dump(person, datei)

# Objekt aus Datei deserialisieren
with open('person.pkl', 'rb') as datei:
    # Laden des gespeicherten Objekts
    geladene_person = pickle.load(datei)

# Ausgabe der geladenen Personendaten
print(f'Name: {geladene_person.name}, Alter: {geladene_person.alter}')
