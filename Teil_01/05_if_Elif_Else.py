# if-else
# Kontrollstruktur
# else darf es nur einmal geben
# elif kann es beliebig oft geben

x = 7

print("if")
if x == 7:
    print("x == 7")

print("if-else")
if x == 8:
    print("x == 8")
else:
    print("x != 8")

print("if-elif-else")
x = 11
if x == 7:          # WENN
    print("x == 7")
elif x == 11:  # SONST WENN
    print("x == 11")
elif x == 17:       # SONST WENN
    print("x == 17")
else:               # SONST
    print("In x ist keine 7 oder 11 oder 17!")

print("Verschachteln")
x = 11
if x != 7: # True
    if x != 11: # False
        if x != 17: # True
            print("In x ist keine 7 oder 11 oder 17!")
        else:
            print("if x != 17 ist False")
    else:
        print("x != 11 ist False")
else:
    print("x != 7 ist False")
