"""
Definiere einen Tupel mit Namen monate mit den Namen der zwölf Monate des Jahres.
Fordere den Benutzer auf, eine Zahl zwischen 1 und 12 einzugeben.
Verwende den Tupel, um den Namen des Monats anzuzeigen, der der eingegebenen Zahl entspricht. Beachte, dass 1 für
Januar, 2 für Februar usw. steht. Wenn die eingegebene Zahl außerhalb des Bereichs 1-12 liegt, gib eine Fehlermeldung
aus, die den Benutzer auffordert, eine gültige Zahl einzugeben.
Hinweis: Verwende die Eingabeüberprüfung, um sicherzustellen, dass der Benutzer eine gültige Zahl eingibt.
"""


monate = ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember")

def zeige_monat(user_input: int):
    if 1 <= user_input <= 12:
        print(f"Der Monat ist: {monate[user_input - 1]}")
    else:
       print("Bitte geben Sie eine gültige Zahl zwischen 1 und 12 ein.")

def user_input() -> int:
    user_input = int(input("Bitte geben Sie eine Zahl zwischen 1 und 12 ein: "))
    return user_input

zeige_monat(user_input())