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

    return tiempos, valores

print(metodo_euler(0, 1, 0.2, 5))

tiempos, valores = metodo_euler(0, 1, 0.2, 5)

def comparar_soluciones(tiempos, valores):
    exactos = []
    errores = []

    for t, y_euler in zip(tiempos, valores):
        solucion_exacta_valor = solucion_exacta(t)

        # Calcula el error absoluto
        error =  abs(y_euler - solucion_exacta_valor)
        # Guarda ambos resultados
        exactos.append(solucion_exacta_valor)
        errores.append(error)

    return exactos, errores

exactos, errores = comparar_soluciones(tiempos, valores)

print(f"Exactos: {exactos}, Errores: {errores}")


plt.figure(figsize=(8, 5))

# Dibuja la solución exacta
plt.plot(tiempos, exactos, label="solución exacta", color="blue", marker="o")
# Dibuja los puntos aproximados de Euler
plt.plot(tiempos, valores, label="aproximación de Euler", color="yellow", marker="o")
# Agrega título y etiquetas a los ejes
plt.title("Comparación de la solución exacta y la aproximación de Euler")
plt.xlabel("tiempo (t)")
plt.ylabel("valor de y")
# Activa una leyenda y una cuadrícula
plt.legend()
plt.grid()
plt.show()
  