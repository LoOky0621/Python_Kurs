# Mehr Zahlenreihen

# 1.
# Schreibe eine for-Schleife, die Folgendes ausgibt:
# 1,0 2,2 3,4 4,6 5,8 7,0 8,2 9,4

for i in range(1, 10):
    if i == 6:
        continue
    elif i < 6:
        print(f"{i},{2*i}", end=" ")
    else:
        print(f"{i-1},{2*(i-1)}", end=" ")


print("-----------------------")
# 2.
# Schreibe ein Programm, das per for-Schleife
# alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.
start = 1
stop = 20
step = 1
erg = 0
for zahl in range(start, stop+1, step):
    erg += zahl
print(erg)
print("-----------------------")
# 3.
# Schreibe eine for-Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23

for i in range(0, 3):
    a = i * 10 + 2
    b = i * 10 + 3
    print(f"a{a}b{b}", end=" ")
print()
print("-----------------------")
# 4.
# Schreibe eine for-Schleife, die Folgendes ausgibt:
# 13 17 21 29 33 37 45

start = 13
stop = 45
step = 4
for i in range(start, stop+1, step):
    print(i, end=" ")
print()
print("-----------------------")

# 5.
# Schreibe EINE for-Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1

for i in range(1, 5+1, 1):
    print(i, end=" ")
    if i == 5:
        for j in range(4, 1-1, -1):
            print(j, end=" ")
print()
print("-----------------------")