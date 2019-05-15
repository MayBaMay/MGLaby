
""" This module allows all objects in the programm to have a position
This position is encapsulated in an independant class.
That will allow us to use methods directly to those positions."""

import config.settings as constants


class Position:
    """generate object's position """

    def __init__(self, x, y):
        """ initialisation with position defined with a tuple (x, y)"""
        self.position = (x, y)

    def __eq__(self, pos):
        if isinstance(pos, Position): # if object still in the game
            # compare two objects of this class with their attribute ".position"
            return self.position == pos.position

    def up(self):
        """ position lifted by 1 sprite """
        x, y = self.position
        return self.__class__(x, (y-constants.SPRITES_SIZE))

    def down(self):
        """ position lowered by 1 sprite"""
        x, y = self.position
        return self.__class__(x, (y+constants.SPRITES_SIZE))

    def right(self):
        """ position moved by 1 sprite towards the right """
        x, y = self.position
        return self.__class__((x+constants.SPRITES_SIZE), y)

    def left(self):
        """ position moved by 1 sprite towards the left """
        x, y = self.position
        return self.__class__((x-constants.SPRITES_SIZE), y)

    @property
    def get_position(self):
        """ returns position in the map as a coordinate tuple (x, y)"""
        x, y = self.position
        return (x, y)
