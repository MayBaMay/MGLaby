#! /usr/bin/env python3
# coding: utf-8

"""
Dans le cadre du parcours de formation Développeur d’application Python,
nous cherchons à développer un petit jeu dans lequel MacGyver doit s’échapper
d’un labyrinthe dont la sortie est bloquée par un garde. MacGyver doit trouver
un moyen de s’échapper et pour se faire il doit trouver divers éléments,
aléatoirement placés dans le labyrinthe, pour fabriquer une seringue qui
servira à endormir le garde. Sans cela, MacGyver n’est pas assez fort pour
le vaincre et meurt, tel un héros mais meurt quand même...

Script Python 3.7.3
"""

import time
from random import randint
import pygame
from pygame.locals import *

import config.settings as constants
from models.map import Map
from models.syringe import Syringe
from models.characters import Hero, Guard


def get_syringe(window, hero, syringe):
    """ this function checks if the hero passes through the same
    position as an element of the stringe """
    if hero.get_position in syringe.objects_positions:
        obj = syringe.interaction_hero()
        if syringe.check_making():
            message(window, "You made the syringe, find the guardian!", (0, 255, 0), 30)
        else:
            msg = "you have found the {}, keep looking!".format(obj)
            message(window, msg, (255, 255, 255))
    syringe.view_objects(window)

def found_guard(window, hero, guard, syringe):
    """ the function check if the hero passes throught the position of the guard"""
    if hero.get_position == guard.get_position:
        if syringe.check_making():
            message(window, "YOU WIN", (0, 255, 0), 40)
            time.sleep(2)
            quit()      # end of the program
        else:
            lose_img = pygame.image.load(constants.IMG_LOSE).convert_alpha()
            lose_img = pygame.transform.scale\
                (lose_img, (constants.SPRITES_SIZE, constants.SPRITES_SIZE))
            window.blit(lose_img, guard.get_position)
            message(window, "YOU'RE DEAD", (255, 0, 0), 40)
            time.sleep(2)
            game_loop()     # the game reset

def text_objects(text, font, color):
    """ this function returns elements needed for a message """
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()

def message(window, text, color, size=20):
    """" this function allows the message to be printed on screen """
    infoText = pygame.font.Font(None, size)
    textSurf, textRect = text_objects(text, infoText, color)
    textRect.center = ((constants.WINDOW_SIDE/2), (constants.WINDOW_SIDE/2))
    window.blit(textSurf, textRect)
    pygame.display.flip()


def game_loop():
    """ main app in a function so you can call it to restart """
    pygame.init()

    # create pygame window
    window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
    pygame.display.set_caption(constants.WINDOW_TITLE)

    # create map, characters and objects
    mapfile = constants.MAPFILE[randint(0,len(constants.MAPFILE)-1)]
    map = Map(mapfile)
    map.view_map(window)
    hero = Hero(map)
    hero.view_character(window, constants.IMG_HERO)
    guard = Guard(map)
    guard.view_character(window, constants.IMG_GUARD)
    sy = Syringe(map, hero)
    sy.view_objects(window)
    pygame.display.flip()

    game = True

    while game:

        for event in pygame.event.get():

            if event.type == QUIT:
                quit()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    hero.move('right')
                elif event.key == K_LEFT:
                    hero.move('left')
                elif event.key == K_UP:
                    hero.move('up')
                elif event.key == K_DOWN:
                    hero.move('down')

                # reload visuels after event
                map.view_map(window)
                guard.view_character(window, constants.IMG_GUARD)
                hero.view_character(window, constants.IMG_HERO)

                # check hero's interacion with objects and characters
                get_syringe(window, hero, sy)
                found_guard(window, hero, guard, sy)

                pygame.display.flip()       # refresh window with new elements


game_loop()
quit()