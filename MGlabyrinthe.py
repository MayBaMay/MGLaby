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

    if isinstance(sy.componants["needle"][0], Position):
        window.blit(needle_img, needle_pos)
    if isinstance(sy.componants["ether"][0], Position):
        window.blit(ether_img, ether_pos)
    if isinstance(sy.componants["tube"][0], Position):
        window.blit(tube_img, tube_pos)


def found_guard():
    if hero.get_position == guard.get_position:
        if sy.check_making() == True :
            message ("YOU WIN", (255,255,255))
        else :
            return ("YOU'RE DEAD", (255,0,0))
            game = 0

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message(text, color):
    infoText = pygame.font.Font(None,40)
    TextSurf, TextRect = text_objects(text, infoText, color)
    TextRect.center = ((constants.WINDOW_SIDE/2),(constants.WINDOW_SIDE/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()

    # time.sleep(2) # ralenti à refresh perso pas à message!!!


pygame.init()

# create pygame window
window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
pygame.display.set_caption(constants.WINDOW_TITLE)

# set map
map = Map(constants.MAPFILE)

# set walls
wall_img = pygame.image.load(constants.IMG_WALL).convert()
wall_img = pygame.transform.scale(wall_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
for position in map._walls :
    wall_pos = position.get_position
    window.blit(wall_img, wall_pos)
# set floor
paths_img = pygame.image.load(constants.IMG_FLOOR).convert()
paths_img = pygame.transform.scale(paths_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
for position in map._paths :
    path_pos = position.get_position
    window.blit(paths_img, path_pos)
#  set start case
start_img = pygame.image.load(constants.IMG_START).convert()
start_img = pygame.transform.scale(start_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
start_pos = map.start.get_position
window.blit(start_img, (0,0))

pygame.display.flip()

# set hero
hero = Hero(map)
hero_img = pygame.image.load(constants.IMG_HERO).convert_alpha()
pygame.display.set_icon(hero_img)
hero_img = pygame.transform.scale(hero_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
hero_pos = hero.get_position
window.blit(hero_img, hero_pos)

# set guardian
guard = Guard(map)
# view guard
guard_img = pygame.image.load(constants.IMG_GUARD).convert_alpha()
guard_img = pygame.transform.scale(guard_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
guard_pos = guard.get_position
window.blit(guard_img, guard_pos)

# set Syringe
sy = Syringe(map, hero)
# view needle
needle_img = pygame.image.load(constants.IMG_NEEDLE).convert_alpha()
needle_img = pygame.transform.scale(needle_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
needle_pos = sy.componants["needle"][0].get_position
window.blit(needle_img, needle_pos)
# view ether
ether_img = pygame.image.load(constants.IMG_ETHER).convert()
ether_img.set_colorkey((1,1,1))
ether_img = pygame.transform.scale(ether_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
ether_pos = sy.componants["ether"][0].get_position
window.blit(ether_img, ether_pos)
# view tube
tube_img = pygame.image.load(constants.IMG_TUBE).convert()
tube_img.set_colorkey((255,255,255))
tube_img = pygame.transform.scale(tube_img, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
tube_pos = sy.componants["tube"][0].get_position
window.blit(tube_img, tube_pos)

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

    # reset the map
    for position in map.walls :
        wall_pos = position
        window.blit(wall_img, wall_pos)
    for position in map.paths :
        path_pos = position
        window.blit(paths_img, path_pos)
    start_pos = map.start.get_position
    window.blit(start_img, start_pos)

    # reset hero(new position) & guard
    hero_pos = hero.get_position
    window.blit(guard_img, guard_pos)
    window.blit(hero_img, hero_pos)

    pygame.display.update()

    get_syringe()
    found_guard()

    pygame.display.update()       # refresh window

game_loop()
pygame.quit()
quit()
