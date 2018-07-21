#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Regex validate PIN code: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132"""

import re


def validate_pin(pin):
    return True if re.compile("^(?:\d{4}|\d{6})$").match(pin) else False
