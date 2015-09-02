# -*- coding: utf-8 -*-
"""
ing1310-201520 02/09/2015 Ricardo Sat

Programa que copia el contenido del archivo original.txt en copia.txt

"""


# con while
original = open("original.txt")
copia = open("copia.txt", "w")


linea = original.readline()

while linea:
    copia.write(linea)
    linea = original.readline()
original.close()
copia.close()


# con for
original = open("original.txt")
copia = open("copia2.txt", "w")

for linea in original:
    copia.write(linea)

original.close()
copia.close()
