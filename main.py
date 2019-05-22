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
            msg = "You have found the {}, keep looking!".format(obj)
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

def text_objects(text, font, col):
    """ this function returns elements needed for a message """
    text_surf = font.render(text, True, col)
    return text_surf, text_surf.get_rect()

def message(window, text, col, size=20):
    """" this function allows the message to be printed on screen """
    info_text = pygame.font.Font(None, size)
    text_surf, text_rect = text_objects(text, info_text, col)
    text_rect.center = ((constants.WINDOW_SIDE/2), (constants.WINDOW_SIDE/2))
    window.blit(text_surf, text_rect)
    pygame.display.flip()


def game_loop():
    """ main app in a function so you can call it to restart """
    pygame.init()

    # create pygame window
    window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
    pygame.display.set_caption(constants.WINDOW_TITLE)

    # create map, characters and objects
    mapfile = constants.MAPFILES[randint(0,len(constants.MAPFILES)-1)]
    mase = Map(mapfile)
    mase.view_map(window)
    hero = Hero(mase)
    hero.view_character(window, constants.IMG_HERO)
    guard = Guard(mase)
    guard.view_character(window, constants.IMG_GUARD)
    syr = Syringe(mase, hero)
    syr.view_objects(window)
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
                mase.view_map(window)
                guard.view_character(window, constants.IMG_GUARD)
                hero.view_character(window, constants.IMG_HERO)

                # check hero's interacion with objects and characters
                get_syringe(window, hero, syr)
                found_guard(window, hero, guard, syr)

                pygame.display.flip()       # refresh window with new elements


game_loop()
quit()
