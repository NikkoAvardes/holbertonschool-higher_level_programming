#!/usr/bin/python3
# Script pour ajouter des arguments à une liste dans un fichier JSON
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Tentative de chargement de la liste existante
try:
    my_list = load_from_json_file(filename)
except FileExistsError:
    my_list = []

# Ajout des arguments de la ligne de commande
my_list.extend(sys.argv[1:])
# Sauvegarde de la liste mise à jour
save_to_json_file(my_list, filename)
