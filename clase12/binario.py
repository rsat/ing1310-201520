# -*- coding: utf-8 -*-
"""
ing1310-201520 11/09/2015 Ricardo Sat
"""


def binarioADecimal(nb):
    sumaDecimal = 0
    i = 0
    while i < 8:  # o nb > 0:
        b = nb % 10
        nb /= 10
        sumaDecimal += b * 2 ** i
        i += 1
    return sumaDecimal


def bytesADecimal(nb):
    s = ""
    while nb > 0:
        byte = nb % 100000000  # lo mismo que 10**8
        nb /= 100000000  # lo mismo que 10**8
        s += str(binarioADecimal(byte)) + " "
    print s


bytesADecimal(10100101011011011101)
