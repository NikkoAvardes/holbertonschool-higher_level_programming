#!/usr/bin/python3
# Sauvegarde d'un objet Python dans un fichier JSON
import json


def save_to_json_file(my_obj, filename):
    # Écriture de l'objet au format JSON dans le fichier
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
