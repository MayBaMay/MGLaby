"""This module rules characters of the game"""

from models.map import Map
from models.position import Position


class Characters:
    """ Generate a character """

    def __init__(self, map):
        """ initialisation class Characters"""
        self.map = map
        self.position = self.map.start
        # default value self.map.start, will be different for guard
        # self.map.start #return to method @property from class Map

    @property
    def get_position(self):
        return self.position


class Hero(Characters):
    """ Generate the Hero of the game : MacGyver! """

    def __init__(self, map):
        """ initialisation class Hero"""
        super().__init__(map)

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


class Guard(Characters):
    """ Generate the guard blocking the exit door """

    def __init__(self, map):
        super().__init__(map)
        self.position = self.map.exit


def main():
    game = Map('data/maps/map.txt')
    mg = Hero(game)
    g = Guard(game)
    print(g.get_position)
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
