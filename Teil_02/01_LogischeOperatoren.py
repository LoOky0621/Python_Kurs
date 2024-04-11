# Logische Operatoren / Boolsche Operatoren
print("and, or, not")

# and - UND (sowohl als auch)
# Nur True, wenn beide True sind
print("and - UND (sowohl als auch)")
print(3 >= 2 and 7 != 9)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# or - ODER (entweder oder)
# Nur False, wenn beide False sind
print("or - ODER (entweder oder)")
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# not - NICHT
# not kehrt den Boolean um
print("not - NICHT")
print(not (1 == 1))  # False
print(not True)  # False
print(not False)  # True
