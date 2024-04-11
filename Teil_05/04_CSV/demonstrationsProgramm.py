# Importiere die CSVService Klasse
from csvService import CSVService

csv_service = CSVService()

# Ein paar Objekte zum Einfügen
objekt1 = {'id': '1', 'name': 'John Doe', 'alter': '30'}
objekt2 = {'id': '2', 'name': 'Jane Doe', 'alter': '25'}
objekt3 = {'id': '3', 'name': 'Max Mustermann', 'alter': '35'}

# insertObject()
csv_service.insertObject(objekt1)
csv_service.insertObject(objekt2)
csv_service.insertObject(objekt3)

# csv_service.insertObjectAtRow()
neues_objekt = {'id': '4', 'name': 'Neuer Eintrag', 'alter': '22'}
csv_service.insertObjectAtRow(neues_objekt, 0)
#
# getAllObjects()
alle_objekte = csv_service.getAllObjects()
print("Alle Objekte nach dem Einfügen:")
for obj in alle_objekte:
    print(obj)
#
# updateObject()
# objekt2 = {'id': '2', 'name': 'Jane Doe', 'alter': '88'}
objekt2['name'] = "Peter"
csv_service.updateObject(objekt2)
#
# getObjectByRow()
objekt_zeile_2 = csv_service.getObjectByRow(2)
print("\nObjekt an Zeile 2:", objekt_zeile_2)
#
# # deleteObject()
csv_service.deleteObject({'id': '1', 'name': 'John Doe', 'alter': '30'})
