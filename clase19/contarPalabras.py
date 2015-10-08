# -*- coding: utf-8 -*-
"""
ing1310-201520 07/10/2015 Ricardo Sat
"""


# como lo habríamos hecho sin diccionarios
def contarPalabras2(s):
    palabras = s.split()
    palabras.sort()
    suma = 0
    palabraAnterior = palabras[0]
    for i in range(len(palabras)):
        if palabras[i] != palabraAnterior:
            print palabraAnterior, suma
            palabraAnterior = palabras[i]
            suma = 1
        else:
            suma += 1
    print palabraAnterior, suma


contarPalabras2("ayer ayer como como estas estas fui fui hola saa saa")


def contarPalabras(s):
    cPalabras = {}
    palabras = s.split()
    for palabra in palabras:
        if palabra not in cPalabras:
            cPalabras[palabra] = 1
        else:
            cPalabras[palabra] += 1

    palabras = cPalabras.keys()
    palabras.sort()
    for palabra in palabras:
        print palabra, ":", cPalabras[palabra]


contarPalabras("hola como estas")


def contarLetras(s):
    cPalabras = {}
    for letra in s:
        if letra != " ":
            if letra not in cPalabras:
                cPalabras[letra] = 1
            else:
                cPalabras[letra] += 1

    palabras = cPalabras.keys()
    palabras.sort()
    for palabra in palabras:
        print palabra, ":", cPalabras[palabra]


contarLetras("hola como estas")
