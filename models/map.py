""" This module creates the map of the game """

import pygame
from pygame.locals import *

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
            for y, line in enumerate(f):
                # y axis
                for x, c in enumerate(line):
                    #  x axis
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

    def view_map(self, window):
        # set walls
        wall_img = pygame.image.load(constants.IMG_WALL).convert()
        wall_img = pygame.transform.scale(wall_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        for position in self._walls :
            wall_pos = position.get_position
            window.blit(wall_img, wall_pos)
        # set floor
        paths_img = pygame.image.load(constants.IMG_FLOOR).convert()
        paths_img = pygame.transform.scale(paths_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        for position in self._paths :
            path_pos = position.get_position
            window.blit(paths_img, path_pos)
        #  set start case
        start_img = pygame.image.load(constants.IMG_START).convert()
        start_img = pygame.transform.scale(start_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        start_pos = self.start.get_position
        window.blit(start_img, (0,0))
