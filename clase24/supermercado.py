# -*- coding: utf-8 -*-
"""
ing1310-201520 28/10/2015 Ricardo Sat
"""

from numpy import *

clientes = []
cajas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
identificadorCliente = 0
for t in range(14 * 60):

    nClienteNuevos = random.randint(0, 3 + 1)
    print "En el minuto {} llegaron {} clientes".format(t, nClienteNuevos)

    # llegada de clientes
    for cliente in range(nClienteNuevos):
        identificadorCliente += 1
        nProductos = random.randint(5, 20 + 1)
        tCaja = t + nProductos + random.randint(3, 6 + 1)
        clientes.append({'tiempoLlegada': t,
                         'numeroProductos': nProductos,
                         'tiempoCaja': tCaja,
                         'fueAtendido': False,
                         'identificador': identificadorCliente
                         })
        print "El cliente {0} llevará {1} productos e irá a la caja en el minuto {2}".format(identificadorCliente,
                                                                                             nProductos, tCaja)

    # atención de clientes
    for cliente in clientes:
        if not cliente['fueAtendido'] and t >= cliente['tiempoCaja']:
            for i in range(len(cajas)):
                if t >= cajas[i] and not cliente['fueAtendido']:
                    tEspera = t - cliente["tiempoCaja"]
                    print "El cliente {} fue atendido en el minuto {} y esperó {} minutos".format(
                        cliente['identificador'], t, tEspera)
                    cliente['fueAtendido'] = True
                    cajas[i] = t + cliente['numeroProductos'] * random.randint(1, 3 + 1)
