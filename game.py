#! /usr/bin/env python3
# coding: utf-8

from models.map import Map
from models.position import Position
from models.syringe import Syringe
from models.characters import Characters, Hero, Guard

map = Map('data/maps/map_test.txt')
hero = Hero(map)
guard = Guard(map)
sy = Syringe(map, hero)

def user_answer():
    user = input("Tapez I(up) J(left) K(down) L(left) Q(quittez)   ")
    user = user.upper()
    if user == "I" :
        hero.move("up")
    elif user == "J":
        hero.move("left")
    elif user == "K":
        hero.move("down")
    elif user == "L":
        hero.move("right")
    print("MacGyver is here : {}".format(hero.get_position))
    return user

user = ""

while user != "Q" :
    user = user_answer()

    if hero.get_position in sy.get_positions:
        print("you have found the {}, keep looking!".format(sy.interaction_hero()))
        if sy.check_making() == True :
            print("Bravo, you have the syringe, find the guardian!")

    if hero.get_position == guard.get_position:
        if sy.check_making() == True :
            print("YOU WIN !!!")
        else :
            print("YOU SHALL NOT PASS !!!")
