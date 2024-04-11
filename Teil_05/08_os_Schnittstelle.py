import os

"""
Schlüsselkonzepte des os-Moduls:
os.getcwd(): Gibt das aktuelle Arbeitsverzeichnis zurück.
os.chdir(path): Wechselt das aktuelle Arbeitsverzeichnis zu path.
os.listdir(path='.'): Listet die Einträge im Verzeichnis path auf.
os.getenv(): Gibt den Wert der Umgebungsvariablen zurück.
os.mkdir(path): Erstellt ein Verzeichnis path.
os.rmdir(path): Löscht das Verzeichnis path.
os.path.join(): Fügt mehrere Pfade zusammen, um einen vollständigen Pfadnamen zu bilden.
os.path.exists(path): Überprüft, ob ein Pfad existiert.
os.name: Gibt den Namen des Betriebssystems zurück ('posix', 'nt', 'java').
"""

# # # Aktuelles Arbeitsverzeichnis abrufen
aktuelles_verzeichnis = os.getcwd()
# print("Aktuelles Arbeitsverzeichnis:", aktuelles_verzeichnis)
# #
# # # Verzeichnis wechseln
# os.chdir('..')  # Geht ein Verzeichnis nach oben
# print("Neues Arbeitsverzeichnis:", os.getcwd())
# #
# # Liste der Einträge im aktuellen Verzeichnis
# print("\nInhalte des aktuellen Verzeichnisses:")
# for eintrag in os.listdir('.'):
#     print(eintrag)
# #
# # Umgebungsvariablen
# print("\nPATH Umgebungsvariable:")
# print(os.getenv('PATH'))
#
# # Erstellen und Löschen eines Verzeichnisses
# os.mkdir('neuesVerzeichnis')
# print("Verzeichnis erstellt:", 'neuesVerzeichnis')
# os.rmdir('neuesVerzeichnis')
# print("Verzeichnis gelöscht:", 'neuesVerzeichnis')
#
# # Dateipfad-Operationen ersrtellt einen neuen Pfad (keine neue Datei)
pfad = os.path.join(aktuelles_verzeichnis, 'neueDatei.txt')
print("\nVollständiger Pfad zur neuen Datei:", pfad)
#
# # Überprüfen, ob eine Datei oder ein Verzeichnis existiert
print("Existiert 'neueDatei.txt'?", os.path.exists(pfad))
#
# # Betriebssystemspezifische Informationen
print("\nBetriebssystemname:", os.name)
print("Absolute Pfadname:", os.path.abspath('.'))
