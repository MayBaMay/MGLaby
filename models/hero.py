#! /usr/bin/env python3
# coding: utf-8


"""This module contains the object Hero"""

from models.map import Map

from models.map import Map
from models.position import Position

class Hero :
	""" Generate the Hero of the game : MacGyver! """

	def __init__(self, map):
		""" initialisation class Hero"""
		self.map = map
		self.position = self.map.start
		# self.map.start #return to method @property from class Map

	@property
	def get_position(self):
		return self.position

	def move(self, direction):
		""" function for heroes movements in the map"""
		new_position = getattr(self.position, direction)()
		# getattr allowed acces an object properties with a string
		# ex : getattr(self.position, "up") = applique la méthode up sur self.position
		if new_position in self.map:
			self.position = new_position
			#  don't add a else cause if it's not in th map, self.position stay the same
		# hero doesn't go through  the walls  neither
		# cause new_position  is not in self.map (returns to function Map.__contains__)

def main():

	game  = Map('data/maps/map.txt')

	game = Map('data/maps/map.txt')
	mg = Hero(game)
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)
	mg.move("down")
	print(mg.get_position)
	mg.move("right")
	print(mg.get_position)



if __name__ == "__main__":
	main()
