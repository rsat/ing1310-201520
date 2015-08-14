# -*- coding: utf-8 -*-
"""
ing1310-201520 14/08/2015 Ricardo Sat

Programa que simula un cajero automático, donde el usuario
ingresa el monto total a retirar y el programa imprime la cantidad
de billetes que devolvió de cada denominación, intentando siempre
devolver la menor cantidad de billetes. Asuma que el cajero tiene
infinitos billetes, no hay una cantidad máxima a retirar,
no se ingresan montos con monedas y el usuario no comete errores.


Recuerdo:

La siguiente operación:
a = a + 4
es análoga a está
a += 4

y funciona de la misma forma con cualquier operador, es decir,
a = a - 10 <=> a -= 10
a = a * 5  <=> a *= 5
a = a / 7  <=> a /= 7
a = a % 7  <=> a %= 7
a = a ** 3 <=> a **= 3

Y obviamente en vez de utilizar un literal se puede utilizar una variable,
a = 2
b = 10
a = a * b <=> a *= b # el valor de a es igual a 20 despúes de esta línea
"""

montoADevolver = int(raw_input("Ingrese el monto a retirar:"))

billetesVeinte = montoADevolver / 20000
montoADevolver %= 20000  # montoADevolver = montoADevolver % 20000
billetesDiez = montoADevolver / 10000
montoADevolver %= 10000  # montoADevolver = montoADevolver % 10000
billetesCinco = montoADevolver / 5000
montoADevolver %= 5000  # montoADevolver = montoADevolver % 5000
billetesDos = montoADevolver / 2000
montoADevolver %= 2000  # montoADevolver = montoADevolver % 2000
billetesMil = montoADevolver / 1000  # sólo quedan billetes de mil, ya que no existen las monedas

print "Billetes retirados:"
print "20000:", billetesVeinte
print "10000:", billetesDiez
print " 5000:", billetesCinco
print " 2000:", billetesDos
print " 1000:", billetesMil

"""
A modo de compresión, lo que el usuario retiró estará dado por
billetesVeinte * 20000 + billetesDiez * 10000 + billetesCinco * 5000 + billetesDos * 2000 + billetesMil * 1000

"""

# Segunda forma de hacerlo sin ocupar módulo(%)
print "Realizando el mismo flujo de antes pero con otra lógica"

montoADevolver = int(raw_input("Ingrese el monto a retirar:"))
# calculámos la cantidad de billetes de 20 que podemos devolver
billetesVeinte = montoADevolver / 20000
# le restamos al monto que nos queda por devolver,
# la cantidad de billetes de veinte que vamos a devolver
montoADevolver -= billetesVeinte * 20000  # montoADevolver = montoADevolver - billetesVeinte*20000
# ocupamos la misma lógica anterior pero para billetes de 10
billetesDiez = montoADevolver / 10000
montoADevolver -= billetesDiez * 10000  # montoADevolver = montoADevolver - billetesDiez*10000
# ocupamos la misma lógica anterior pero para billetes de 5
billetesCinco = montoADevolver / 5000
montoADevolver -= billetesCinco * 5000  # montoADevolver = montoADevolver - billetesCinco*5000
# ocupamos la misma lógica anterior pero para billetes de 2
billetesDos = montoADevolver / 2000
montoADevolver -= billetesDos * 2000  # montoADevolver = montoADevolver - billetesCinco*5000
# sólo quedan billetes de mil, ya que no existen las monedas
billetesMil = montoADevolver / 1000

print "Billetes retirados:"
print "20000:", billetesVeinte
print "10000:", billetesDiez
print " 5000:", billetesCinco
print " 2000:", billetesDos
print " 1000:", billetesMil
