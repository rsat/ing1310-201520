# -*- coding: utf-8 -*-
"""
ing1310-201520 06/11/2015 Ricardo Sat
"""
from numpy import *


def apocalipsisZombie(nZombies, nHumanos, modZombies, modHumanos):
    tProximaPelea = nZombies / nHumanos
    while nZombies > 0 and nHumanos > 0:
        expZombie = random.randint(101) + modZombies
        expHumano = random.randint(101) + modHumanos
        if expHumano > expZombie:
            r = random.random()
            nZombies -= 1
            if r > 0.5:
                # lo transforma
                nHumanos += 1
        else:
            nHumanos -= 1
        if nZombies > 0 and nHumanos > 0:
            tProximaPelea = tProximaPelea + nZombies / nHumanos
    print "El apocalipsis duró", tProximaPelea, "horas"


apocalipsisZombie(10, 10, 20, 10)
