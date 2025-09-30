#!/usr/bin/python3
# Fonction pour écrire du texte dans un fichier
def write_file(filename="", text=""):
    # Écriture dans le fichier (écrase le contenu existant)
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
