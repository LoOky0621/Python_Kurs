# -*- coding: utf-8 -*-
"""
    Multiplikation

    Schreibe ein Programm, das ermittelt,
    wie viele ganzzahlige Multiplikator-Multiplikand-Kombinationen
    vom Produkt 8.420.000 es gibt,
    bei denen sowohl Multiplikator, als auch Multiplikand
    kleiner als 10.000 sind.

    1000 * 8420 und 8420 * 1000 ist nur eine Kombination.
"""

zahl = 8420000
anzahl = 0

for divisor in range(1, 10000):
    if zahl % divisor == 0:
        quotient = zahl // divisor
        #print(quotient)
        if quotient < 10000:
            anzahl += 1
            print("Dividend:", quotient)

print("Kombinationen:", anzahl)
