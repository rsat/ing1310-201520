# -*- coding: utf-8 -*-
"""
ing1310-201520 30/09/2015 Ricardo Sat
"""


def productoPuntoImpar(a, b):
    suma = 0
    if len(a) != len(b):
        return 0

    for i in range(len(a)):
        if i % 2 != 0:
            suma += a[i] * b[i]
    return suma


def productoPuntoImpar2(a, b):
    suma = 0
    if len(a) != len(b):
        return 0

    for i in range(1, len(a), 2):
        suma += a[i] * b[i]
    return suma


def existePalabraRepetida(s):
    palabras = s.split()
    for palabra in palabras:
        if palabras.count(palabra) > 1:
            return True
    return False


print existePalabraRepetida("El perro es verde")
