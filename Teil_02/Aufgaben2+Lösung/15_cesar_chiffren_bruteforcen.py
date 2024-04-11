"""
    Cäsar-Chiffre bruteforcen

    Schreibe ein Programm, das alle möglichen Lösungen
    eines Cäsar-chiffrierten Strings ausgibt.

    Was bedeutet "vxumxgssokxkt sginz yvgyy"?

    Wer Cäsar-Chiffre nicht kennt: https://de.wikipedia.org/wiki/Caesar-Verschlüsselung
"""

def caesar_bruteforce(encrypted_text):
    for shift in range(26):
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                    decrypted_text += chr(shifted)
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                    decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")

encrypted_message = "vxumxgssokxkt sginz yvgyy"
caesar_bruteforce(encrypted_message)
