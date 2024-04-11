import csv
import os


class CSVService:
    def __init__(self, dateipfad="test.csv"):
        """
        Initialisiert den CSV-Service mit dem angegebenen Dateipfad oder erstellt eine neue CSV-Datei, wenn keine vorhanden ist.

        Args:
            dateipfad (str): Der Dateipfad, in dem die CSV-Daten gespeichert werden sollen. Standardmäßig ist dies "test.csv".
        """
        # Ermittle den Pfad des Verzeichnisses der aktuellen Datei
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Kombiniere den Verzeichnispfad mit dem Dateinamen
        self.dateipfad = os.path.join(current_dir, dateipfad)

        # Stelle sicher, dass die Datei existiert, sonst erstelle eine leere Datei
        if not os.path.exists(self.dateipfad):
            with open(self.dateipfad, mode='w') as file:
                pass

    def getObjectByRow(self, row):
        """
        Ruft das Objekt aus der CSV-Datei anhand der angegebenen Zeilennummer ab.

        Args:
            row (int): Die Zeilennummer, aus der das Objekt abgerufen werden soll.

        Returns:
            dict: Das Objekt als Wörterbuch.
        """
        with open(self.dateipfad, mode='r') as datei:
            reader = csv.DictReader(datei)
            for i, obj in enumerate(reader):
                if i == row:
                    return obj
        return None

    def getObjectByKeyValue(self, key, value):
        """
        Ruft das Objekt aus der CSV-Datei anhand des angegebenen Schlüssel-Wert-Paares ab.

        Args:
            key (str): Der Schlüssel des zu suchenden Werts.
            value (str): Der Wert, nach dem gesucht werden soll.

        Returns:
            dict: Das gefundene Objekt als Wörterbuch.
        """
        with open(self.dateipfad, mode='r') as file:
            reader = csv.DictReader(file)
            for obj in reader:
                if obj.get(key) == value:
                    return obj
        return None

    def getAllObjects(self):
        """
        Ruft alle Objekte aus der CSV-Datei ab.

        Returns:
            list: Eine Liste aller Objekte als Wörterbücher.
        """
        objects = []
        with open(self.dateipfad, mode='r') as file:
            reader = csv.DictReader(file)
            objects = [row for row in reader]
        return objects

    def updateObject(self, object):
        """
        Aktualisiert ein Objekt in der CSV-Datei.

        Args:
            object (dict): Das zu aktualisierende Objekt als Wörterbuch.
        """
        objects = self.getAllObjects()
        updated = False
        for i, obj in enumerate(objects):
            if obj['id'] == object['id']:  # Annahme: Jedes Objekt hat eine eindeutige ID
                objects[i] = object
                updated = True
                break
        if updated:
            self.__overWriteFile(objects)

    def insertObject(self, object):
        """
        Fügt ein Objekt der CSV-Datei hinzu.

        Args:
            object (dict): Das hinzuzufügende Objekt als Wörterbuch.
        """
        with open(self.dateipfad, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=object.keys())
            if file.tell() == 0:  # Datei ist leer, schreibe Header
                writer.writeheader() # Wenn ihr mit existierenden Dateien arbeitet, ist das nicht erforderlich
            writer.writerow(object)

    def insertObjectAtRow(self, object, row):
        """
        Fügt ein Objekt an einer bestimmten Zeile in der CSV-Datei ein.

        Args:
            object (dict): Das hinzuzufügende Objekt als Wörterbuch.
            row (int): Die Zeilennummer, an der das Objekt eingefügt werden soll.
        """
        objects = self.getAllObjects()
        objects.insert(row, object)
        self.__overWriteFile(objects)

    def deleteObject(self, object_to_delete):
        """
        Löscht ein Objekt aus der CSV-Datei.

        Args:
            object_to_delete (dict): Das zu löschende Objekt als Wörterbuch.
        """
        all_objects = self.getAllObjects()
        new_objects = []
        for obj in all_objects:
            if obj != object_to_delete:
                new_objects.append(obj)
        self.__overWriteFile(new_objects)

    def __overWriteFile(self, objects):
        """
        Überschreibt die CSV-Datei mit den angegebenen Objekten.

        Args:
            objects (list): Eine Liste von Objekten als Wörterbücher.
        """
        with open(self.dateipfad, mode='w') as file:
            if len(objects) > 0:
                writer = csv.DictWriter(file, fieldnames=objects[0].keys())
                writer.writeheader()
                writer.writerows(objects)
