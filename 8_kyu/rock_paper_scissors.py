#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rock Paper Scissors!: https://www.codewars.com/kata/5672a98bdbdd995fad00000f"""


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'

    if (p1 == 'scissors' and p2 == 'paper') or \
            (p1 == 'paper' and p2 == 'rock') or \
            (p1 == 'rock' and p2 == 'scissors'):
        return "Player 1 won!"

    return "Player 2 won!"
