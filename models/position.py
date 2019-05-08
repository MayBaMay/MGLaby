
""" This module allows all object in the programm to heve a position"""

import config.settings as constants


class Position :
    """generate object's position """

    def __init__(self, x, y):
        """ initialisation with position defined by tuple (x, y)"""
        self.position = (x, y)

    def __repr__(self):
        """ return position as a list of tuple when printed """
        return str(self.position)

    def __eq__(self, pos):
        if isinstance(pos, Position): # if object still in the game
            # compare two positions
            return self.position == pos.position

    def __hash__(self):
        """ allow to return position into a hashable table (or dictionnary)"""
        # renvoi  un tuple de clé de dictionnaire
        # hash  possible que  si non mutabilité
        return hash(self.position)

    def up(self):
        """ position lifted by 1 case"""
        x, y = self.position
        return self.__class__(x, (y-constants.SPRITES_SIZE))

    def down(self):
        """ position lowered by 1 case"""
        x, y = self.position
        return self.__class__(x, (y+constants.SPRITES_SIZE))

    def right(self):
        """ position moved by 1 case towards the right """
        x, y = self.position
        return self.__class__((x+constants.SPRITES_SIZE), y)

    def left(self):
        """ position moved by 1 case towards the left """
        x, y = self.position
        return self.__class__((x-constants.SPRITES_SIZE), y)

    @property
    def get_position(self):
        """ returns position in the map as a coordinate tuple"""
        x, y = self.position
        return (x, y)
