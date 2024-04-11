class MyException(Exception):
    def __init__(self, message="Es werden nur positive Zahlen akzeptiert"):
        """
        Eine benutzerdefinierte Ausnahme, die ausgelöst wird, wenn eine nicht positive Zahl eingegeben wird.

        Args:
            message (str): Die Fehlermeldung, die angezeigt werden soll. Standardmäßig ist dies "Es werden nur positive Zahlen akzeptiert".
        """
        self.message = message
        super().__init__(self.message)

def run():
    """
    Die Hauptfunktion des Programms, die die Benutzereingabe für das Alter verarbeitet und Ausnahmen behandelt.
    """
    try:
        userInput = input("Geben Sie Ihr Alter ein: ")
        if int(userInput) < 0:
            raise MyException
        print("(>^.^)> Es wurden keine Ausnahmen ausgelöst <(^.^<)")
    except MyException as e:
        print(e)
        run()  # Ruft die run() Funktion erneut auf, um eine gültige Eingabe zu erhalten
    except Exception as e:
        print(e)


run()
