"""
    Einmaliges in Liste

    Schreibe ein Programm, das eine Liste mit neun Zahlen befüllt.
    Dabei sollen vier Zahlen doppelt vorkommen
    und eine Zahl nur einmal.

    Mische dann die Liste zufällig durch.

    Schreibe dann ein Programm, das aus dieser Liste die Zahl findet,
    die nur einmal vorkommt.
"""
import random
def zahlen_generieren() -> list:

    doppelte_zahlen = random.sample(range(1, 101, 4), 4)
    print(f'DEBUG: Doppelte Zahlen: {doppelte_zahlen}')


    liste = doppelte_zahlen * 2


    while True:
        fuenfte_zahl = random.randint(1, 101)
        if fuenfte_zahl not in doppelte_zahlen:
            liste.append(fuenfte_zahl)
            print(f'DEBUG: einzigartige Zahl: {fuenfte_zahl}')
            break


    random.shuffle(liste)
    print(f'DEBUG: Liste mit Zahlen, gemischt: {liste}')

    return liste

def finde_die_eine(liste:list) -> int:
    #anzahl = len(liste)
    #print(f'DEBUG: Anzahl: {anzahl}')

    zahl_anzahl = {}
    for zahl in liste:
        if zahl in zahl_anzahl:
            zahl_anzahl[zahl] += 1
        else:
            zahl_anzahl[zahl] = 1

    for zahl, anzahl in zahl_anzahl.items():
        if anzahl == 1:
            print(f'DEBUG: Einzigartige Zahl gefunden: {zahl}')
            return zahl



finde_die_eine(zahlen_generieren())