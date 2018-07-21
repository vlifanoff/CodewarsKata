#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ASCII hex converter: https://www.codewars.com/kata/52fea6fd158f0576b8000089"""


class Converter():
    @staticmethod
    def to_ascii(h):
        return h.decode('hex')

    @staticmethod
    def to_hex(s):
        return ''.join(["{:02x}".format(ord(x)) for x in s])
