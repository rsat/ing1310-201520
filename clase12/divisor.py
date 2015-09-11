# -*- coding: utf-8 -*-
"""
ing1310-201520 11/09/2015 Ricardo Sat
"""


def divisor(n, i):
    if i <= 0:
        return -1

    divisor = 1
    idxDivisor = 1
    while divisor < n:
        if n % divisor == 0:
            if idxDivisor == i:
                return divisor
            idxDivisor += 1
        divisor += 1
    return -1


print divisor(12, 6)
