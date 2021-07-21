# coding=utf-8

import numpy as np
import math
from metodos import *
from funciones import *
from raices import *
import matplotlib
import matplotlib.pyplot as plt


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

    funcion = math.sin
    funcion_derivada = math.cos

    # ejecutar newton_raphson para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper(tolerancia, 10, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper(tolerancia, 100, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper(tolerancia, 1000, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper(tolerancia, 10000, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float32(newton_raphson_wrapper(tolerancia, 100000, semilla, funcion, funcion_derivada)[0])))

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

    funcion = math.sin
    funcion_derivada = math.cos

    # ejecutar newton_raphson para n = 10
    print("         n = 10")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper(tolerancia, 10, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 100
    print("         n = 100")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper(tolerancia, 100, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 1000
    print("         n = 1000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper(tolerancia, 1000, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 10000
    print("         n = 10000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper(tolerancia, 10000, semilla, funcion, funcion_derivada)[0])))

    # ejecutar newton_raphson para n = 100000
    print("         n = 100000")
    print("         Aproximación obtenida: " + str(np.float64(newton_raphson_wrapper(tolerancia, 100000, semilla, funcion, funcion_derivada)[0])))

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

def pruebas_funciones(funciones, cota_error_1, cota_error_2):

    for f in funciones:

        funcion = f"f{funciones.index(f)+1}"
        print(f"\n(!) Funcion: {funcion}")

        print("\n**PRUEBAS BISECCIÓN**")

        print(f"\n   Tolerancia: 1e-5")
        raiz, historial = biseccion_wrapper(f.funcion, INICIO_INTERVALO, FINAL_INTERVALO, cota_error_1)
        l_bis, p_bis = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_bis, p_bis)
        print("\n   Tolerancia: 1e-13")
        raiz, historial = biseccion_wrapper(f.funcion, INICIO_INTERVALO, FINAL_INTERVALO, cota_error_2)
        l_bis, p_bis = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_bis, p_bis)

        print("\n**PRUEBAS NEWTON-RAPHSON**")

        print(f"\n   Tolerancia: 1e-5")
        raiz, historial = newton_raphson_wrapper(cota_error_1, 10000, 1, f.funcion, f.derivada)
        l_nr, p_nr = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_nr, p_nr)
        print("\n   Tolerancia: 1e-13")
        raiz, historial = newton_raphson_wrapper(cota_error_2, 10000, 1, f.funcion, f.derivada)
        l_nr, p_nr = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_nr, p_nr)

        print("\n**PRUEBAS NEWTON-RAPHSON MODIFICADO**")

        print(f"\n   Tolerancia: 1e-5")
        raiz, historial = newton_raphson_modificado_wrapper(f.funcion, f.derivada, f.derivada_doble, cota_error_1, 10000, 1, COTA_CERO_M)
        l_nrm, p_nrm = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_nrm, p_nrm)
        print("\n   Tolerancia: 1e-13")
        raiz, historial = newton_raphson_modificado_wrapper(f.funcion, f.derivada, f.derivada_doble, cota_error_2, 10000, 1, COTA_CERO_M)
        l_nrm, p_nrm = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_nrm, p_nrm)

        print("\n**PRUEBAS SECANTE**")

        print(f"\n   Tolerancia: 1e-5")
        raiz, historial = secante_wrapper(f.funcion, FINAL_INTERVALO, INICIO_INTERVALO, cota_error_1, 10000)
        l_sec, p_sec = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_sec, p_sec)
        print("\n   Tolerancia: 1e-13")
        raiz, historial = secante_wrapper(f.funcion, FINAL_INTERVALO, INICIO_INTERVALO, cota_error_2, 10000)
        l_sec, p_sec = analizar_historial(historial)
        imprimir_historial(historial, raiz, l_sec, p_sec)

        input(f"\n***********************************\n>>Se imprimirá ahora el gráfico de λ y de p de la funcion {funcion}.Presione ENTER para continuar:")


        colores = ['blue', 'red', 'green', 'orange']
        labels = ['Biseccion', 'Newton Raphson', 'Newton Raphson Modificado', 'Secante']

        # Const Asintóticas #
        fig, ax = plt.subplots()
        plt.title(f"Historial de constantes asintóticas para {funcion}")
        ax.set_ylabel('λ')

        const_asint = [l_bis, l_nr, l_nrm, l_sec]
        const_asint = [l for l in const_asint if (l != None)]

        xmax = max([len(l) for l in const_asint])
        
        i = 0
        for constante in const_asint:
            if ( not constante):
                continue
            plt.plot([i for i in range(len(constante))], constante, color = colores[i], label=labels[i])
            i += 1
        plt.xticks([i*10 for i in range(xmax#10)])
        plt.xlim(1, xmax)
        plt.grid(True)
        plt.legend(loc = 'best')
        plt.show()

        # Convergencia #
        fig, ax = plt.subplots()
        plt.title(f"Historial de orden de convergencia para {funcion}")
        ax.set_ylabel('p')

        orden_conv = [p_bis, p_nr, p_nrm, p_sec]
        orden_conv = [p for p in orden_conv if (p != None)]

        xmax = max([len(p) for p in orden_conv])
        
        i = 0
        for conv in orden_conv:
            if ( not conv):
                continue
            plt.plot([i for i in range(len(conv))], conv, color = colores[i], label=labels[i])
            i += 1
        plt.xticks([i*10 for i in range(xmax#10)])
        plt.xlim(1, xmax)
        plt.grid(True)
        plt.legend(loc = 'best')
        plt.show()

 
def pruebas_punto_2():
    print("\n***\nÍtem 2)c)")
    pruebas_newton_raphson_32()
    pruebas_leibniz_32()
    input("Presione ENTER para seguir.")

    print("\n***\nÍtem 2)d)")
    pruebas_newton_raphson_64()
    pruebas_leibniz_64()
    input("Presione ENTER para seguir.")

def pruebas_punto_3():

    funcion1 = FuncionDerivable(f1, df1, ddf1)
    funcion2 = FuncionDerivable(f2,df2,ddf2)
    funcion3 = FuncionDerivable(f3,df3,ddf3)

    print("\n***\nÍtem 3)a) y 3)c)")
    pruebas_raices([funcion1,funcion2,funcion3])
    input("Presione ENTER para seguir.")

    print("\n***\nÍtem 3)b)")
    
    cota_error_1 = 1e-5
    cota_error_2 = 1e-13

    pruebas_funciones([funcion1,funcion2,funcion3], cota_error_1, cota_error_2)
    
def analizar_historial(historial):
    
    if (len(historial) == 0):
        print("El método falla. No puede asegurarse la convergencia.")
        return None, None

    p = []
    l = []
    for i in range(len(historial)):

        error = historial[i][2]
        error_1 = historial[i-1][2]
        error_2 = historial[i-2][2]

        if (abs(error_1 - error_2) < COTA_CERO):
            break

        if i < 3 or error < COTA_CERO:
            p.append(None)
            l.append(None)
            i += 1
            continue

        p.append( math.log(error/error_1) / math.log(error_1/error_2) )
        l.append(error / (error_1**p[i]))
    return l, p

def imprimir_historial(historial, raiz, l, p):

    if (len(historial) == 0):
        return

    print("\nTABLA DE VALORES: se imprimen las primeras y las últimas 5 entradas")

    for i in range(len(l)):    
        if (i > 5 and i < len(historial) -5):
            continue
        k = "{:02d}".format(i)
        x_n = "{:.14f}".format(historial[i][1])  # punto_medio # formato con 14 dígitos porque se adapta a la tolerancia de 1e-13
        error = "{:.14f}".format(historial[i][2])
        
        print(f"k: {k}   Xn: {x_n}      ΔXn: {error}     λ: {l[i]}       p: {p[i]}")

    if (len(l) < len(historial)):
            print(">>La cantidad de dígitos no suficiente para representar correctamente los puntos dados.\nSe detiene la iteración.")
    if (not raiz):
        print("La función no converge para la semilla dada. No puede asegurarse una raíz.")
    
def main():
    print("\nTP 1 - ANÁLISIS NUMÉRICO - FIUBA\n1er Cuatrimestre - 2021")
    print("Aldana Rastrelli - Aldana Barbesini - Juan Ignacio Baserga")

    pruebas_punto_2()
    pruebas_punto_3()

main()