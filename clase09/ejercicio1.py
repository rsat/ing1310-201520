# -*- coding: utf-8 -*-
"""
ing1310-201520 02/09/2015 Ricardo Sat
"""

original = open("original.txt")
copia = open("copia.txt", "w")

"""
linea = original.readline()

while linea:
    copia.write(linea)
    linea = original.readline()
original.close()
copia.close()
"""

for linea in original:
    copia.write(linea)

original.close()
copia.close()
