""" programm constants """

# Windows config
SPRITES_NB = 15
SPRITES_SIZE = 40
WINDOW_SIDE = SPRITES_NB * SPRITES_SIZE
LAST_POS = WINDOW_SIDE - SPRITES_SIZE
WINDOW_TITLE = "MacGiver's Adventures!"

MAPFILE = ['data/maps/map.txt', 'data/maps/map2.txt']

# Maze SHAPE
START_GAME = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'

# Images adress
# Map:
IMG_FLOOR = "ressources/map/floor-stone-tiles.png"
IMG_WALL = "ressources/map/wall-stone-tiles.png"
IMG_START = "ressources/map/start-tiles.png"

# Characters:
IMG_HERO = "ressources/MacGyver.png"
IMG_GUARD = "ressources/Gardien.png"
# Syringe:
IMG_NEEDLE = "ressources/syringe/aiguille.png"
IMG_TUBE = "ressources/syringe/tube_plastique.png"
IMG_ETHER = "ressources/syringe/ether.png"

# + :
IMG_LOSE = "ressources/You_lose.png"
