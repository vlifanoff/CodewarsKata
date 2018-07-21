#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get Planet Name By ID: https://www.codewars.com/kata/515e188a311df01cba000003"""

planets = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune",
}


def get_planet_name(id):
    try:
        return planets[id]
    except KeyError:
        return ''
