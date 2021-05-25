from scipy import optimize
import math
import matplotlib.pyplot as plt
import numpy as np

def main():

    inicio_interv = 0
    final_interv = 2
    funciones = [f1,f2,f3]
    graficar_funciones(inicio_interv, final_interv, funciones)
    imprimir_raices(inicio_interv, final_interv, funciones)

def graficar_funciones(inicio_interv, final_interv, funciones):
    
    x = np.linspace(inicio_interv,final_interv,100)
    
    for funcion in funciones:
        y = funcion(x)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.set(xlabel="x", ylabel="y")

        plt.plot(x,y, label= "f" + str(funciones.index(funcion)+1) + "(x):" )
        plt.legend(loc='upper left')

        # show the plot
        plt.show()

    return

def imprimir_raices(inicio_interv, final_interv, funciones):

    print("\n** OBTENCIÓN DE RAÍCES CON SCIPY**\n")
    print("Intervalo: [" + str(inicio_interv) + ", " + str(final_interv) + "]")    

    for funcion in funciones:
        print("\nRaíz/raíces f" + str(funciones.index(funcion)+1) + "(x):")
        imprimir_raiz_en_intervalo(funcion,inicio_interv,final_interv)

def imprimir_raiz_en_intervalo(funcion, inicio_interv, final_interv):

    raiz = optimize.brentq(funcion,inicio_interv,final_interv)
    print("{:.4f}".format(raiz))        ## limita la cantidad de dígitos a imprimirse a 4

def f1(x):
    return (x**2 - 2)

def f2(x):
    return (x**5 - 6.6*x**4 + 5.12*x**3 + 21.312*x**2 - 38.016*x + 17.28)

def f3(x):
    return ((x-1.5)*(math.e)**(-4*(x-1.5)**2))

main()
