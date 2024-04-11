from DataClass import Person
from JSONservice import JSONservice

service = JSONservice()

# Daten einfügen
person1 = Person(2, "Magdalena Veronika", 29)
service.insert(person1)
print(person1)

# Daten aktualisieren
person1.alter=88
person1.name ="Anna"
service.update(person1)
print(person1)

# # Daten abrufen
alle_personen = service.getAllPersons()
for person in alle_personen:
    print(person)

# Daten löschen
service.delete(person1)
