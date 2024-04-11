"""
Definiere ein Dictionary namens studentenNoten mit Schülernamen als Schlüssel und ihren Noten als Wert. Beispiel:
studentenNoten = {"Anna": 1.3, "Bernd": 2.5, "Carla": 1.7, "David": 3.2}
Fordere den Benutzer auf, den Namen eines Schülers einzugeben.
Überprüfe, ob der eingegebene Name im Dictionary vorhanden ist. Wenn ja, zeige die Note des Schülers an.
Wenn der Name nicht im Dictionary vorhanden ist, gib eine Meldung aus, dass der Schüler nicht gefunden wurde, und
fordere den Benutzer auf, einen anderen Namen einzugeben.
Hinweis: Implementiere eine Schleife, die es dem Benutzer ermöglicht, wiederholt Namen einzugeben, bis ein gültiger
Name eingegeben wird oder der Benutzer entscheidet, das Programm zu beenden.
"""

studentenNoten = {"Anna": 1.3, "Bernd": 2.5, "Carla": 1.7, "David": 3.2}
while True:
    student = input("Bitte den Namen eines Schülers eingeben:")
    if student in studentenNoten.keys():
        note = studentenNoten[student]
        print(f"Student {student} hat die Note: {note}")
        print("Weitere Studenten suchen?")
        weiter = input("JA(y)/Nein(n)")
        if weiter == "n":
            break
    else:
        print(f"Student {student} nicht gefunden bitte noch einmal versuchen")

