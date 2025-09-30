#!/usr/bin/python3
# Chargement d'un objet Python depuis un fichier JSON
import json


def load_from_json_file(filename):
    # Lecture et conversion du JSON en objet Python
    with open(filename, "r") as f:
        return json.load(f)
