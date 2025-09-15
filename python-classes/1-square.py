#!/usr/bin/python3
"""Module qui définit une classe Square avec attribut privé size"""


class Square:
	"""Classe qui définit un carré avec taille privée"""

	def __init__(self, size=None):
		"""Initialise un carré avec une taille donnée
		
		Args:
			size: La taille du carré
		"""
		self.__size = size
