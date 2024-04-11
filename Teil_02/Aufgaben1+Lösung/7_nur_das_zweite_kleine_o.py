# schreibe ein Python script das nur das 2te o in folgendem String
# zu einem "i" macht

# mein_anderer_string = "Otto oder Anna"

s = "Otto oder Anna"
erstes_o = s.find("O")
print("Position:", erstes_o)
zweites_o = s.find("o", erstes_o + 1)
print("Position:", zweites_o)
vorheriger_teil = s[:zweites_o]
print(vorheriger_teil)
nachfolgender_teil = s[zweites_o + 1:]
print(nachfolgender_teil)
neuer_string = vorheriger_teil + "i" + nachfolgender_teil
print()
print(neuer_string)