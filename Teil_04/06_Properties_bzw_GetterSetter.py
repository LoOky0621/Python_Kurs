class Auto:
    def __init__(self, maxSpeed):
        self.__maxSpeed = maxSpeed  # Der Setter wird aufgerufen

    @property
    def maxSpeed(self):
        """Getter-Methode für maxSpeed"""
        # todo sende Nachricht an Admin. SessionUser used this Getter
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, value):
        """Setter-Methode für maxSpeed"""
        if value < 0:
            print("Die Höchstgeschwindigkeit darf nicht negativ sein.")
            return
        self.__maxSpeed = value

auto = Auto(50)

# Nutzen des Setters
auto.maxSpeed = 100

# Nutzen des Getters
print(auto.maxSpeed)  # Ausgabe: 100

# Nutzen des Setters mit negativem Wert
auto.maxSpeed = -123456689  # Fehlermeldung: "Die Höchstgeschwindigkeit darf nicht negativ sein."

# Nutzen des Getters
print(auto.maxSpeed)  # Ausgabe: 100
