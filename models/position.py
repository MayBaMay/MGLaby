
""" This module allows all object in the programm to heve a position"""


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
        """ allowed to return position into a hashable table (or dictionnary)"""
        # renvoi  un tuple de clé de dictionnaire
        # hash  possible que  si non mutabilité
        return hash(self.position)

    def up(self):
        """ position lifted by 1"""
        x, y = self.position
        return self.__class__(x-1, y)

    def down(self):
        """ position lowered by 1 """
        x, y = self.position
        return self.__class__(x+1, y)

    def right(self):
        """ position moved by 1 towards the right """
        x, y = self.position
        return self.__class__(x, y+1)

    def left(self):
        """ position moved by 1 towards the left """
        x, y = self.position
        return self.__class__(x, y-1)


def main():
    pos = Position(3, 4)
    pos = pos.left().right().right().down().down().up()
    print(pos)


if  __name__ == "__main__":
    main()
