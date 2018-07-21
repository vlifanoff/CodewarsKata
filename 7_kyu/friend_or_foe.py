#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Friend or Foe?: https://www.codewars.com/kata/55b42574ff091733d900002f"""


def friend(x):
    return [x for x in x if len(x) == 4]
