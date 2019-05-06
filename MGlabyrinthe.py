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

map = Map('data/maps/map_test.txt')
hero = Hero(map)


pygame.init()


window = pygame.display.set_mode((constants.WINDOW_SIDE, constants.WINDOW_SIDE))
pygame.display.set_caption(constants.WINDOW_TITLE)

fond = pygame.image.load("ressources/background.jpg").convert()
window.blit(fond, (0,0))

pygame.display.flip()

hero = Hero(map)
hero_icon = pygame.image.load("ressources/MacGyver.png").convert_alpha()
hero_icon = pygame.transform.scale(hero_icon, (20,20))
hero_pos = hero.get_position
window.blit(hero_icon, hero_pos)
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

    hero_pos = hero.get_position
    window.blit(fond, (0,0))
    window.blit(hero_icon, hero_pos)
    pygame.display.flip()
