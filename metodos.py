import numpy as np
from sympy import *
import math


# item 2 a
# Programar un algoritmo para aproximar π utilizando la funci´on seno(x) con el m´etodo de
# Newton-Raphson, en función de x, que realice iteraciones hasta alcanzar el l´ımite de la herramienta utilizada.

def newton_raphson_wrapper_getPi(tolerancia, maxIteraciones, semilla):
    """ La semilla debe de estar cerca del intervalo."""
    seno = math.sin
    seno_derivado = math.cos


    historia = np.zeros((maxIteraciones, 3)) # matriz maxIteraciones x 3
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo no contiene información suficiente: no puede asegurarse una raíz")
        return None, np.array([])

    return NewtonRaphsonRecursivo(seno, seno_derivado, tolerancia, maxIteraciones, semilla, 0, historia)


def newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n, iteracion, historia):
    """Se consideran a los valores recibimos como válidos: no requieren validación extra.
    Si la derivada no se anula y las condiciones se cumplen, se devuelve la raíz.
    De lo contrario el valor de return será None y la historia acumulada."""

    if iteracion >= maxIteraciones - 1:
        return None, np.array([])

    valorFuncion = funcion(x_n)
    valorDerivada = funcion_derivada(x_n)

    if valorDerivada == 0:
        return None, np.array([])

    x_n_mas_1 = x_n - (valorFuncion / valorDerivada)

    error = abs(x_n_mas_1 - x_n)

    historia[iteracion] = (iteracion, x_n, error)

    if x_n_mas_1 == x_n:
        historia = historia[:iteracion + 1]
        return x_n, historia

    if error < tolerancia:
        historia[iteracion + 1] = (iteracion + 1, x_n_mas_1,error)
        historia = historia[:iteracion + 2]
        return x_n_mas_1, historia

    return NewtonRaphsonRecursivo(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n_mas_1, iteracion + 1, historia)

#item 2 b
# Programar un algoritmo para aproximar π utilizando la serie de Leibniz, en función de n.

def serie_leibniz_pi(iteraciones):
    """devuelve None si la cantidad de iteraciones enviadas por parámetro no son al menos 1.
    Devuelve una aproximación de pi obtenida con la cantidad de iteraciones indicada"""

    if (iteraciones <1 ):
        return None
    
    resultado = 0.0
    signo = 1.0
    
    for i in range(iteraciones):
        resultado += signo/(2.0*n+1.0)
        signo = -signo

    return 4*resultado

# item 2 c
# Ejecutar los programas solicitados en a y b utilizando representación de punto flotante de
# 32 bits y comparar las respuestas obtenidas con n = 10, n = 100, n = 1000, n = 10000 y
# n = 100000.

def pruebas_newton_raphson_32():
    # ejecutar newton_raphson para n = 10
    # ejecutar newton_raphson para n = 100
    # ejecutar newton_raphson para n = 1000
    # ejecutar newton_raphson para n = 10000
    # ejecutar newton_raphson para n = 100000

def pruebas_leibniz_32():
    #ejecutar leibniz para n = 10
    #ejecutar leibniz para n = 100
    #ejecutar leibniz para n = 1000
    #ejecutar leibniz para n = 10000
    #ejecutar leibniz para n = 100000

# item 2 d
# Ejecutar los programas solicitados en a y b utilizando representación de punto flotante de
# 64 bits y comparar las respuestas obtenidas con n = 10, n = 100, n = 1000, n = 10000 y
# n = 100000.

def pruebas_newton_raphson_64():
    # ejecutar newton_raphson para n = 10
    # ejecutar newton_raphson para n = 100
    # ejecutar newton_raphson para n = 1000
    # ejecutar newton_raphson para n = 10000
    # ejecutar newton_raphson para n = 100000

def pruebas_leibniz_64():
    #ejecutar leibniz para n = 10
    #ejecutar leibniz para n = 100
    #ejecutar leibniz para n = 1000
    #ejecutar leibniz para n = 10000
    #ejecutar leibniz para n = 100000

# item 2 e
# Ejecutar los programas solicitados en a y b con una calculadora (aclarar marca y modelo) y
# comparar las respuestas obtenidas con n = 10, n = 100, n = 1000, n = 10000 y n = 100000
# (en caso de no alcanzar la memoria de la calculadora utilizar el m´aximo n posible).

    """Hacer las cuentas"""

# item 2 f
# Representar las dos respuestas finales obtenidas (para n = 100000 y el método de Newton
# Raphson) en c, d y e de manera de expresarlo como π = π(vect) + ∆π

    """ calcular ∆π """

# item 2 g
# Podemos afirmar qué para la computadora el número π es una constante?

    """En la computadora, el número π es una constante, porque es una representación del número π con la cantidad de decimales que la representación del sistema permita"""

