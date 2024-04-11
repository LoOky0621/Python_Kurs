# Definition der Basisklasse Animal
class Animal:
    # Konstruktor, der beim Erstellen einer Instanz aufgerufen wird
    def __init__(self, name):
        self.name = name

    # Methode, um anzuzeigen, dass das Tier spricht
    def speak(self):
        print("Animal speaks")

# Definition der erbenden Klasse Dog, die von Animal erbt
class Dog(Animal):
    pass  # Dog erbt die speak-Methode von Animal

# Definition der erbenden Klasse Cat, die von Animal erbt
class Cat(Animal):
    # Überschreiben der speak-Methode von Animal
    def speak(self):
        return f"{self.name} sagt Miau!"

# Verwendung der abgeleiteten Klassen
dog = Dog("Bello")
cat = Cat("Whiskers")

# Aufrufen der speak-Methode für die Instanzen
print(dog.speak())  # Ausgabe: "Animal speaks" (von der Basisklasse geerbt)
print(cat.speak())  # Ausgabe: "Whiskers sagt Miau!" (von der abgeleiteten Klasse Cat)
