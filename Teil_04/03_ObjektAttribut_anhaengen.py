# Definition der Klasse Pizza
class Pizza:
    # Konstruktor, der beim Erstellen einer Instanz aufgerufen wird
    def __init__(self, belagParam, durchmesserParam):
        # Initialisierung der Instanzattribute mit den übergebenen Parametern
        self.belag = belagParam
        self.durchmesser = durchmesserParam

    # Methode, um Informationen über die Pizza auszugeben
    def info(self):
        return f"Ich bin eine Pizza. Mein Belag ist {self.belag}, mein Durchmesser ist {self.durchmesser}"

# Erstellen von Instanzen der Pizza-Klasse mit unterschiedlichen Attributwerten
pizza1 = Pizza("Fungi", 48)
pizza2 = Pizza("Hawaii", 20)

# Zugriff auf die Attributwerte der Instanz pizza1 und Ausgabe der Informationen über die Pizza
print(pizza1.belag)
print(pizza1.durchmesser)
print(pizza1.info())

# Einem Objekt ein neues Attribut anhängen
print("Einem Objekt ein Attribut anhängen")
pizza1.temperatur = "heiß"
print(pizza1.temperatur)
# Dieses Attribut ist nur für das Objekt pizza1 verfügbar
# print(pizza2.temperatur) # AttributeError: 'Pizza' object has no attribute 'temperatur'
