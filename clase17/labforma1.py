# -*- coding: utf-8 -*-
"""
ing1310-201520 30/09/2015 Ricardo Sat
"""


def maximaDistanciaAdyacente(lista):
    lista2 = []
    i = 1
    while i < len(lista):
        distancia = lista[i - 1] - lista[i]
        if distancia < 0:
            distancia = -distancia
        lista2.append(distancia)
        i += 1
    lista2.sort()
    return lista2[-1]
