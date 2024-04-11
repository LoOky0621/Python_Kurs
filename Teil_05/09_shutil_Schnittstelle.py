import shutil
import os

"""
Schlüsselkonzepte des shutil-Moduls:
shutil.copy(src, dst): Kopiert die Datei src nach dst. Wenn dst ein Verzeichnis ist, wird eine Datei mit demselben Namen darin erstellt.
shutil.move(src, dst): Verschiebt die Datei src nach dst. Kann auch zum Umbenennen verwendet werden.
shutil.copytree(src, dst): Kopiert ein Verzeichnis src rekursiv nach dst, einschließlich aller Unterverzeichnisse und Dateien.
shutil.rmtree(path): Löscht ein Verzeichnis und alle darin enthaltenen Dateien und Unterverzeichnisse rekursiv.
shutil.make_archive(base_name, format, root_dir): Erstellt ein Archiv (z.B. ZIP oder TAR) des Verzeichnisses root_dir.
shutil.unpack_archive(filename, extract_dir): Entpackt ein Archiv in das Verzeichnis extract_dir.


Das shutil-Modul ist besonders nützlich für Skripte, die Datei- und Verzeichnismanagement-Aufgaben automatisieren, 
wie das Einrichten von Projektstrukturen, das Erstellen von Backups oder das Verteilen von Dateien.
"""

# # Verzeichnis für Beispiele erstellen
# os.mkdir('shutil_demo')
# os.chdir('shutil_demo')
# Eine Testdatei im aktuellen Verzeichnis erstellen
# with open('testdatei.txt', 'w') as f:
#     f.write('Das ist eine Testdatei.')

# Kopieren einer Datei
# os.chdir('shutil_demo')
# shutil.copy('testdatei.txt', 'kopie_von_testdatei.txt')
# print("Datei kopiert")
#
# Verschieben einer Datei
# os.chdir('shutil_demo')
# shutil.move('kopie_von_testdatei.txt', 'neuer_name_fuer_kopie.txt')
# print("Datei verschoben und umbenannt")
#
# Ein Verzeichnis rekursiv kopieren
# os.chdir('shutil_demo')
# os.mkdir('quellverzeichnis')
# # Das Zielverzeichnis kann existieren, wenn dirs_exist_ok=True gesetzt ist
# with open(os.path.join('quellverzeichnis', 'datei_im_verzeichnis.txt'), 'w') as f:
#     f.write('Inhalt der Datei im Verzeichnis.')
# shutil.copytree('quellverzeichnis', 'zielverzeichnis', dirs_exist_ok=True)
# print("Verzeichnis kopiert")
#
# Ein Verzeichnis rekursiv entfernen
# os.chdir('shutil_demo')
# shutil.rmtree('zielverzeichnis')
# print("Verzeichnis gelöscht")
# #
# # Archivieren eines Verzeichnisses
# os.chdir('shutil_demo')
# shutil.make_archive('archiv', 'zip', 'quellverzeichnis')
# print("Verzeichnis archiviert")
# #
# # # Archiv entpacken
# os.chdir('shutil_demo')
# shutil.unpack_archive('archiv.zip', 'entpacktes_archiv')
# print("Archiv entpackt")
#
# Aufräumen
os.chdir('shutil_demo')
os.chdir('..')  # Zurück zum übergeordneten Verzeichnis
shutil.rmtree('shutil_demo')  # Demo-Verzeichnis entfernen
