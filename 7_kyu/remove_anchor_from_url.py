#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remove anchor from URL: https://www.codewars.com/kata/51f2b4448cadf20ed0000386"""


def remove_url_anchor(url):
    return url.partition('#')[0]
