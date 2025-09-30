#!/usr/bin/python3
# Fonction pour ajouter du texte à la fin d'un fichier
def append_write(filename="", text=""):
    # Ajout du texte à la fin du fichier
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
