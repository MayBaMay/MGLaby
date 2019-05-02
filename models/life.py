#! /usr/bin/env python3
# coding: utf-8

from models.characters import Characters, Hero, Guard

""" Module to determine life esperance of the hero """


class Lifebar :
    """ Each time the hero goes in the guardian case,
    the lifebargoes down till his death! """

    def __init__(self, hero, chances, guard):
        self.hero =  hero
        self.chances = [1]*chances
        self.guard = guard

    def fight(self):
        """ This function lowered the lifebar """
        if self.hero.get_position == self.guard.get_position:
            self.chances.pop()
            return True

    def death(self):
        """This function unfortunately ends the hero's life..."""
        if len(self.chances) == 0:
            return True
