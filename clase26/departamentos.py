# -*- coding: utf-8 -*-
"""
ing1310-201520 06/11/2015 Ricardo Sat
"""

from numpy import *

departmentos = []

for d in range(12 * 3):
    departmentos.append({"inicio": random.randint(1, 3 + 1), "valor": random.randint(200000, 500001)})

montoRecaudado = 0
costos = 0
m = 1
mInversionInicial = None
numeroArrendatariosTotales = 0
tiempoTotal = 0
while montoRecaudado < 4000000000 + costos:

    # recaudar renta
    for departmento in departmentos:
        if departmento["inicio"] <= m:
            montoRecaudado += departmento["valor"]

    # ver si la persona se va
    for departmento in departmentos:
        # si lleva mas de 12 meses tiene la posibilidad de irse
        if m - departmento["inicio"] > 12:
            r = random.randint(100)
            if r < 5:
                # para estadisticas
                tiempoTotal += m - departmento["inicio"]
                numeroArrendatariosTotales += 1

                costos += random.randint(100000, 300001)
                departmento['inicio'] = m + random.randint(1, 3 + 1)
                departmento['valor'] = random.randint(200000, 500001)

    if not mInversionInicial and montoRecaudado >= 4000000000:
        mInversionInicial = m

    m += 1

print "Tiempo en recuperar inversión total", m
print "Tiempo en recuperar inversión inicial", mInversionInicial
print "Tiempo promedio de arriendo", float(tiempoTotal) / numeroArrendatariosTotales
