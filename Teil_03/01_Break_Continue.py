# 'break' beendet die Schleife, in der es auftritt, und springt zum Code nach der Schleife.
# 'continue' beendet die aktuelle Iteration der Schleife und springt zur nächsten Iteration.

print("break in for-Schleife")
for i in range(5):
    if i == 3:
        break  # Beendet die Schleife, wenn i gleich 3 ist
    print(i)

print("continue in for-Schleife")
for i in range(5):
    if i == 3:
        continue  # Überspringt den Rest der aktuellen Iteration, wenn i gleich 3 ist
    print(i)

print("break in while-Schleife")
i = 0
while i < 5:
    if i == 3:
        break  # Beendet die Schleife, wenn i gleich 3 ist
    print(i)
    i += 1

print("continue in while-Schleife")
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue  # Springt zur nächsten Iteration, wenn i gleich 3 ist
    print(i)
    i += 1

print("break im enhanced for loop")
liste = [4, 5, 6]
for element in liste:
    if element == 5:
        break  # Beendet die Schleife, wenn das Element gleich 5 ist
    print(element)

print("continue im enhanced for loop")
liste = [4, 5, 6]
for element in liste:
    if element == 5:
        continue  # Springt zur nächsten Iteration, wenn das Element gleich 5 ist
    print(element)

print("Break im verschachtelten Loop")
outer = 0
inner = 0
while outer < 5:
    print("outer =", outer)
    while inner < 5:
        print("inner =", inner)
        inner += 1
        break  # Beendet den inneren Loop bei der ersten Iteration
    outer += 1
    inner = 0  # Setzt den inneren Loop-Zähler zurück, um ihn bei jedem äußeren Loop neu zu starten
