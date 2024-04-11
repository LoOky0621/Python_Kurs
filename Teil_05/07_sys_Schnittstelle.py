import sys

"""
sys.argv: Eine Liste, die die Kommandozeilenargumente enthält, die an ein Python-Skript übergeben wurden. 
Sehr nützlich für Skripte, die Parameter über die Kommandozeile akzeptieren.

sys.exit(): Beendet das Python-Programm. Kann optional einen Exit-Status übergeben, der an das Betriebssystem 
zurückgegeben wird.

sys.path: Eine Liste von Verzeichnisnamen, in denen Python nach Modulen sucht, wenn ein import-Befehl ausgeführt wird. 
Dies kann zur Laufzeit modifiziert werden, um zusätzliche Verzeichnisse einzubeziehen.

sys.version und sys.platform: Geben Informationen über die Python-Version bzw. die Plattform, auf der das Skript läuft.

sys.stdin, sys.stdout, sys.stderr: Objekte, die für die Ein- und Ausgabe in der Konsole verwendet werden. Nützlich für 
die Umleitung von Ein- und Ausgaben oder das Schreiben von Fehlermeldungen.
"""

# sys.argv
# Zugriff auf Kommandozeilenargumente; argv[0] ist der Skriptname
# print("Skriptname:", sys.argv[0])
# if len(sys.argv) > 1:
#     print("Übergebene Argumente:", sys.argv[1:])

# sys.exit()
# Beendet das Python-Programm; kann einen optionalen Exit-Statuscode übernehmen
# Entkommentieren Sie die nächste Zeile, um das Beenden zu demonstrieren
# sys.exit(10)

# sys.path
# Eine Liste von Strings, die die Suchpfade für Module angibt
# print("\nPython-Suchpfade:")
# for pfad in sys.path:
#     print(pfad)
#
# sys.version
# Zeigt die Python-Version, die aktuell ausgeführt wird
# print("\nPython-Version:")
# print(sys.version)
#
# sys.platform
# Zeigt die Plattform, auf der das Skript läuft
# print("\nPlattform:")
# print(sys.platform)
#
# # sys.stdin, sys.stdout, sys.stderr
# Zugriff auf die Standard-Ein-/Ausgabe- und Fehler-Streams
# sys.stdin liest Eingaben, sys.stdout gibt Ausgaben aus, und sys.stderr gibt Fehler aus
# print("\nBeispiel für die Nutzung von sys.stdout:", file=sys.stdout)
# print("Beispiel für die Nutzung von sys.stderr", file=sys.stderr)