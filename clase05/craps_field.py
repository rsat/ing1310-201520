# -*- coding: utf-8 -*-
"""
ing1310-201520 19/08/2015 Ricardo Sat
"""
from numpy import random

montoApuesta = int(raw_input("Ingrese el monto que quiere apostar: "))

d1 = random.randint(1, 7)
d2 = random.randint(1, 7)

print "La combinación de los dados es " + str(d1) + " y " + str(d2)

s = d1 + d2
if (s >= 3 and s <= 4) or (s >= 9 and s <= 11):
    print "Ganaste!", montoApuesta * 2
elif s == 2 or s == 12:
    print "Ganaste!", montoApuesta * 3
else:
    print "Perdiste!"
