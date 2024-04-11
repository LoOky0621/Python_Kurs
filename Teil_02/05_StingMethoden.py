myString = "Hello World!"
print("len(myString)")
# gibt die Länge des Strings zurück
laenge = len(myString)
print(laenge)  # 12

print("einzelner Buchstabe (Substring)")
print("einzelner_Buchstabe = myString[4]")
einzelner_Buchstabe = myString[4]  # exklusiv des 5.-Index "o"
print(einzelner_Buchstabe)  # o

print("String-Teilung (Substring)")
print("erster_teil = myString[:5]")
erster_teil = myString[:5]  # exklusiv des 5.-Index "o"
print(erster_teil)  # Hallo

print("zweiter_teil = myString[5:] (Substring)")
zweiter_teil = myString[6:]  # inklusive des 6.-Index "W"
print(zweiter_teil)  # World!

print("teil_ab_index_bis_index = myString[3:8]")
teil_ab_index_bis_index = myString[3:8]  # erster Index ist inklusive, der zweite ist exklusiv
print(teil_ab_index_bis_index)  # lo Wo

print("myString.upper()")
gross = myString.upper()  # Methoden-Aufruf
print(gross)  # HELLO WORLD!

print("myString.lower()")
klein = myString.lower()
print(klein)  # hello world!

print("myString.replace('World', 'Python')")
ersetzt1 = myString.replace("World", "Python")
print(ersetzt1)  # Hallo Python!

mein_anderer_string = "Otto oder Anna"

print('mein_anderer_string.replace("o", "i", 1)')
ersetzt1 = mein_anderer_string.replace("o", "i", 1)
print(ersetzt1)  # itto oder Anna

print('mein_anderer_string.replace("o", "i")')
ersetzt2 = mein_anderer_string.replace("o", "i")
print(ersetzt2)  # Itti iider Anna

print('myString.find("World")')
position = myString.find("World")  # gibt den Index zurück, bei dem das Wort anfängt
print(position)  # 6

print('myString.find("d")')
position = myString.find("d")  # gibt den ersten Treffer zurück
print(position)  # 10
print('mein_anderer_string.find("d")')
position1 = mein_anderer_string.find("o")  # gibt den ersten Treffer zurück
print(position1)  # 1

for i in range(5):
    print(f"irgendwas hat den Wert: {i}")
