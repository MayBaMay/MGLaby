""" This module creates the map of the game """

import config.settings as constants
from models.position import Position


class Map :
    """generate the map of the game"""

    def __init__(self, filename):
        """ initialisation with datafile of the map"""

        self.filename = filename

        # set variables as private as we can't acces it from out of the class
        self._paths = set()
        self._walls = set()
        self._start = set()
        self._goal = set()

        self.load_from_file()

    def __contains__(self, position):
        return position in self._paths

    def load_from_file(self):
        """load datafile containing the shape of the map"""
        with open(self.filename) as f:
            for x, line in enumerate(f):
                # x = number of each line so x = y axis
                for y, c in enumerate(line):
                    # y = number of each column so y = x axis
                    if c == constants.PATH_CHAR:
                        # if caracter correspond to PATH_CHAR constant defined in settings
                        # add a Position instance in the attribute _paths
                        self._paths.add(Position(x, y))
                    elif c == constants.START_GAME:
                        # if caracter correspond to START_GAME constant defined in settings
                        # add a Position instance in the attribute _start
                        # and add a Position instance in the attribute _path
                            # cause you always can come back by this position
                        self._paths.add(Position(x, y))
                        self._start.add(Position(x, y))
                    elif c == constants.GOAL_CHAR:
                        # if caracter correspond to GOAL_CHAR constant defined in settings
                        # add a Position instance in the attribute _goal
                        # and add a Position instance in the attribute _path
                            # cause you always can path again by this position
                        self._paths.add(Position(x, y))
                        self._goal.add(Position(x, y))
                    else:
                        # this is a wall
                        # we  choose not to create a list of the wall positon
                        # pass
                        self._walls.add(Position(x, y))
    @property
    def start(self):
        """ transform self._start (set()) into a list """
        return list(self._start)[0]

    @property
    def exit(self):
        """ transform self._goal (set()) into a list """
        return list(self._goal)[0]

    # @property
    ## remarque je le trouve avec methode exit si goal au bout
    # def max_paths_coord(self):
    #     """gives size max of axis x and  y
    #       Purpose is to find out where we can add the elements of the syringe"""
    #     all_cases = self._paths | self._walls
    #     all_cases  =  list(all_cases)
        # max_tuple = max(all_cases, key=lambda x: x[0])
        # # return list(all_cases)[len(all_cases)-1]
        # # return max(list(all_cases))
        # return max_tuple
        ### bon je baisse les bras max() ne marche pas car à l'intérieur de la
            #liste c'est des objets de classe class et pas des tuple simple
            # mais si j'arrive à les transformer en tuple ça marcherait normalement
                        # for e in all_cases:
                        #     e = type(tuple)
                        # return type(all_cases[0])
                        ###marche pas du tout reste des objets class Position


def main():
    map = Map('data/maps/map.txt')
    p = Position(0,0).right().right()
    print(p in map)


if  __name__ == "__main__":
    main()
