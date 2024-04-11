# Definition der Klasse Pizza
class Pizza:
    # Statische Attribute, die für alle Instanzen der Klasse gleich sind
    belag = "Salami"
    durchmesser = 20

    # Methode, um Informationen über die Pizza auszugeben
    def info(self):
        # Zugriff auf die statischen Attribute über self
        print(f"Ich bin eine Pizza. Mein Belag ist {self.belag}, mein Durchmesser ist {self.durchmesser}")
        return None  # Rückgabe von None, um anzuzeigen, dass die Methode keinen Wert zurückgibt

# Erstellen einer Instanz der Pizza-Klasse
pizza1 = Pizza()

# Zugriff auf die statischen Attribute der Instanz
print(pizza1.belag)
print(pizza1.durchmesser)

# Aufrufen der info-Methode, um Informationen über die Pizza auszugeben
pizza1.info()

# Die info-Methode gibt None zurück, daher wird None hier gedruckt
print(pizza1.info())

# Ändern der Werte der Instanzattribute
pizza1.belag = "Diavolo"
pizza1.durchmesser = 40

# Drucken der geänderten Attributwerte und Aufrufen der info-Methode
print("Nach der Veränderung:")
print(pizza1.belag)
print(pizza1.durchmesser)
print(pizza1.info())
