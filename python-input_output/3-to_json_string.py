#!/usr/bin/python3
# Conversion d'un objet Python en chaîne JSON
import json


def to_json_string(my_obj):
    # Retourne la représentation JSON de l'objet
    return json.dumps(my_obj)
