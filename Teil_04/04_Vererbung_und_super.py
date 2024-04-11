# Definition der Basisklasse Animal
class Animal:
    # Konstruktor, der beim Erstellen einer Instanz aufgerufen wird
    def __init__(self, name):
        self.name = name

    # Methode, um zu zeigen, dass das Tier atmet
    def breath(self):
        print(f"{self.name} atmet")

# Definition der erbenden Klasse Dog, die von Animal erbt
class Dog(Animal):
    # Konstruktor, der den Konstruktor der Basisklasse aufruft und den Namen des Hundes setzt
    def __init__(self, name):
        super().__init__(name)

# Erstellen von Instanzen der Basisklasse Animal und der erbenden Klasse Dog
animal = Animal("Heinrich")
dog = Dog("Bello")

# Aufrufen der breath-Methode für die Instanzen
animal.breath()  # Heinrich atmet
dog.breath()     # Bello atmet
