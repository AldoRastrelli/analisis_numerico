import numpy as np
import math

# TP 1

# item 2 a
# Programar un algoritmo para aproximar π utilizando la función seno(x) con el método de
# Newton-Raphson, en función de x, que realice iteraciones hasta alcanzar el límite de la herramienta utilizada.

def newton_raphson_wrapper_getPi(tolerancia, maxIteraciones, semilla):
    """ La semilla debe de estar cerca del intervalo."""
    seno = math.sin
    seno_derivado = math.cos

    historia = np.zeros((maxIteraciones, 3)) # matriz maxIteraciones x 3
    if tolerancia < 0 or maxIteraciones < 0:
        print(" El intervalo no contiene información suficiente: no puede asegurarse una raíz")
        return None, np.array([])

    return newton_raphson(seno, seno_derivado, tolerancia, maxIteraciones, semilla, 0, historia)

def newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n, iteracion, historia):
    """Se consideran a los valores recibimos como válidos: no requieren validación extra.
    Si la derivada no se anula y las condiciones se cumplen, se devuelve la raíz.
    De lo contrario el valor de return será None y la historia acumulada."""

    if iteracion >= maxIteraciones - 1:
        return None, np.array([])

    valorFuncion = funcion(x_n) # Evalua sen(x_n)
    valorDerivada = funcion_derivada(x_n) # Evalua cos(x_n)

    if valorDerivada == 0:
        return None, np.array([])

    x_n_mas_1 = x_n - (valorFuncion / valorDerivada)

    error = abs(x_n_mas_1 - x_n)

    historia[iteracion] = (iteracion, x_n, error)

    if error < tolerancia:
        historia[iteracion + 1] = (iteracion + 1, x_n_mas_1,error)
        historia = historia[:iteracion + 2]
        return x_n_mas_1, historia

    return newton_raphson(funcion, funcion_derivada, tolerancia, maxIteraciones, x_n_mas_1, iteracion + 1, historia)

#item 2 b
# Programar un algoritmo para aproximar π utilizando la serie de Leibniz, en función de n.

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

# item 2 c
# Ejecutar los programas solicitados en a y b utilizando representación de punto flotante de
# 32 bits y comparar las respuestas obtenidas con n = 10, n = 100, n = 1000, n = 10000 y
# n = 100000.

def pruebas_newton_raphson_32():
    tolerancia = 1e-5
    semilla = np.float32(2.0)
    print("\n**PRUEBAS NEWTON-RAPHSON PARA 32 BITS**")
    print("[Valor Exacto π:  3.141592653589793...]")

    print("\n   Tolerancia: 1e-5, semilla: 2.0")

    # ejecutar newton_raphson para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper_getPi(tolerancia, 10, semilla)[0])))

    # ejecutar newton_raphson para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper_getPi(tolerancia, 100, semilla)[0])))

    # ejecutar newton_raphson para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper_getPi(tolerancia, 1000, semilla)[0])))

    # ejecutar newton_raphson para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper_getPi(tolerancia, 10000, semilla)[0])))

    # ejecutar newton_raphson para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper_getPi(tolerancia, 100000, semilla)[0])))

    return

def pruebas_leibniz_32():
    print("\n**PRUEBAS SERIE DE LEIBNIZ PARA 32 BITS**")
    print("[Valor Exacto π:  3.141592653589793...]")
    
    #ejecutar leibniz para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float32((serie_leibniz_pi(10)))))

    #ejecutar leibniz para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float32(serie_leibniz_pi(100))))
    
    #ejecutar leibniz para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float32(serie_leibniz_pi(1000))))

    #ejecutar leibniz para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float32(serie_leibniz_pi(10000))))

    #ejecutar leibniz para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float32(serie_leibniz_pi(100000))))

    return


# item 2 d
# Ejecutar los programas solicitados en a y b utilizando representación de punto flotante de
# 64 bits y comparar las respuestas obtenidas con n = 10, n = 100, n = 1000, n = 10000 y
# n = 100000.

def pruebas_newton_raphson_64():
    tolerancia = 1e-5
    semilla = np.float64(2.0)

    print("\n**PRUEBAS NEWTON-RAPHSON PARA 64 BITS**")
    print("[Valor Exacto π:  3.141592653589793...]")

    print("\n   Tolerancia: 1e-5, semilla: 2.0")

    # ejecutar newton_raphson para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper_getPi(tolerancia, 10, semilla)[0])))

    # ejecutar newton_raphson para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper_getPi(tolerancia, 100, semilla)[0])))

    # ejecutar newton_raphson para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper_getPi(tolerancia, 1000, semilla)[0])))

    # ejecutar newton_raphson para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper_getPi(tolerancia, 10000, semilla)[0])))

    # ejecutar newton_raphson para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper_getPi(tolerancia, 100000, semilla)[0])))

    return


def pruebas_leibniz_64():
    print("\n**PRUEBAS SERIE DE LEIBNIZ PARA 64 BITS**")
    print("[Valor Exacto π:  3.141592653589793...]")
    
    #ejecutar leibniz para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float64(serie_leibniz_pi(10))))

    #ejecutar leibniz para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float64(serie_leibniz_pi(100))))
    
    #ejecutar leibniz para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float64(serie_leibniz_pi(1000))))

    #ejecutar leibniz para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float64(serie_leibniz_pi(10000))))

    #ejecutar leibniz para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float64(serie_leibniz_pi(100000))))

    return


def main():
    print("\nTP 1 - ANÁLISIS NUMÉRICO - FIUBA\n1er Cuatrimestre - 2021")
    print("Aldana Rastrelli - Aldana Barbesini - Juan Ignacio Baserga")

    print("\n***\nÍtem 2)c)")
    pruebas_newton_raphson_32()
    pruebas_leibniz_32()

    print("\n***\nÍtem 2)d)")
    pruebas_newton_raphson_64()
    pruebas_leibniz_64()


main()