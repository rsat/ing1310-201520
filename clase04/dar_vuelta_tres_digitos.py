# -*- coding: utf-8 -*-
"""
ing1310-201520 14/08/2015 Ricardo Sat

Programa que solicita un número de tres dígitos y lo imprime al revés
"""

numeroOriginal = int(raw_input("Ingrese número de tres dígitos:"))

c = numeroOriginal % 10
numeroOriginal /= 10  # numeroOriginal = numeroOriginal / 10
b = numeroOriginal % 10
numeroOriginal /= 10  # numeroOriginal = numeroOriginal / 10
a = numeroOriginal

print str(c) + str(b) + str(a)
