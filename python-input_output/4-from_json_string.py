#!/usr/bin/python3
# Conversion d'une chaîne JSON en objet Python
import json


def from_json_string(my_str):
    # Retourne l'objet Python à partir du JSON
    return json.loads(my_str)
