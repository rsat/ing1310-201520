# -*- coding: utf-8 -*-
"""
ing1310-201520 30/10/2015 Ricardo Sat

Simular la urgencia de un hospital, donde llegan pacientes desde las 08:00 hrs
hasta las 18:00 hrs y se cierra una vez que se hayan atentido todos. Cada
minuto existe 20% probabilidad de que llegue un paciente nuevo. Cuando llega
un paciente tiene un 60% de que sea de prioridad baja, un 30% de prioridad media
y un 10% de prioridad alta. La atención de pacientes se realiza por prioridad, y si
existen dos pacientes con la misma prioridad, se atiende el que llegó primero.

Existen 5 doctores que atienden, donde cada uno demora un rango entre 1 y 5 minutos
en atender a un paciente de prioridad baja, 5 a 10 minutos uno de prioridad media,
y por último, entre 10 y 20 para uno de prioridad alta.

Imprima al final de la simulación cual fue el tiempo de atención promedio de cada doctor

"""

from numpy import *

t = 0
quedanPacientes = True
bajos = []
medios = []
altos = []
doctores = [0, 0, 0, 0, 0]

# esto es para contar el tiempo de atencion de los doctores
# y cuantos pacientes atendieron
doctoresTiempo = [0, 0, 0, 0, 0]
doctoresPacientes = [0, 0, 0, 0, 0]

while t < (18 - 6) * 60 or quedanPacientes:

    if t < (18 - 6) * 60:  # la llegada de pacientes ocurre entre ese horario
        r = random.random()
        if r < 0.2:
            r2 = random.random()
            if r2 < 0.6:
                bajos.append(1)
            elif r2 < 0.9:
                medios.append(1)
            else:
                altos.append(1)

    for i in range(len(doctores)):
        if doctores[i] <= t:
            if len(altos) > 0:
                paciente = altos.pop(0)
                tiempoPaciente = random.randint(10, 20 + 1)
                doctores[i] = t + tiempoPaciente
                # acumulamos los tiempos de atencion de cada doctor
                doctoresTiempo[i] += tiempoPaciente
                # contamos cuantos pacientes ha atendido cada doctor
                doctoresPacientes[i] += 1

    for i in range(len(doctores)):
        if doctores[i] <= t:
            if len(medios) > 0:
                paciente = medios.pop(0)
                tiempoPaciente = random.randint(5, 10 + 1)
                doctores[i] = t + tiempoPaciente
                doctoresTiempo[i] += tiempoPaciente
                doctoresPacientes[i] += 1

    for i in range(len(doctores)):
        if doctores[i] <= t:
            if len(bajos) > 0:
                paciente = bajos.pop(0)
                tiempoPaciente = random.randint(1, 5 + 1)
                doctores[i] = t + tiempoPaciente
                doctoresTiempo[i] += tiempoPaciente
                doctoresPacientes[i] += 1

    if len(altos) == 0 and len(medios) == 0 and len(bajos) == 0:
        quedanPacientes = False

    t += 1

for i in range(len(doctores)):
    if doctoresPacientes[i] > 0:
        print "Tiempo promedio de atención para Doctor", i + 1, float(doctoresTiempo[i]) / doctoresPacientes[
            i], "minutos"
