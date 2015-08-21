# -*- coding: utf-8 -*-
"""
ing1310-201520 19/08/2015 Ricardo Sat

Programa que permite a dos personas jugar el cachipun
de Big Bang Theory, pidiéndole a cada uno su jugada y
luego imprimiendo quien ganó la partida.


"""

j1 = raw_input("Jugador 1, ingrese su jugada: ")
j2 = raw_input("Jugador 2, ingrese su jugada: ")

if j1 == j2:
    print "Empate!"
elif j1 == "spock" and (j2 == "scissors" or j2 == "rock"):
    print "Ganó Jugador 1"
elif j1 == "scissors" and (j2 == "paper" or j2 == "lizard"):
    print "Ganó Jugador 1"
elif j1 == "rock" and (j2 == "scissors" or j2 == "lizard"):
    print "Ganó Jugador 1"
elif j1 == "lizard" and (j2 == "spock" or j2 == "paper"):
    print "Ganó Jugador 1"
elif j1 == "paper" and (j2 == "spock" or j2 == "rock"):
    print "Ganó Jugador 1"
else:
    print "Ganó Jugador 2"
