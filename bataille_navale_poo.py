#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Version orientée objet de la Bataille Navale.
Inspirée du code procédural de base, en suivant les principes (encapsulation, héritage, typage statique, etc.)
"""
from typing import Tuple, List


class Ship:
	"""Représente un navire sur la grille."""
	def __init__(self, name: str, position: List[Tuple[int, int]]):

		self.name = name
		self.position = position # Cases occupée
		self.hits : List[Tuple[int, int]] = [] # Cases touchées

	def is_hit(self, coordinated: Tuple[int, int]) -> bool:
		"""Retourne True si la coordonnée correspond à une case du navire."""

		return coordinated in self.position

	def register_hit(self, coordinated: Tuple[int, int]) -> str:
		"""
		Marque un tir sur le navire et renvoie le message associé.
		:type coordinated: Tuple[int, int]
		"""
		if coordinated not in self.position:
			return "Manqué !"
		self.hits.append(coordinated)
		self.position.remove(coordinated)
		if not self.position:
			return f"Touché et coulé ! ({self.name})"
		return "Touché !"

	def is_sunk(self) -> bool:
		"""Retourne True si toutes les positions du navire ont été touchées."""

		return len(self.position) == 0


porte_avion = Ship("porte-avion", [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)])
print(porte_avion.is_hit((2, 3)))
