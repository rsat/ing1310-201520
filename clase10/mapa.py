# -*- coding: utf-8 -*-
"""
ing1310-201520 04/09/2015 Ricardo Sat

Problema basado en el ejercicio 2 de la clase 10 (4 de septiembre)
No chequea que los tanques estén dentro del mapa

"""
tanque = open("tanque.txt")

w = int(tanque.readline())
h = int(tanque.readline())
x1 = int(tanque.readline())
y1 = int(tanque.readline())
x2 = int(tanque.readline())
y2 = int(tanque.readline())

s = ""
r = 0
while r < h + 2:
    c = 0
    while c < w + 2:
        if r == 0 or r == h + 2 - 1:  # primera y última fila
            s += "**"
        elif c == 0:  # primera columna
            s += "* "
        elif c == w + 2 - 1:
            s += " *"
        else:
            if r == y2 + 1 and c == x2 + 1:
                s += "T2"
            elif r == y1 + 1 and c == x1 + 1:
                s += "T1"
            else:  # elif (r != y1 + 1 and c != x1 + 1) or (r != y2 + 1 and c != x2 + 1):
                s += "  "
        c += 1
    s += "\n"
    r += 1

print s
