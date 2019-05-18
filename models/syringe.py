""" This module generates elements for the syringe
MacGyver has to make it with a needle, a small plastic tube and ether
Those elements will be found on the map randomly
They will be used to distract the guard at the exit door"""

from random import randrange
import pygame
from pygame.locals import *

import config.settings as constants
from models.position import Position


class Syringe:
    """Generates elements for the syringe"""

    def __init__(self, map, hero):
        self.map = map
        self.hero = hero
        self.objects = ['needle', 'tube', 'ether']
        self.componants = {}
            # form self.componants will be : {"object_name" : [position , flag]}
            # flag : True=picked / False=not picked
        self.syringe = False    #turns True when all objects had been picked

        self.place_componants()

    def place_componants(self):
        """ Instanciation of syringe's componants :
        They shouldn't be outside a path neither then at the same place
        of an other or start and goal postition """
        places = []            # used positions checking list
        for object in self.objects:
            while 1:
                randrange_x = randrange(0, constants.LAST_POS, constants.SPRITES_SIZE)
                randrange_y = randrange(0, constants.LAST_POS, constants.SPRITES_SIZE)
                place = Position(randrange_x, randrange_y)
                if place in self.map:            # check in available sprites (paths)
                    if place not in self.map.start:     # check out of start sprite
                        if place not in self.map.goal:      # check out of goal sprite
                            if place not in places:              # check not already used sprite
                                break
            places.append(place)
            infos = [place, False]
            self.componants[object] = infos

    @property
    def objects_positions(self):
        """ returns all the class_objects positions"""
        pos = []            # get positions only
        for object in self.objects:
            if isinstance(self.componants[object][0], Position):
                p = self.componants[object][0].get_position
                pos.append(p)
            else:
                pos.append(self.componants[object][0])
        return pos

    @property
    def get_flags(self):
        """ returns flags allowing to check if the hero passed through the sprite already"""
        flags = []      # list of flags which are True if the hero picked the object
        for object in self.objects:
            flags.append(self.componants[object][1])
        return flags

    def interaction_hero(self):
        """ if componant is on the same position as the hero, componant removed from the list"""
        for componant, info in self.componants.items():
            if isinstance(info[0], Position):
                if info[0].get_position == self.hero.get_position:
                    self.componants[componant] = ['off', True]
                    return componant

    def check_making(self):
        """ check if all the componant have been picked up"""
        flags = self.get_flags
        if False not in flags:         #so if the hero found all the componants
            self.syringe = True
            return True

    def view_objects(self, window):
        """ generates objects in the pygame window
        only if position still in the object's values
        would be "off" if the hero picked it up, or a class Position object if not """
        # view needle
        if isinstance(self.componants["needle"][0], Position):
            needle_img = pygame.image.load(constants.IMG_NEEDLE).convert_alpha()
            needle_img = pygame.transform.scale\
                        (needle_img, (constants.SPRITES_SIZE, constants.SPRITES_SIZE))
            needle_pos = self.componants["needle"][0].get_position
            window.blit(needle_img, needle_pos)
        # view ether
        if isinstance(self.componants["ether"][0], Position):
            ether_img = pygame.image.load(constants.IMG_ETHER).convert()
            ether_img.set_colorkey((1, 1, 1))     # ignore black background
            ether_img = pygame.transform.scale\
                        (ether_img, (constants.SPRITES_SIZE, constants.SPRITES_SIZE))
            ether_pos = self.componants["ether"][0].get_position
            window.blit(ether_img, ether_pos)
        # view tube
        if isinstance(self.componants["tube"][0], Position):
            tube_img = pygame.image.load(constants.IMG_TUBE).convert()
            tube_img.set_colorkey((255, 255, 255))    # ignore white background
            tube_img = pygame.transform.scale\
                        (tube_img, (constants.SPRITES_SIZE, constants.SPRITES_SIZE))
            tube_pos = self.componants["tube"][0].get_position
            window.blit(tube_img, tube_pos)
