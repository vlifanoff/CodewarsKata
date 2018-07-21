#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Two fighters, one winner: https://www.codewars.com/kata/577bd8d4ae2807c64b00045b"""


def declare_winner(fighter1, fighter2, first_attacker):
    current_attacker, current_attacked = fighter1, fighter2

    if current_attacker.name != first_attacker:
        current_attacker, current_attacked = fighter2, fighter1

    while True:
        current_attacked.health -= current_attacker.damage_per_attack
        if current_attacked.health < 1:
            return current_attacker.name
        current_attacker, current_attacked = current_attacked, current_attacker
