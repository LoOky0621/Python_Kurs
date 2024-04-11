import json
from DataClass import Person  # Stellt sicher, dass dies auf Ihre tatsächliche Datei/Modulstruktur passt
from typing import List

class JSONservice:
    def __init__(self, dateipfad="personen.json"):
        """
        Initialisiert den JSON-Dienst mit dem angegebenen Dateipfad oder erstellt eine neue Datei, wenn keine vorhanden ist.

        Args:
            dateipfad (str): Der Dateipfad, in dem die Daten gespeichert werden sollen. Standardmäßig ist dies "personen.json".
        """
        self.dateipfad = dateipfad
        self._initialisieren()

    def _initialisieren(self):
        """Stellt sicher, dass die Datei existiert, oder erstellt eine neue Datei, wenn keine vorhanden ist."""
        try:
            with open(self.dateipfad, 'r'):
                pass
        except FileNotFoundError:
            with open(self.dateipfad, 'w') as datei:
                json.dump([], datei)

    def insert(self, person):
        """
        Fügt eine Person zur JSON-Datei hinzu.

        Args:
            person (Person): Die Person, die hinzugefügt werden soll.
        """
        daten = self.__lesen()
        person_existiert_bereits = False
        for p in daten:
            if p['id'] == person.id:
                person_existiert_bereits = True
                break

        if not person_existiert_bereits:
            daten.append(person.toJson())
            self.__schreiben(daten)

    def update(self, person):
        """
        Aktualisiert die Daten einer Person in der JSON-Datei.

        Args:
            person (Person): Die aktualisierte Person.
        """
        daten = self.__lesen()
        for i, p in enumerate(daten):
            if p['id'] == person.id:
                daten[i] = person.__dict__
                break
        self.__schreiben(daten)

    def delete(self, person):
        """
        Löscht eine Person aus der JSON-Datei.

        Args:
            person (Person): Die zu löschende Person.
        """
        daten = self.__lesen()
        daten = [p for p in daten if p['id'] != person.id]
        self.__schreiben(daten)

    def getAllPersons(self):
        """
        Ruft alle Personen aus der JSON-Datei ab.

        Returns:
            List[Person]: Eine Liste aller Personen.
        """
        daten = self.__lesen()
        return [Person(d['id'], d['name'], d['alter']) for d in daten]

    def __lesen(self):
        """Liest Daten aus der JSON-Datei."""
        with open(self.dateipfad, 'r', encoding='utf-8') as datei:
            return json.load(datei)

    def __schreiben(self, daten):
        """Schreibt Daten in die JSON-Datei."""
        with open(self.dateipfad, 'w', encoding='utf-8') as datei:
            json.dump(daten, datei)
