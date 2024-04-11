# 'w' öffnet/erzeugt eine Datei im (Über-)Schreibmodus / Write mode
with open("file.txt", "w") as datei:
    datei.write("[w] hat den gesamten Text überschrieben")

# 'a' öffnet eine Datei im Anhängemodus / Append mode
with open("file.txt", "a") as datei:
    # Fügt am Ende einer Datei Text hinzu
    datei.write("\n[a] war auch hier!")

# 'r' öffnet eine Datei im Lesemodus / Read mode
with open("file.txt", "r") as datei:
    if datei.mode == 'r':
        # Überprüfe, ob die Datei existiert, bevor du ihren Inhalt liest
        inhalt = datei.read()
        print(f"\t\t\t\t[r] liest: \n {inhalt}")

# 'wb' öffnet/erzeugt eine Datei im Binär-Schreibmodus / Write Binary mode
with open("file.bin", "wb") as datei:
    # Schreibt binäre Daten in die Datei
    datei.write(b"[wb] hat binaere Daten geschrieben")

# 'rb' öffnet eine Datei im Binär-Lesemodus / Read Binary mode
with open("file.bin", "rb") as datei:
    if datei.mode == 'rb':
        # Liest binäre Daten aus der Datei
        inhalt = datei.read()
        print(f"\t\t\t\t[rb] liest: \n {inhalt}")
        # Binäre Darstellung
        binär_inhalt = ' '.join(format(byte, '08b') for byte in inhalt)
        print(f"\t\t\t\t[rb] liest binär: \n {binär_inhalt}")
