import matplotlib.pyplot as plt
import numpy as np
import math

def derivada(t, y):
    
    return -2*y

def solucion_exacta(t):
    return math.exp(-2*t)

print(derivada(0, 1))
print(solucion_exacta(0))
  