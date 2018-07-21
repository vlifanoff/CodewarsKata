#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IPv4 Validator: https://www.codewars.com/kata/57193694938fcdfe3a001dd7"""


def ipValidator(ip):
    return ip.count('.') == 3 and all(x.isdigit() and 0 <= int(x) < 256 for x in ip.split('.'))
