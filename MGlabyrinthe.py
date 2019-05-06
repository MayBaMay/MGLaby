"""

MacGyver Labyrinthe:
Étant un grand fan de Richard Dean Anderson, vous imaginez un
labyrinthe 2D dans lequel MacGyver aurait été enfermé.
La sortie est surveillée par un garde du corps dont la coiffure
ferait pâlir Tina Turner. Pour le distraire, il vous faut réunir les
éléments suivants (dispersés dans le labyrinthe) : une aiguille, un
petit tube en plastique et de l'éther. Ils permettront à MacGyver de
créer une seringue et d'endormir notre garde.

Script Python
Fichiers : à modifier
"""

import pygame
from pygame.locals import *

import config.settings as constants
from models.map import Map
from models.position import Position
from models.syringe import Syringe
from models.characters import Characters, Hero, Guard
from models.life import Lifebar

print(((constants.WINDOW_SIDE),(constants.WINDOW_SIDE)))

def get_syringe():
    if hero.get_position in sy.get_positions:
        print("you have found the {}, keep looking!".format(sy.interaction_hero()))
        if sy.check_making() == True :
            print("Bravo, you have the syringe, find the guardian!")

    if isinstance(sy.componants["needle"][0], Position):
        window.blit(needle_icon, needle_pos)
    if isinstance(sy.componants["ether"][0], Position):
            window.blit(ether_icon, ether_pos)
    if isinstance(sy.componants["tube"][0], Position):
            window.blit(tube_icon, tube_pos)


def found_guard():
    if hero.get_position == guard.get_position:
        if sy.check_making() == True :
            return "win"
        else :
            return "dead"

def win_loose(IMG):
    win_icon = pygame.image.load(IMG).convert()
    win_icon.set_colorkey((1,1,1))
    win_size = int(constants.WINDOW_SIDE/2)
    win_coord = (int(win_size/2), int(win_size/2))
    win_icon = pygame.transform.scale(win_icon, (win_size, win_size))
    window.blit(IMG, win_coord)

pygame.init()


# create pygame window
window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
pygame.display.set_caption(constants.WINDOW_TITLE)

# set map
map = Map(constants.MAPFILE)

wall_icon = pygame.image.load(constants.IMG_WALL).convert()
wall_icon = pygame.transform.scale(wall_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
for position in map._walls :
    wall_pos = position.get_position
    window.blit(wall_icon, wall_pos)
paths_icon = pygame.image.load(constants.IMG_FLOOR).convert()
paths_icon = pygame.transform.scale(paths_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
for position in map._paths :
    path_pos = position.get_position
    window.blit(paths_icon, path_pos)

pygame.display.flip()

# set hero
hero = Hero(map)
hero_icon = pygame.image.load(constants.IMG_HERO).convert_alpha()
hero_icon = pygame.transform.scale(hero_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
hero_pos = hero.get_position
window.blit(hero_icon, hero_pos)

# set guardian
guard = guard = Guard(map)
guard_icon = pygame.image.load(constants.IMG_GUARD).convert_alpha()
guard_icon = pygame.transform.scale(guard_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
guard_pos = guard.get_position
window.blit(guard_icon, guard_pos)

# set Syringe
sy = Syringe(map, hero)
needle_icon = pygame.image.load(constants.IMG_NEEDLE).convert_alpha()
needle_icon = pygame.transform.scale(needle_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
needle_pos = sy.componants["needle"][0].get_position
window.blit(needle_icon, needle_pos)
ether_icon = pygame.image.load(constants.IMG_ETHER).convert()
ether_icon.set_colorkey((1,1,1))
ether_icon = pygame.transform.scale(ether_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
ether_pos = sy.componants["ether"][0].get_position
window.blit(ether_icon, ether_pos)
tube_icon = pygame.image.load(constants.IMG_TUBE).convert()
tube_icon.set_colorkey((255,255,255))
tube_icon = pygame.transform.scale(tube_icon, (constants.SPRITES_SIZE,constants.SPRITES_SIZE))
tube_pos = sy.componants["tube"][0].get_position
window.blit(tube_icon, tube_pos)


pygame.display.flip()
game = True

while game:
    pygame.time.Clock().tick(30)

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

    for position in map._walls :
        wall_pos = position.get_position
        window.blit(wall_icon, wall_pos)
    for position in map._paths :
        path_pos = position.get_position
        window.blit(paths_icon, path_pos)

    get_syringe()

    hero_pos = hero.get_position
    window.blit(guard_icon, guard_pos)
    window.blit(hero_icon, hero_pos)
    if found_guard() == "win":
        win_loose(constants.IMG_WIN)
    elif found_guard() == "dead":
        win_loose(constants.IMG_LOSE)

    pygame.display.flip()
