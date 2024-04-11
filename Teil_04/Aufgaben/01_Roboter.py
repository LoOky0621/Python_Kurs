"""
Wir haben die folgende einfache Roboterklasse in Python:

class Roboter:
    def __init__(self, name):
        self.name = name


Diese Klasse ist plötzlich weltweit sehr beliebt geworden. Wir haben jedoch ein Problem:
Die internationale Robotergewerkschaft hat ein weltweites Verbot durchgesetzt, dass Roboter nicht mehr "Bernd" genannt werden dürfen.
Ändere nun die Klasse so ab, dass Roboter automatisch "Herbert" genannt werden, wenn jemand versucht,
sie "Bernd" zu taufen oder einen Roboter in "Bernd" umzubenennen.
Die Benutzer der Klasse sollten keine Änderungen bemerken, außer dass jetzt zweimal "Herbert" ausgegeben wird, wenn:

roboter_x = Roboter("Herbert")
roboter_y = Roboter("Bernd")
print(roboter_x.name + " und " + roboter_y.name)

Bitte teste auch das Umbenennen. Nach dem Versuch, einen Roboter in „Bernd” umzubenennen,
sollte der Name des Roboters „Herbert” sein:

roboter_z = Roboter("Stefan")
roboter_z.name = "Bernd"
print(roboter_z.name)  # Herbert
"""
class Roboter:
    alle_Roboter = []  # Liste aller Roboter

    def __init__(self, name):
        if name == "Bernd":  # Wenn der Name Bernd ist, ändere ihn in Herbert
            self.name = "Herbert"
        else:
            self.name = name
        Roboter.alle_Roboter.append(self)  # Füge den Roboter zur Liste aller Roboter hinzu

    @classmethod
    def ausgabe_gesamt(cls):
        for robo in cls.alle_Roboter:
            print(robo)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "Bernd":  # Wenn jemand versucht, den Namen auf Bernd zu setzen, ändere ihn wieder in Herbert
            self._name = "Herbert"
        else:
            self._name = value

    def __str__(self):
        return self.name


# Test
roboter_x = Roboter("Herbert")
roboter_y = Roboter("Bernd")
roboter_z = Roboter("Thorsten")

Roboter.ausgabe_gesamt()
print()

# Testen der Namensänderung
roboter_z.name = "Bernd"  # Versuche, den Namen von Thorsten in Bernd zu ändern
print(roboter_z)  # Der Name sollte automatisch wieder zu Herbert geändert werden
