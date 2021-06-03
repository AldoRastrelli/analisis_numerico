# coding=utf-8

import numpy as np
import math

COTA_CERO = 1e-20
COTA_CERO_M = 1e-40

# TP 1

# item 2 a
# Programar un algoritmo para aproximar pi utilizando la función seno(x) con el método de
# Newton-Raphson, en función de x, que realice iteraciones hasta alcanzar el límite de la herramienta utilizada.

def newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n, iteracion, historia, cota_cero):
    """Se consideran a los valores recibimos como válidos: no requieren validación extra.
    Si la derivada no se anula y las condiciones se cumplen, se devuelve la raíz.
    De lo contrario el valor de return será None y la historia acumulada."""

    if iteracion >= maxIteraciones - 1:
        return None, historia

    valor_funcion = funcion(x_n)
    valor_derivada = funcion_derivada(x_n)

    # # # Corrección: no comparar float con int usando == 0 # # #  
    if abs(valor_derivada) < cota_cero:
        return None, historia

    x_n_mas_1 = x_n - (valor_funcion / valor_derivada) 

    if (iteracion < 1):
        error = x_n
        historia.append((iteracion, x_n, error))
    
    error = abs(x_n_mas_1 - x_n)
    historia.append((iteracion, x_n_mas_1, error))

    # # # Correccion: Error Local Relativo # # #
    if abs(x_n_mas_1 - x_n / x_n) < COTA_CERO:
        historia = historia[:iteracion + 1]
        return x_n, historia

    if error < tolerancia or abs(x_n_mas_1 - x_n) < tolerancia:
        historia.append((iteracion + 1, x_n_mas_1,error))
        historia = historia[:iteracion + 2]
        return x_n_mas_1, historia

    return newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n_mas_1, iteracion + 1, historia, cota_cero)

def newton_raphson_wrapper(tolerancia, maxIteraciones, semilla, funcion, funcion_derivada, cota_cero = COTA_CERO):
    """ La semilla debe de estar cerca del intervalo."""

    historia = []
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo no contiene información suficiente: no puede asegurarse una raíz")
        return None, historia

    return newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, semilla, 0, historia, cota_cero)


## Newton Raphson Modificado ## Se usa para el punto 3

def newton_raphson_modificado(funcion, funcion_derivada, funcion_doble_derivada, tolerancia, maxIteraciones, x_n, iteracion, historia, cota_cero = COTA_CERO_M):
    """Se consideran a los valores recibimos como válidos: no requieren validación extra.
    Si la derivada no se anula y las condiciones se cumplen, se devuelve la raíz.
    De lo contrario el valor de return será None y la historia acumulada."""

    if iteracion >= maxIteraciones - 1:
        return None, historia

    valor_funcion = funcion(x_n)
    valor_derivada = funcion_derivada(x_n)
    valor_doble_derivada = funcion_doble_derivada(x_n)

    # # # Corrección: no comparar float con int usando == 0 # # #  
    if abs(valor_derivada) < cota_cero:
        return None, historia

    x_n_mas_1 = x_n - ((valor_funcion * valor_derivada) / ((valor_derivada**2) - valor_funcion * valor_doble_derivada))
 
    if (iteracion < 1):
        error = x_n
        historia.append((iteracion, x_n, error))
    
    error = abs(x_n_mas_1 - x_n)
    historia.append((iteracion, x_n_mas_1, error))

    # # # Correccion: Error Local Relativo # # #
    if abs(x_n_mas_1 - x_n / x_n) < COTA_CERO:
        historia = historia[:iteracion + 1]
        return x_n, historia

    if error < tolerancia or abs(x_n_mas_1 - x_n) < tolerancia:
        historia.append((iteracion + 1, x_n_mas_1,error))
        historia = historia[:iteracion + 2]
        return x_n_mas_1, historia

    return newton_raphson_modificado(funcion, funcion_derivada, funcion_doble_derivada, tolerancia, maxIteraciones, x_n_mas_1, iteracion + 1, historia, cota_cero)

def newton_raphson_modificado_wrapper(funcion, funcion_derivada, funcion_doble_derivada, tolerancia, maxIteraciones, semilla, cota_cero = COTA_CERO_M):
    """La tolerancia y numero de iteraciones tienen que ser positivos.
    La semilla debe de estar cerca del intervalo, caso contrario no va a converger."""

    historia = []
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo no contiene información suficiente: no puede asegurarse una raíz")
        return None, historia

    return newton_raphson_modificado(funcion, funcion_derivada, funcion_doble_derivada, tolerancia, maxIteraciones, semilla, 0, historia, cota_cero)

#item 2 b
# Programar un algoritmo para aproximar pi utilizando la serie de Leibniz, en función de n.

def serie_leibniz_pi(iteraciones):
    """devuelve None si la cantidad de iteraciones enviadas por parámetro no son al menos 1.
    Devuelve una aproximación de pi obtenida con la cantidad de iteraciones indicada"""

    if (iteraciones <1 ):
        return None
    
    resultado = 0.0
    signo = 1.0
    
    for i in range(iteraciones):   # i = 0, 1, 2, 3..
        resultado += signo/(2.0*i+1.0)
        signo = -signo

    return 4*resultado

#item 3 b
# Halle para cada una de ellas la raíz en el intervalo indicado mediante los métodos vistos en clase 
# (Bisección, Newton-Raphson, Newton-Raphson modificado, Secante). Use para todos los métodos como 
# criterio de parada las siguientes cotas de error: 1 · 10−5, 1 · 10−13, para Newton-Raphson use 
# semilla x0 = 1.0, para secante use como semillas los extremos del intervalo.

def biseccion(funcion, a, b, tolerancia, num_iteracion, historia):
    """Se considera que los valores recibidos son válidos."""
    punto_medio = a + (b - a) / 2

    if (num_iteracion < 1):
        error = punto_medio
    else:
        error = abs(punto_medio - historia[num_iteracion - 1][1]) ## punto_medio - punto_medio_anterior

    historia.append((num_iteracion, punto_medio, error))

    if (error < tolerancia):
        historia = historia[:num_iteracion + 1]
        return punto_medio, historia
    elif (funcion(a) * funcion(punto_medio)) > COTA_CERO:
        a = punto_medio
    else:
        b = punto_medio

    return biseccion(funcion, a, b, tolerancia, num_iteracion + 1, historia)

def biseccion_wrapper(funcion, a, b, tolerancia):
    """El intervalo enviado debe de ser valido. La tolerancia y numero de iteraciones no pueden ser negativos.
    Se devuelve el punto aproximado de la raiz y la historia de iteraciones."""
    historia = []
    if funcion(a) * funcion(b) > 0 or tolerancia < 0:
        print(" No se puede asegurar una raiz")
        return None, historia

    return biseccion(funcion, a, b, tolerancia, 0, historia)

def secante(funcion, x_1, x_0, tolerancia, num_iteracion, max_iteraciones, historia):
    """Se considera que los valores recibidos son validos."""

    if num_iteracion >= max_iteraciones - 1:
        return None, historia

    error = abs(x_0 - x_1)
    historia.append((num_iteracion, x_1, error))

    if error < tolerancia:
        historia = historia[:num_iteracion + 1]
        return x_1, historia

    fx_1 = funcion(x_1)
    fx_0 = funcion(x_0)

    if(fx_1 == fx_0):
        return x_1, historia

    x2 = x_1 - fx_1 * (x_1 - x_0) / (fx_1 - fx_0)

    return secante(funcion, x2, x_1, tolerancia, num_iteracion + 1, max_iteraciones, historia)

def secante_wrapper(funcion, x_1, x_0, tolerancia, max_iteraciones):
    """ La tolerancia y numero de iteraciones no pueden ser negativos.
    Si se cumplen las condiciones se enviara el punto aproximado de la raiz y la historia de iteraciones."""

    historia = []
    if tolerancia < 0 or max_iteraciones < 0:
        print("No se puede asegurar una raiz")
        return None, historia
    
    try:
        return secante(funcion, x_1, x_0, tolerancia, 0, max_iteraciones, historia)
    except RecursionError:
        print(f"\n>>Se excede la cantidad de iteraciones máximas({max_iteraciones}). El método no converge para la función, las semillas dadas no son adecuadas.")
        return None, []