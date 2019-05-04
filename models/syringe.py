
""" This module generate elements for the syringe
MacGyver has to make it with a needle, a small plastic cube and ether
Those elements will be found on the map randomly
They will be used to distract the guard at the exit door"""

from random import randrange

import config.settings as constants
from models.map import Map
from models.position import Position
from models.characters import Characters, Hero, Guard


class Syringe:
    """Generate the elements for the syringe"""

    def __init__(self, map, hero):
        self.map = map
        self.hero = hero
        self.objects = ['needle', 'cube', 'ether']
        self.componants = {}
            # form self.componants will be :
            # {needle : [position , flag], cube : [position , flag] , ether : [position , flag]}
        self.syringe = False

        self.place_componants()

    def place_componants(self):
        """ Instanciation of syringe's componants :
        They shouldn't be outside a path neither then at the same place
        of an other """
        places  = []            # used positions checking list
        for object in self.objects :
            while 1 :
                randrange_x = randrange(0, constants.LAST_POS, constants.SPRITES_SIZE)
                randrange_y = randrange(0, constants.LAST_POS, constants.SPRITES_SIZE)
                place = Position(randrange_x,randrange_y)
                if place != Position(0,0):
                    if place != self.map.exit:
                        if place in self.map :
                            if place not in places :
                                break
            places.append(place)
            infos = [place, False]
            self.componants[object] = infos

    @property
    def get_positions(self):
        """ return all the class_objects positions"""
        pos = []
        for object in self.objects :
            pos.append(self.componants[object][0])
        return pos

    @property
    def get_flags(self):
        """ return flags allowing to see if the hero passed through the case already"""
        flags = []
        for object in self.objects :
            flags.append(self.componants[object][1])
        return flags

    def interaction_hero(self):
        """ if componant is on the same position as the hero, componant removed from the list"""
        for componant, info in self.componants.items() :
            if info[0] == self.hero.get_position :
                self.componants[componant] = ['off', True]
                return componant

    def check_making(self):
        """ check all the componant have been picked up"""
        flags = self.get_flags
        if False not in flags :
            self.syringe = True
            return True

def main():
    game = Map('data/maps/map_test.txt')
    mg = Hero(game)
    sy = Syringe(game, mg)

    print (constants.LAST_POS)
    print(constants.SPRITES_SIZE)
    print(sy.get_positions)
    print(mg.get_position)

    # print("au début MG is :{}".format(mg.get_position))
    # print(sy.get_positions)
    # print(sy.get_flags)
    # print(sy.interaction_hero())
    # print(sy.get_positions)
    # print(sy.get_flags, '\n')
    # print(sy.check_making())

    # mg.move("right")
    # print(mg.get_position)
    # print(sy.get_positions)
    # print(sy.get_flags)
    # print(sy.interaction_hero())
    # print(sy.get_positions)
    # print(sy.get_flags, '\n')
    # print(sy.check_making())
    #
    # mg.move("right")
    # print(mg.get_position)
    # mg.move("right")
    # print(mg.get_position)
    # mg.move("right")
    # print(mg.get_position)

if __name__ == "__main__":
    main()
