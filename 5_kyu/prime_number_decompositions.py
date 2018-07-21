#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Prime number decompositions: https://www.codewars.com/kata/53c93982689f84e321000d62"""


def getPrimeFactor(n):
    for i in range(2, n):
        if n % i == 0:
            return int(i)

    return n


def getAllPrimeFactors(n):
    if n is None: return []
    if not isinstance(n, int): return []
    if n < 1: return []
    if n == 1: return [n]

    f = []
    n = int(n)

    while n > 1:
        f.append(getPrimeFactor(n))
        n /= f[len(f) - 1]

    return f


def getUniquePrimeFactorsWithCount(n):
    tmp = {}

    for x in getAllPrimeFactors(n):
        if x in tmp.keys():
            tmp[x] += 1
        else:
            tmp[x] = 1

    unique = []
    rp = []

    for key in sorted(tmp):
        unique.append(key)
        rp.append(tmp[key])

    return [unique, rp]


def getUniquePrimeFactorsWithProducts(n):
    unique, rp = getUniquePrimeFactorsWithCount(n)
    return [unique[i] ** rp[i] for i in range(len(unique))]
