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

        self.paths = []
        self.walls = []
        self.start = []
        self.goal = []
        
        self.load_from_file()

    def __contains__(self, position):
        """ returns only paths """
        return position in self.paths

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
                        self.paths.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    elif c == constants.START_GAME:
                        # if caracter correspond to START_GAME constant defined in settings
                        # add a Position instance in the attribute _start
                        # and add a Position instance in the attribute _path
                            # cause you always can come back by this position
                        self.paths.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                        self.start.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    elif c == constants.GOAL_CHAR:
                        # if caracter correspond to GOAL_CHAR constant defined in settings
                        # add a Position instance in the attribute _goal
                        # and add a Position instance in the attribute _path
                            # cause you always can path again by this position
                        self.paths.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                        self.goal.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))
                    elif c == constants.WALL_CHAR:
                        # if caracter correspond to WALL_CHAR constant defined in settings
                        # add a Position instance in the attribute _walls
                        self.walls.append(Position(x*constants.SPRITES_SIZE, y*constants.SPRITES_SIZE))

    def view_map(self, window):
        """ generate the map in the pygame window """
        # set walls
        wall_img = pygame.image.load(constants.IMG_WALL).convert()
        wall_img = pygame.transform.scale(wall_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        for position in self.walls :
            wall_pos = position.get_position
            window.blit(wall_img, wall_pos)
        # set floor
        paths_img = pygame.image.load(constants.IMG_FLOOR).convert()
        paths_img = pygame.transform.scale(paths_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        for position in self.paths :
            path_pos = position.get_position
            window.blit(paths_img, path_pos)
        #  set start case
        start_img = pygame.image.load(constants.IMG_START).convert()
        start_img = pygame.transform.scale(start_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        start_pos = self.start[0].get_position
        window.blit(start_img, (0,0))
