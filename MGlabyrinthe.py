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

pygame.init()



# create pygame window
window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
pygame.display.set_caption(constants.WINDOW_TITLE)

# set map
map = Map('data/maps/map_test.txt')

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
print (map.exit)

pygame.display.flip()
continuer = True

while continuer:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():

        if event.type == QUIT:
            continuer_jeu = 0
            continuer = 0

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.move('right')
                print(hero.get_position)
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
    hero_pos = hero.get_position
    window.blit(guard_icon, guard_pos)
    window.blit(hero_icon, hero_pos)
    pygame.display.flip()
