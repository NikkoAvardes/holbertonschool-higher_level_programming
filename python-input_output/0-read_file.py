#!/usr/bin/python3
# Fonction pour lire et afficher le contenu d'un fichier
def read_file(filename=""):
    # Ouverture et lecture du fichier en UTF-8
    with open(filename, encoding="utf-8") as e:
        read = e.read()
        print(read)
