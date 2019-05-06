#! /usr/bin/env python3
# coding: utf-8

"""
MacGyver Labyrinthe:
Étant un grand fan de Richard Dean Anderson, vous imaginez un
labyrinthe 2D dans lequel MacGyver aurait été enfermé.
La sortie est surveillée par un garde du corps dont la coiffure
ferait pâlir Tina Turner. Pour le distraire, il vous faut réunir les
éléments suivants (dispersés dans le labyrinthe) : une aiguille, un
petit tube en plastique et de l'éther. Ils permettront à MacGyver de
créer une seringue et d'endormir notre garde.

Script Python 3.7.2
Fichiers : à modifier
"""

import pygame
from pygame.locals import *
import time

import config.settings as constants
from models.map import Map
from models.position import Position
from models.syringe import Syringe
from models.characters import Characters, Hero, Guard


def get_syringe():
    if hero.get_position in sy.objects_positions:
        if sy.check_making() == True :
            message( "Bravo, you have the syringe, find the guardian!", (255,255,255))
        else :
            msg = "you have found the {}, keep looking!".format(sy.interaction_hero())
            message(msg, (255,255,255))
    sy.view_objects(window)


def found_guard():
    if hero.get_position == guard.get_position:
        if sy.check_making() == True :
            message ("YOU WIN", (255,255,255))
        else :
            message ("YOU'RE DEAD", (255,0,0))
            lose_img = pygame.image.load(constants.IMG_LOSE).convert_alpha()
            lose_img = pygame.transform.scale(lose_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
            window.blit(lose_img, guard.get_position)
            # time.sleep(2) # ralenti à bouge le perso alors  qu'avant dans le code
            quit()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message(text, color):
    infoText = pygame.font.Font(None,40)
    TextSurf, TextRect = text_objects(text, infoText, color)
    TextRect.center = ((constants.WINDOW_SIDE/2),(constants.WINDOW_SIDE/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()

    #time.sleep(2) # ralenti à refresh perso pas à message!!!

pygame.init()

# create pygame window
window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
pygame.display.set_caption(constants.WINDOW_TITLE)

# set map
map = Map(constants.MAPFILE)
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
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():

        if event.type == QUIT:
            game = 0

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.move('right')
            elif event.key == K_LEFT:
                hero.move('left')
            elif event.key == K_UP:
                hero.move('up')
            elif event.key == K_DOWN:
                hero.move('down')

    map.view_map(window)
    guard.view_character(window, constants.IMG_GUARD)
    hero.view_character(window, constants.IMG_HERO)

    get_syringe()
    found_guard()

    pygame.display.update()       # refresh window
