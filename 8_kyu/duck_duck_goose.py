#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Duck Duck Goose: https://www.codewars.com/kata/582e0e592029ea10530009ce"""


def duck_duck_goose(ducks, goose):
    return ducks[(goose - 1) % len(ducks)].name
