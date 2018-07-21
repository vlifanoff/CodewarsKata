#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sort Numbers: https://www.codewars.com/kata/5174a4c0f2769dd8b1000003"""


def solution(nums):
    if not nums:
        return []
    nums.sort()
    return nums
