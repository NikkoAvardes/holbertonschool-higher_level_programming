#!/usr/bin/env python3
"""
Module pour la sérialisation et désérialisation de données en format XML.

Ce module fournit des fonctions pour convertir des dictionnaires Python
en fichiers XML et vice versa, en utilisant la bibliothèque
xml.etree.ElementTree.

Fonctions:
    serialize_to_xml(dictionary, filename): Sérialise un dictionnaire
                                           en fichier XML
    deserialize_from_xml(filename): Désérialise un fichier XML
                                   en dictionnaire

Exemple d'utilisation:
    data = {'name': 'John', 'age': 30, 'city': 'Paris'}
    serialize_to_xml(data, 'output.xml')
    result = deserialize_from_xml('output.xml')
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en fichier XML.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de sortie.

    Returns:
        None: La fonction écrit directement dans le fichier spécifié.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du fichier XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for item in root:
        text = item.text
        if text.isdigit():
            result[item.tag] = int(text)
        else:
            try:
                result[item.tag] = float(text)
            except ValueError:
                result[item.tag] = text
    return result
