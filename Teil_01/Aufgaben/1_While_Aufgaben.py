"""Achte darauf das die Ausgabe auch tatsächlich in einer Zeile stattfindet"""

# 1.
# Schreibe eine while-Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10

start = 100
end = 0
zähler = 10
while start > end:
    print(start)
    start = start - zähler
print("--------------------------")


# 2.
# Schreibe eine while-Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000

start = 2000
end = 6000
zähler = 1000
while start <= end:
    print(start)
    start = start + zähler
print("--------------------------")


# 3.
# Schreibe eine while-Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0

start = 2.0
end = -1.0
zähler = 0.5
while start >= end:
    print(start)
    start = start - zähler
print("--------------------------")

# 4.
# Schreibe eine while-Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13

start = 5
end = 13
zähler = 2
while start <= end:
    print(f'Z{start}')
    start = start + zähler
print("--------------------------")
