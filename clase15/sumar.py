# -*- coding: utf-8 -*-
"""
ing1310-201520 23/09/2015 Ricardo Sat
"""


def sumar(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        suma += numero
    return suma


def sumarPares(listaNumeros):
    suma = 0
    i = 0
    while i < len(listaNumeros):
        if i % 2 == 0:
            suma += listaNumeros[i]
        i += 1
    return suma


def sumarContenidosPares(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        if numero % 2 == 0:
            suma += numero
    return suma


def listaIndicesContenidosPares(listaNumeros):
    indices = []
    i = 0
    for numero in listaNumeros:
        if numero % 2 == 0:
            indices.append(i)
        i += 1
    return indices


def sumarX(numeros, x):
    suma = 0
    for numero in numeros:
        if numero == x:
            return suma
        suma += numero
    return suma
