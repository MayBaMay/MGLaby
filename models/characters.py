"""This module rules characters of the game"""
import pygame
from pygame.locals import *

import config.settings as constants
from models.map import Map
from models.position import Position


class Characters:
    """ Generate a character """

    def __init__(self, map):
        """ initialisation class Characters"""
        self.map = map
        self.position = self.map.start      #return to method @property from class Map
        # default value self.map.start, will be different for guard

    @property
    def get_position(self):
        return self.position.get_position

    def view_character(self, window, img):
        char_img = pygame.image.load(img).convert_alpha()
        char_img = pygame.transform.scale(char_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
        char_pos = self.get_position
        window.blit(char_img, char_pos)


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
