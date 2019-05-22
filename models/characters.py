"""This module rules characters of the game"""

import pygame
from pygame.locals import *

import config.settings as constants


class Characters:
    """ Generate a character """

    def __init__(self, mase):
        """ initialisation class Characters"""
        self.mase = mase
        self.position = self.mase.start[0]
        # default value self.mase.start, will be different for the guard

    @property
    def get_position(self):
        """ call the get_position function from the class Position
        to use the position as a tuple """
        return self.position.get_position

    def view_character(self, window, img):
        """ generate the character in the pygame window """
        char_img = pygame.image.load(img).convert_alpha()
        char_img = pygame.transform.scale\
                    (char_img, (constants.SPRITES_SIZE, constants.SPRITES_SIZE))
        char_pos = self.get_position
        window.blit(char_img, char_pos)


class Hero(Characters):
    """ Generate the Hero of the game : MacGyver! """

    def __init__(self, mase):
        """ initialisation class Hero"""
        Characters.__init__(self, mase)

    def move(self, direction):
        """ function for hero's movements in the mase"""
        new_position = getattr(self.position, direction)()
        # getattr allows acces to object's properties with a string
        # ex : getattr(self.position, "up") = call the method up on self.position
        if new_position in self.mase:
            # returns to function Map.__contains__ which had been limited to paths
            self.position = new_position
            # don't add an else cause if it's not in a path, self.position stay the same


class Guard(Characters):
    """ Generate the guard blocking the exit door """

    def __init__(self, mase):
        super().__init__(mase)
        self.position = self.mase.goal[0]
