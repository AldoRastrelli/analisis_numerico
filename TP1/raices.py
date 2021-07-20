from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
from funciones import *

def graficar_funciones(inicio_interv, final_interv, funciones):
    
    x = np.linspace(inicio_interv,final_interv,100)
    
    for f in funciones:
        y = f.funcion(x)
        df = f.derivada(x)
        ddf = f.derivada_doble(x)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.set(xlabel="x", ylabel="y")

        plt.plot(x,y, label= "f" + str(funciones.index(f)+1) + "(x):", color = 'blue')
        plt.plot(x,df, label= "df" + str(funciones.index(f)+1) + "(x):", color = 'red')
        plt.plot(x,ddf, label= "ddf" + str(funciones.index(f)+1) + "(x):", color = 'green')
        plt.legend(loc='upper left')

        # show the plot
        plt.show()

    return

def imprimir_raices(inicio_interv, final_interv, funciones):

    print("\n** OBTENCIÓN DE RAÍCES CON SCIPY**\n")
    print("Intervalo: [" + str(inicio_interv) + ", " + str(final_interv) + "]")    

    for f in funciones:
        print("\nRaíz/raíces f" + str(funciones.index(f)+1) + "(x):")
        imprimir_raiz_en_intervalo(f.funcion,inicio_interv,final_interv)

def imprimir_raiz_en_intervalo(funcion, inicio_interv, final_interv):

    raiz = optimize.brentq(funcion,inicio_interv,final_interv)
    print("{:.4f}".format(raiz))        ## limita la cantidad de dígitos a imprimirse a 4

def pruebas_raices(funciones):
    imprimir_raices(INICIO_INTERVALO, FINAL_INTERVALO, funciones)
    input("\n>>Se imprimiran los gráficos de las funciones. Presione ENTER para continuar.\n")
    graficar_funciones(INICIO_INTERVALO, FINAL_INTERVALO, funciones)