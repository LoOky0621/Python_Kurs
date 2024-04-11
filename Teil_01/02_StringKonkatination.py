# String-Konkatenation

print("Verkettung mit dem + Operator")
string1 = "Hallo"
string2 = "Welt"
verkettet1 = string1 + " " + string2
print(verkettet1)

print("Verkettung innerhalb des print Befehls mit Komma")
print(string1, "junge", string2, "and", "Universe")

print("Verkettung mit der join() Methode")
strings = ["Hallo", "Welt"]  # Liste von Zeichenketten
print(strings)
verkettet2 = " ".join(strings)
print(verkettet2)

print("Verkettung mit Literalen")
verkettet3 = "Hallo" " Welt"
print(verkettet3)

print("Verkettung mit dem %-Operator")
verkettet4 = " Schreibe %s schöne %s auf die Konsole" % (string1, string2)
print(verkettet4)

print("Verkettung mit der format() Methode")
verkettet5 = "{} {}".format(string1, string2)
print(verkettet5)

print("Verkettung mit f-Strings (ab Python 3.6)")
verkettet6 = f"{string1} {string2}"
print(verkettet6)
