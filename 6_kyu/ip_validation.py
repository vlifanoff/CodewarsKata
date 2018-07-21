#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IP Validation: https://www.codewars.com/kata/515decfd9dcfc23bb6000006"""


def is_valid_IP(ip):
    if ip.count('.') != 3:
        return False

    ip_nums = ip.split('.')
    if all(len(x) == 1 or (1 < len(x) <= 3 and not x.startswith('0')) for x in ip_nums):
        if all(x.isdigit() and 0 <= int(x) < 256 for x in ip_nums):
            return True

    return False
