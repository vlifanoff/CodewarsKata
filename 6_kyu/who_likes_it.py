#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Who likes it?: https://www.codewars.com/kata/5266876b8f4bf2da9b000362"""


def likes(names):
    try:
        return {
            1: lambda: "{} likes this".format(*names),
            2: lambda: "{} and {} like this".format(*names),
            3: lambda: "{}, {} and {} like this".format(*names)
        }[len(names)]()
    except:
        try:
            return "{0}, {1} and {2} others like this".format(names[0], names[1], len(names[2:]))
        except:
            return 'no one likes this'
