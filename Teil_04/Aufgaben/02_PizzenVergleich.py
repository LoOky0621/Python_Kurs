"""
Pizzen-Vergleich

Erweitere die Klasse `Pizza` um eine Methode `__eq__`, die das Gleichheitsverhalten überlädt.
Zwei Pizzen sollen als gleich betrachtet werden, wenn sie die gleiche Größe und den gleichen Belag haben.

Teste die neue Methode mit dem folgenden Code:

class Pizza:
    def __init__(self, belag="Margherita", groesse=28):
        self.belag = belag
        self.groesse = groesse


# Beispiele für die Erstellung von Pizza-Instanzen
p1 = Pizza()
p2 = Pizza("Margherita")
p3 = Pizza(belag=28)
p4 = Pizza("Margherita", 28)

print(p1 == p2)  # True
print(p1 == p3)  # True
print(p1 == p4)  # True

p5 = None
str = "Margherita"
print(p1 == p5)   # False
print(p1 == str)  # False

p7 = Pizza("Salami")
p8 = Pizza(30)
p9 = Pizza("Funghi", 32)

print(p1 == p7)  # False
print(p1 == p8)  # False
print(p1 == p9)  # False

Anweisungen:
1. Definiere eine Klasse `Pizza` mit den Attributen `belag` und `groesse` und setze Standardwerte.
2. Implementiere die Methode `__eq__`, die zwei Pizzen auf Gleichheit überprüft.
3. Teste die Methode mit dem bereitgestellten Code.
"""


class Pizza:
    def __init__(self, belag="Margherita", groesse=28):
        # Initialisierung der Pizza mit Standardwerten für Belag und Größe
        self.belag = belag
        self.groesse = groesse

    def __eq__(self, pizza2):
        # Überladung des Gleichheitsoperators, um die Gleichheit zweier Pizzen zu überprüfen
        if isinstance(pizza2, Pizza):
            # Überprüfen, ob pizza2 eine Instanz von Pizza ist
            return self.belag == pizza2.belag and self.groesse == pizza2.groesse
            # Rückgabe von True, wenn Belag und Größe beider Pizzen übereinstimmen
        return False
        # Rückgabe von False, wenn pizza2 keine Instanz von Pizza ist

# Beispiele für die Erstellung von Pizza-Instanzen
p1 = Pizza()  # Standard-Pizza
p2 = Pizza("Margherita")  # Pizza mit Standard-Belag
p3 = Pizza(belag=28)  # Pizza mit Standard-Größe
p4 = Pizza("Margherita", 28)  # Pizza mit Standard-Belag und -Größe

# Ausgabe des Vergleichs von Pizzen
print(p1 == p2)  # True, da beide Pizzen die Standardwerte haben
print(p1 == p3)  # True, da beide Pizzen die Standardwerte haben
print(p1 == p4)  # True, da beide Pizzen die Standardwerte haben

# Weitere Tests mit unterschiedlichen Datentypen und Pizzakombinationen
p5 = None
str = "Margherita"
print(p1 == p5)   # False, da p5 nicht vom Typ Pizza ist
print(p1 == str)  # False, da str kein Pizza-Objekt ist

p7 = Pizza("Salami")  # Pizza mit anderem Belag
p8 = Pizza(30)  # Pizza mit anderer Größe
p9 = Pizza("Funghi", 32)  # Pizza mit anderem Belag und anderer Größe

# Weitere Vergleiche von Pizzen
print(p1 == p7)  # False, da die Beläge unterschiedlich sind
print(p1 == p8)  # False, da die Größen unterschiedlich sind
print(p1 == p9)  # False, da sowohl Belag als auch Größe unterschiedlich sind

