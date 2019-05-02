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
        # say the guard is in the exit cause
        # hero can pass through it but can't go bout
        # will guard stairs for example

    @property
    def get_position(self):
        return self.position

def main():
    game = Map('data/maps/map.txt')
    g = Guard(game)
    print(g.get_position)

if __name__ == "__main__":
    main()
