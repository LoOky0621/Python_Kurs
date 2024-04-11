
"""
Fakultät

Schreibe ein Programm,
das ermittelt, welche Zahl möglichst groß ist
ohne dass ihre Fakultät über 1.000.000.000 ist.

Gib zum Beweis auch alle kleineren Fakultäten aus.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""

def fakultät(wert):
    if wert == 0:
        return 1
    else:
        return wert * fakultät(wert - 1)

zahl = 0
fakultät_wert = 1
while fakultät_wert <= 1000000000:
    print(f"{zahl}! = {fakultät_wert}")
    zahl += 1
    fakultät_wert = fakultät(zahl)

print(f"Die größte Zahl mit einer Fakultät unter 1.000.000.000 ist {zahl - 1}.")



