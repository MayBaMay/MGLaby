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
                        self._paths.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    elif c == constants.START_GAME:
                        # if caracter correspond to START_GAME constant defined in settings
                        # add a Position instance in the attribute _start
                        # and add a Position instance in the attribute _path
                            # cause you always can come back by this position
                        self._paths.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                        self._start.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    elif c == constants.GOAL_CHAR:
                        # if caracter correspond to GOAL_CHAR constant defined in settings
                        # add a Position instance in the attribute _goal
                        # and add a Position instance in the attribute _path
                            # cause you always can path again by this position
                        self._paths.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                        self._goal.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    else:
                        # this is a wall
                        # we  choose not to create a list of the wall positon
                        # pass
                        self._walls.add(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
    @property
    def start(self):
        """ transform self._start (set()) into a list """
        return list(self._start)[0]

    @property
    def exit(self):
        """ transform self._goal (set()) into a list """
        return list(self._goal)[0]

    @property
    def paths(self):
        paths = []
        for e in self._paths:
            e = e.get_position
            paths.append(e)
        return paths

    @property
    def walls(self):
        walls = []
        for e in self._walls:
            e = e.get_position
            walls.append(e)
        return walls

def main():
    map = Map('data/maps/map_test.txt')
    p = Position(0,0).right().right().right()
    print(type(map.exit.get_position),map.exit.get_position)
    print(type(map.start.get_position),map.start.get_position)
    print(map.paths,type(map.paths[3]))
    print(map.walls,type(map.walls[3]))
    # print(type(map.paths[3].get_position),map.start[3].get_position)
    # print(p in map)


if  __name__ == "__main__":
    main()
