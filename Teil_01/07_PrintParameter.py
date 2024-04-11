# Python print()-Funktion und ihre benannten Parameter

print("sep")
# sep: Definiert das Trennzeichen zwischen den Ausgaben. Standardmäßig ist dies ein Leerzeichen.
print("Hallo", "Welt", sep=" ")  # Hallo Welt (Default)
print("Hallo", "Welt", sep="-")  # Hallo-Welt
print("Hallo", "Welt", sep="#")  # Hallo#Welt

print("end")
# end: Definiert, was am Ende der Ausgabe hinzugefügt wird. Standardmäßig ist dies ein Zeilenumbruch.
print("Hallo", end="\n") # (Default)
print("Welt")
print("Hallo", end=" ")
print("Welt")
print("Hallo", end="")
print("Welt")




# Kombination von 'sep' und 'end': Nutzt beide Parameter in einem Befehl
print("kombination")
print("Hallo", "schöne", "neue", "Welt", sep="-", end="!")