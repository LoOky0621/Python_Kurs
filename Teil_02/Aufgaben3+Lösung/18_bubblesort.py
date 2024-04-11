"""
    Bubblesort

    Schreibe eine Datei in
    der man eine Liste mit beliebig vielen Integern als Werten übergeben kann
    und die diese Liste sortiert und zurückgibt.

    Benutze hierzu den Bubblesort-Algorithmus.
    Bei diesem wird die Liste durchlaufen
    und jede Zahl mit der jeweils nachfolgenden Zahl verglichen.
    Wenn die nachfolgende Zahl kleiner ist,
    werden die Zahlen getauscht.
    Die Liste wird solange durchlaufen,
    bis bei einem Durchlauf keine Zahlen getauscht werden müssen.
"""

def bubble_sort(input_list):
    n = len(input_list)
    # Durchlaufe die Liste, bis keine Elemente mehr getauscht werden müssen
    for i in range(n):
        swapped = False
        # Vergleiche jedes Element mit seinem Nachfolger
        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                # Tausche die Elemente, wenn sie in der falschen Reihenfolge sind
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        # Wenn in diesem Durchlauf keine Elemente getauscht wurden, ist die Liste sortiert
        if not swapped:
            break
    return input_list

# Beispielaufruf
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)

