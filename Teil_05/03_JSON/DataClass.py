import json
from typing import List

class Person:
    def __init__(self, id: int, name: str, alter: int):
        """Initialisiert eine Person mit ID, Name und Alter."""
        self.id = id
        self.name = name
        self.alter = alter

    def __str__(self):
        """Gibt eine lesbar formatierte Zeichenfolge der Person zurück."""
        return f"Person id:{self.id}, name:{self.name}, alter:{self.alter}"

    def toJson(self) -> str:
        """Konvertiert die Person in ein JSON-Format."""
        return {
            'id': self.id,
            'name': self.name,
            'alter': self.alter
        }

    @staticmethod
    def fromJson(json_str: str) -> 'Person':
        """
        Erstellt eine Person aus einem JSON-String.
        
        Args:
            json_str (str): Der JSON-String mit den Personendaten.
        
        Returns:
            Person: Die erstellte Person.
        """
        daten = json.loads(json_str)
        return Person(daten['id'], daten['name'], daten['alter'])
