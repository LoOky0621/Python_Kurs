"""
Definiere eine Liste mit Namen temperaturen mit zufälligen Temperaturwerten für eine Woche (7 Werte).
Fordere den Benutzer auf, eine neue Temperatur (als Ganzzahl oder Fließkommazahl) einzugeben, die am Ende der Liste hinzugefügt werden soll.
Aktualisiere die Liste, indem du die neue Temperatur hinzufügst.
Berechne den Durchschnitt der Temperaturen in der aktualisierten Liste.
Gib die aktualisierte Liste der Temperaturen und den berechneten Durchschnittswert aus.
Hinweis: Verwende geeignete Funktionen, um die Liste zu aktualisieren und den Durchschnitt zu berechnen.
"""
import random
meineListe = []
erg = 0
zähler = 0
for temp in range(1, 7+1, 1):
    zufall = random.randint(-20, 50)
    meineListe.append(zufall)
    erg += zufall
for templiste in meineListe:
    zähler += 1
    print(f"Temperatur {zähler}: {templiste}")
eingabe = input("Bitte eine weitere Temperatur eingaben: ")
meineListe.append(eingabe)
eingabe = int(eingabe)
erg += eingabe
print("Die Durchschnittstemperatur beträgt: ", erg / 8, "° Celsius")


