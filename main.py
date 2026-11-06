import matplotlib.pyplot as plt
import numpy as np
import math

def derivada(t, y):
    
    return -2*y

def solucion_exacta(t):
    return math.exp(-2*t)

print(derivada(0, 1))
print(solucion_exacta(0))
  


def metodo_euler(t0, y0, h, pasos):
    tiempos = [t0]
    valores = [y0]

    t = t0
    y = y0

    for i in range(pasos):
        
        y = y + h * derivada(t, y)

        t = t + h

        tiempos.append(t)
        valores.append(y)

        pass

    return tiempos, valores

print(metodo_euler(0, 1, 0.2, 5))

