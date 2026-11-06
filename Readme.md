# Resolución de una ecuación diferencial mediante separación de variables y el método de Euler

## Descripción

Este proyecto presenta la resolución de una ecuación diferencial ordinaria (EDO) de primer orden mediante dos enfoques:

- **Método analítico:** separación de variables para obtener la solución exacta.
- **Método numérico:** método de Euler para aproximar la solución mediante pasos discretos.

El objetivo es comparar los resultados de ambos métodos y analizar el error introducido por la aproximación numérica.

## 1. Planteamiento del problema

Se considera la ecuación diferencial:

$
\frac{dy}{dt}=-2y
$

Con la condición inicial:

$
y(0)=1
$

Se busca resolverla en el intervalo:

$
t\in[0,1]
$

Utilizando un tamaño de paso de:

$
h=0.2
$

## 2. Solución analítica

Mediante separación de variables:

$
\frac{1}{y}dy=-2dt
$

Integramos ambos lados:

$
\ln|y|=-2t+C
$

Despejando y aplicando la condición inicial, obtenemos:

$
\boxed{y(t)=e^{-2t}}
$

Esta expresión representa un decaimiento exponencial.

## 3. Aproximación mediante Euler

El método de Euler utiliza la pendiente conocida en un punto para estimar el siguiente valor de la función.

Su expresión general es:

$
y_{n+1}=y_n+h f(t_n,y_n)
$

Para nuestro problema:

$
y_{n+1}=y_n+0.2(-2y_n)
$

Por tanto:

$
y_{n+1}=0.6y_n
$

Se realizan cinco pasos para aproximar la solución desde $t=0$ hasta $t=1$.

## 4. Resultados

| t | Solución exacta | Método de Euler | Error absoluto |
|---|---|---|---|
| 0.0 | 1.000000 | 1.000000 | 0.000000 |
| 0.2 | 0.670320 | 0.600000 | 0.070320 |
| 0.4 | 0.449329 | 0.360000 | 0.089329 |
| 0.6 | 0.301194 | 0.216000 | 0.085194 |
| 0.8 | 0.201897 | 0.129600 | 0.072297 |
| 1.0 | 0.135335 | 0.077760 | 0.057575 |

El error absoluto se calcula como:

$
E=|y_{\text{exacta}}-y_{\text{Euler}}|
$

## 5. Implementación en Python

El archivo `main.py` contiene las siguientes funciones:

- `derivada(t, y)`: evalúa la ecuación diferencial.
- `solucion_exacta(t)`: calcula la solución analítica.
- `metodo_euler(t0, y0, h, pasos)`: aproxima la solución numéricamente.
- `comparar_soluciones(tiempos, valores)`: calcula los valores exactos y los errores absolutos.

La implementación también utiliza Matplotlib para visualizar y comparar ambas soluciones.

## 6. Requisitos y ejecución

Se requiere Python 3 y las dependencias incluidas en `requirements.txt`.

Para instalarlas:

```bash
pip install -r requirements.txt
```

Para ejecutar el programa:

```bash
python main.py
```

El programa imprime los resultados numéricos y muestra una gráfica comparativa.

## 7. Conclusiones

El método de separación de variables permite obtener una solución analítica exacta para la ecuación diferencial seleccionada.

Por otro lado, el método de Euler aproxima la solución mediante evaluaciones sucesivas de la pendiente lo cual introduce una acumulacion de error que se puede reducir proporcionalmente como incrementemos el numero de pasos.

En este problema, las aproximaciones de Euler son menores que los valores exactos para los puntos posteriores a la condición inicial, y se puede observar como el error se va estabilizando, al inicio aumenta y se reduce paulatinamente, sin embargo nunca llegara a ser 0 por completo.

El tamaño de paso influye en la precisión del método. En general, utilizar pasos suficientemente pequeños mejora la aproximación, aunque aumenta el número de iteraciones necesarias la carga de procesamiento para el computador.

Este ejercicio permite comprender la relación entre las soluciones analíticas y los métodos numéricos utilizados en el estudio de ecuaciones diferenciales. En mi opinion la primera es mejor para soluciones que pueden encontrarse relativamente facil y cuando no es posible aproximamos la respuesta con el metodo de Euler.