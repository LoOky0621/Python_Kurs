import random

# Zufallszahl zwischen 0 und 1
print("Zufallszahl zwischen 0 und 1")
zufalls_float = random.random()
print("zufalls_float = random.random()", zufalls_float)
print("random.random()", random.random())

# Zufällige Ganzzahl zwischen 1 und 10
print("Zufällige Ganzzahl zwischen 1 und 10")
zufallszahl = random.randint(1, 10)
print("zufallszahl = random.randint(1, 10)", zufallszahl)
print("random.randint(1, 10)", random.randint(1, 10))

# Zufallsfloat zwischen zwei gegebenen Werten
print("Zufallsfloat zwischen zwei gegebenen Werten")
zufalls_float_bereich = random.uniform(88, 100)
print("zufalls_float_bereich = random.uniform(88, 100)", zufalls_float_bereich)
print("random.uniform(88, 100)", random.uniform(88, 100))
