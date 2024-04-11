"""
Begrüßung

Es soll eine Begrüssung in Abhängigkeit zur Uhrzeit ausgegeben werden.
Zwischen 22Uhr und 5Uhr: Gute Nacht
Vor 11Uhr: Guten Morgen
Vor 15Uhr: Mahlzeit
Vor 18Uhr: Guten Nachmittag
Vor 22Uhr: Guten Abend

Die Stunde per Random zwischen 0 - 23 erstellen.
"""

from random import randint
# from datetime import time

def uhrzeit() -> str:
    stunde = randint(0, 23)


    if 22 <= stunde or stunde < 5:
        begruessung = "Gute Nacht"
    elif stunde < 11:
        begruessung = "Guten Morgen"
    elif stunde < 15:
        begruessung = "Mahlzeit"
    elif stunde < 18:
        begruessung = "Guten Nachmittag"
    else:
        begruessung = "Guten Abend"

    return(f'{begruessung}, es ist {stunde} Uhr')

print(uhrzeit())

