
#! /usr/bin/env python3
# coding: utf-8

from models.map import Map
from models.position import Position
from models.syringe import Syringe
from models.characters import Characters, Hero, Guard
from models.life import Lifebar

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

def get_syringe():
    if hero.get_position in sy.get_positions:
        print("you have found the {}, keep looking!".format(sy.interaction_hero()))
        if sy.check_making() == True :
            print("Bravo, you have the syringe, find the guardian!")

def check_syringe():
    if sy.check_making() == True :
        print("YOU WIN !!!")
        return "Q"

def battle():
    if life.fight():
        if life.death():
            print("YOU'RE DEAD, GAME OVER ")
            return "dead"


map = Map('data/maps/map_test.txt')
hero = Hero(map)
guard = Guard(map)
sy = Syringe(map, hero)
life = Lifebar(hero, 5, guard)
user = ""
print("seringe ", sy.get_positions)

while user != "Q" :
    user = user_answer()
    if hero.get_position in sy.get_positions:
        print("putain!")
    get_syringe()
    if hero.get_position == guard.get_position:
        if check_syringe() :
            user = "Q"
        elif battle() == "dead":
            user = "Q"
        else :
            print("YOU SHALL NOT PASS !!! You have {} chances left". format(len(life.chances)))
