globale_variable = "Ich bin global"


def beispielFunktion():
    lokale_variable = "Ich bin lokal"
    print(lokale_variable)
    print(globale_variable)


beispielFunktion()

def schatten_funktion():
    globale_variable = "Lokal überschrieben"
    print(globale_variable)



schatten_funktion()
print(globale_variable)


def nichtSchattenFunktion():
    global globale_variable
    globale_variable = "Lokal überschrieben"
    print(globale_variable)

nichtSchattenFunktion()
print(globale_variable)
