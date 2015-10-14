# -*- coding: utf-8 -*-
"""
ing1310-201520 14/10/2015 Ricardo Sat
"""

from numpy import *


def dec2Bin(n):
    nDigitos = int(log(n) / log(2) + 1)
    b = arange(nDigitos - 1, -1, -1)
    b = 2 ** b
    print (n / b) % 2


def dec2Base(n, base):
    nDigitos = int(log(n) / log(base) + 1)
    b = arange(nDigitos - 1, -1, -1)
    b = base ** b
    print (n / b) % base
