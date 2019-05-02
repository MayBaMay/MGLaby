#! /usr/bin/env python3
# coding: utf-8

from models.map import Map
from models.position import Position
from models.hero import Hero

""" This module contains the object Guard """

class Guard:
    """ Generate the guard blocking the exit door """

    def __init__(self, map):
        self.map = map
        self.position = self.map.exit   # N.B: starts with 0

        self.test_map_sides()

    def test_map_sides(self):
        """ check where to put the guard in the game"""
        pass
        # if self.position.right not in self.map:
        #     if self .position.left not in self.map :


def main():
    game = Map('data/maps/map.txt')
    g = Guard(game)
    print(g.test_map_sides())

if __name__ == "__main__":
    main()
