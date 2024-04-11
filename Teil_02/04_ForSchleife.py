print("for-Schleife")

# Standardverwendung der range-Funktion
for i in range(5):
    print(i)

# range mit 2 Argumenten
print("range mit 2 Argumenten")
start = 5
stop = 10
for i in range(start, stop):
    print(i)

# range mit 3 Argumenten
print("range mit 3 Argumenten")
start = 2
stop = 10
step = 3
for i in range(start, stop, step):
    print(i)

# Benutzerdefinierte Verwendung der range-Funktion
print("Benutzerdefinierte Verwendung der range-Funktion")
for i in range(1, 15, 4):
    print(i)

# Beispiel 2: Benutzerdefinierte for-Schleife
print("Beispiel 2: Benutzerdefinierte for-Schleife")
startpunkt = 50
endpunkt = 0
schrittweite = -10
for i in range(startpunkt, endpunkt, schrittweite):
    print(i)

# Beispiel 3: Benutzerdefinierte for-Schleife
print("Beispiel 3: Benutzerdefinierte for-Schleife")
for i in range(6, -1, -2):
    print(i)
