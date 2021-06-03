# Ej 3

*Nota: Para la correcta visualizacion de los resultados y graficos, es importante ejecutar las celdas en orden. Esto se puede hacer en la pestaña 'Entorno de ejecución' -> Ejecutrar todo, o presionando 'ctrl + f0'*

 ## 3. a)

Primero, graficamos las 3 funciones pedidas, con sus respectivas derivadas.

import numpy as np
import matplotlib.pyplot as plt

Definimos las funciones indicadas. La notacion usada para las derivadas es la mostrada en el código a continuación, agregando una 'd' para la derivada primera, y dos para la derivada segunda. 
Para las funciones exponenciales, se usan las disponibles en Numpy.

def f1(x):
    return x ** 2 - 2

def df1(x):
    return 2 * x

def ddf1(x):
    return 2.0 + x - x #La funcion deberia ser 2, pero si no depende de x falla al graficar

def f2(x):
    return x**5 - 6.6 * x**4 + 5.12 * x**3 + 21.312 * x**2 - 38.016 * x + 17.28

def df2(x):
    return 5.0 * x**4 - 26.4 * x**3 + 15.36 * x**2 + 42.624 * x - 38.016

def ddf2(x):
    return 20.0 * x **3 - 79.2 * x** 2 + 30.72 * x + 42.624  

def f3(x):
    return (x - 1.5) * np.exp(-4 * (x - 1.5)**2)

def df3(x):
    return (-8 * x + 12.0) * (x - 1.5) * np.exp(-4 * (x - 1.5)**2) + np.exp(-4 * (x - 1.5)**2) 

def ddf3(x):
    return (-24 * x + (x - 1.5)*((8 * x - 12.0)**2) ) * np.exp(-4 * (x - 1.5)**2)


Primero observamos como se ven las 3 funciones superpuestas en el rango [0; 2]

 ### Todas las funciones

CANT_MUESTRAS = 10000 #Tomamos 1000 muestras equidistantes entre 0 y 2. A mayor numero de muestras, mayor precision tendra el grafico
x = np.linspace(0, 2, CANT_MUESTRAS)
plt.figure()
plt.plot(x, f1(x), lw=2, label='f1(x)')
plt.plot(x, f2(x), lw=2, label='f2(x)')
plt.plot(x, f3(x), lw=2, label='f3(x)')

plt.xlim(0, 2)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('Comparativa de f1(x), f2(x) y f3(x)')
plt.legend(loc = 'best')
plt.grid(True)

plt.show() 

Pasamos a ver los gráficos de cada función más detalladamente con sus derivadas. Para f1, que es una función cuadrática, crece en el intervalo dado.
Su primera derivada es la recta df1(x) = 2.x, y su derivada segunda es 2. 

 ### f1(x)

'''
Graficos de f1(x)
'''
plt.figure()
plt.plot(x, f1(x), lw=4, label = 'f1(x)')
plt.plot(x, df1(x), 'r--', lw=1, label = 'df1(x)', color='green')
plt.plot(x, ddf1(x), 'r--', lw=1, label='ddf1(x)', color='red')
plt.grid(True)
plt.legend(loc='best')
plt.xlim(0, 2)
plt.title('f1(x) y sus derivadas en [0; 2]')

plt.show()


Para f2(x), observamos un comportamiento mas variado en el intervalo, ya que es un polinomio de grado 5. El gráfico muestra que cerca de x=1 parece tener una raíz, lo veremos más adelante aplicando distintos métodos.

 ### f2(x)

'''
Graficos de f2(x)
'''
plt.figure()
plt.plot(x, f2(x), lw=4, label = 'f2(x)')
plt.plot(x, df2(x), 'r--', lw=1, label = 'df2(x)', color='green')
plt.plot(x, ddf2(x), 'r--', lw=1, label='ddf2(x)', color='red')
plt.grid(True)
plt.legend(loc='best')
plt.xlim(0, 2)
plt.title('f2(x) y sus derivadas')

plt.show()


Finalmente, vemos el gráfico de f3(x). Vemos que es el producto entre una recta y una Gaussiana, cambiando de signo en x=1.5

 ### f3(x) 

'''
Graficos de f3(x) sin zoom
'''
plt.figure()
plt.plot(x, f3(x), lw=1, label = 'f3(x)')
plt.plot(x, df3(x), 'r--', lw=1, label = 'df3(x)', color='green')
plt.plot(x, ddf3(x), 'r--', lw=1, label='ddf3(x)', color='red')
plt.grid(True)
plt.legend(loc='best')
plt.xlim(0, 2)
plt.title("f3(x) y sus derivadas")

plt.show()


El anterior gráfico no nos es útil para ver el comportamiento de f3(x) entre 0 y 2, ya que al tener su derivada segunda una imagen mucho más amplia, la función original no queda a la vista. Considerando esto, vemos otro gráfico con una escala que nos permita visualizar mejor f3(x):

'''
Graficos de f3(x) con y entre -0.25 y 0.25
'''
plt.figure()
plt.plot(x, f3(x), lw=2, label = 'f3(x)')
plt.plot(x, df3(x), 'r--', lw=1, label = 'df3(x)', color='green')
plt.plot(x, ddf3(x), 'r--', lw=1, label='ddf3(x)', color='red')
plt.grid(True)
plt.legend(loc='best')
plt.xlim(0, 2)
plt.ylim(-0.25, 0.25)
plt.title("f3(x) y sus derivadas, entre y=-0.25 e y=0.25")

plt.show()

 ## 3. b)


A continuación, usamos distintos algoritmos de búsqueda de raíces para cada función, para más adelante analizar los resultados obtenidos y comparar los métodos usados.

 ### Biseccion con f1(x)

Definimos primero la función del método de bisección, con las pre y post-condiciones indicadas en la documentación:

def biseccion(f, a, b, TOL, N_0):
    '''
    Metodo de biseccion, para aproximar una raiz en un intervalo dado.
    f -> funcion a evaluar
    a, b -> limites superior e inferior del intervalo respectivamente
    TOL -> tolerancia del error para corte
    N_0 -> Numero maximo de iteraciones admitidas
    Hay 2 valores de retorno:
    - El primero es la aproximacion de la raiz encontrada, o None si no convergio
    - Como criterio, decimos que si el error absoluto entre un p_n y su anterior evaluados en f es menor a la tolerancia, entonces p convergio  
    - El segundo es una lista de tuplas de la forma (n_iter, p_n), que sirve como historial de valores obtenidos
    '''
    if a >= b: 
      print("Error, intervalo inexistente")
      return None, []
    if f(a) * f(b) >= 0:
      print("No es posible que exista una unica raiz en el intervalo [a;b]")
      return None, []
    
    i = 1
    p_prev = a
    historial = []
    while i <= N_0:
        p = (a + b) / 2
        historial.append((i, p))
        if np.abs(f(p) - f(p_prev)) < TOL: return p, historial
        if f(a) * f(p) > 0: a = p
        else: b = p
        i += 1
        p_prev = p
    print("No convergio.")
    return None, historial

Corremos ahora el algoritmo para dos tolerancias distintas: 10^-5 y 10^-13, observando su historia de convergencia, es decir, la cantidad de iteraciones y el valor parcial de 'p' en cada una de ellas.

lim_inferior = 0
lim_superior = 2
tolerancia = 1e-5
max_iteraciones = 50
raiz1, h_bis = biseccion(f1, lim_inferior, lim_superior, tolerancia, max_iteraciones)

print("Biseccion con tolerancia de 10^-5")

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))

Observamos que tarda 20 iteraciones en converger. Ahora, probamos con una mayor precisión, observando cuantas iteraciones más necesita para converger.

tolerancia = 1e-13
raiz2, h_bis = biseccion(f1, lim_inferior, lim_superior, tolerancia, max_iteraciones)

print("Biseccion con tolerancia de 10^-13")

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))

Con esta tolerancia se necesitaron más del doble que con la anterior, pero tenemos una aproximación mucho más precisa. A continuación, aplicamos el método de Newton-Raphson, viendo así sí también converge y que tan rápido lo hace.

 ### Metodo de Newton con f1(x)

Comenzamos definiendo la función del método de Newton-Raphson, junto con su respectiva documentación


def newton_raphson(f, df, semilla, TOL, N_0):
    '''
    Metodo de Newton-Raphson, para aproximar una raiz en un intervalo dado.
    f -> funcion a evaluar
    df -> la derivada de la funcion a evaluar
    semilla -> aproximacion inicial de p. Si es una aproximacion mala, el algoritmo podria no converger.
    TOL -> tolerancia del error para corte
    N_0 -> Numero maximo de iteraciones admitidas
    Hay 2 valores de retorno:
    - El primero es la aproximacion de la raiz encontrada, o None si no convergio
    - Como criterio, decimos que si el error absoluto entre un p_n y su anterior evaluados en f es menor a la tolerancia, entonces p convergio  
    - El segundo es una lista de tuplas de la forma (n_iter, p_n), que sirve como historial de valores obtenidos
    '''
    i = 1
    p_prev = semilla
    historial = []
    historial.append((1, semilla))
    while i <= N_0:
        if np.abs(df(p_prev)) < 1e-15:
            print("Derivada en " + str(p_prev) + "demasiado cercana a 0")
            return None, historial 
        p = p_prev - (f(p_prev) / df(p_prev)) 
        historial.append((i + 1, p))
        if np.abs(f(p) - f(p_prev)) < TOL: return p, historial
        p_prev = p
        i += 1
    print("No convergio.")
    return None, historial

Corremos nuevamente el algoritmo sobre f1 para las mismas tolerancias, pero ahora con Newton-Raphson. Usamos x=1 como semilla.

print("Newton-Raphson con tolerancia de 10^-5")

tolerancia = 1e-5
semilla = 1
raiz1, h_nr = newton_raphson(f1, df1, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))

Vemos que, tal como era esperado, la velocidad de convergencia es mucho mas grande para el método de Newton-Raphon que para bisección; con este último tardo 20 iteraciones, mientras que Newton-Raphson necesitó solo 5 para la tolerancia dada. Probamos ahora con una tolerancia de 10^-13

print("Newton-Raphson con tolerancia de 10^-13")
tolerancia = 1e-13
raiz1, h_nr = newton_raphson(f1, df1, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))

La diferencia es aún mayor; con este método obtenemos una aproximación muy precisa en solo 7 iteraciones.

Ahora vemos que resultados obtenemos usando Newton-Raphson modificado.
Primero, definimos la función.

 ### Newton raphson modificado con f1(x)

def U(x, f, df):
    '''
    Devuelve None en caso de que el denominador en x sea 0 
    '''
    return f(x) * df(x)

def dU(x, f, df, ddf):
    '''
   # Devuelve None en caso de que el denominador en x sea 0
    '''
    return df(x)**2 - f(x) * ddf(x) 


def newton_raphson_mod(f, df, ddf, semilla, TOL, N_0):
    '''
    Metodo de Newton-Raphson modificado, para aproximar una raiz en un intervalo dado.
    f -> funcion a evaluar
    df -> la derivada primerade la funcion a evaluar
    ddf -> la derivada segunda de la funcion a evaluar
    semilla -> aproximacion inicial de p. Si es una aproximacion mala, el algoritmo podria no converger.
    TOL -> tolerancia del error para corte
    N_0 -> Numero maximo de iteraciones admitidas
    Hay 2 valores de retorno:
    - El primero es la aproximacion de la raiz encontrada, o None si no convergio
    - Como criterio, decimos que si el error absoluto entre un p_n y su anterior evaluados en f es menor a la tolerancia, entonces p convergio  
    - El segundo es una lista de tuplas de la forma (n_iter, p_n), que sirve como historial de valores obtenidos
    En caso de error, se informa imprimiendo por consola, devolviendo None y el historial en el momento del error.
    '''
    i = 1
    historial = []
    historial.append((i, semilla))
    p_prev = semilla
    while i <= N_0:
        numerador = U(p_prev, f, df)
        denominador = dU(p_prev, f, df, ddf)
        if np.abs(denominador) < 1e-15:
            print("Derivada demasiado cerca de 0")
            return None, historial
        p = p_prev - (numerador/denominador)
        historial.append((i + 1, p))
        if abs(f(p) - f(p_prev)) < TOL: return p, historial
        p_prev = p
        i += 1
    print("No convergio")
    return None, historial

Corremos el algoritmo para tolerancia de 10^-5 y 10^-13:

print("Newton-Raphson modificado con tolerancia de 1e-5")

tolerancia = 1e-5
raiz1, h_nrm = newton_raphson_mod(f1, df1, ddf1, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_nrm = newton_raphson_mod(f1, df1, ddf1, semilla, tolerancia, max_iteraciones)
print("Newton-Raphson modificado con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))


Observamos un igual rendimiento que con el Newton-Raphson normal: logra llegar al resultado esperado en 5 y 7 iteraciones respectivamente.

 ### Metodo de la secante en f1(x)

Definimos la función:

def secante(f, semilla_1, semilla_2, TOL, N_0):
    '''
    Metodo de la secante, para encontrar una raiz de f
    f -> la funcion a evaluar
    semilla_1 -> primera aproximacion de f
    semilla_2 -> segunda aproximacion de f
    TOL -> Tolerancia para la cual se considera resultado valido
    N_0 -> Maximo numero de iteraciones permitidas
    Hay 2 valores de retorno:
    - El primero es la aproximacion de la raiz encontrada, o None si no convergio
    - Como criterio, decimos que si el error absoluto entre un p_n y su anterior evaluados en f es menor a la tolerancia, entonces p convergio  
    - El segundo es una lista de tuplas de la forma (n_iter, p_n), que sirve como historial de valores obtenidos
    En caso de error, se informa imprimiendo por consola, devolviendo None y el historial en el momento del error.
    '''
    i = 1
    p_0 = semilla_1
    p_1 = semilla_2
    q_0 = f(p_0)
    q_1 = f(p_1)
    historial = []
    while i < N_0:
        if np.abs(q_1 - q_0) < 1e-20:
            print("Denominador muy cercano a 0")
            return None, historial
        p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
        historial.append((i, p))
        if abs(f(p) - f(p_1)) < TOL: return p, historial
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)
        i += 1
    return None, historial
 

Ahora lo corremos con tolerancias 10^-5 y 10^-13

tolerancia = 1e-5
semilla_1 = 0
semilla_2 = 2
raiz1, h_sec = secante(f1, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-5")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_sec = secante(f1, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

Vemos que, si bien necesitó una iteración más que Newton-Raphson para llegar al resultado en ambos casos, sigue teniendo un rendimiento muy bueno; precisa solo 6 iteraciones para tolerancia de 10^-5 y 8 para 10^-13.

Mostramos una comparativa de las iteraciones para cada metodo:

#Comparativa de historiales
bases_biseccion = [h_bis[i][0] for i in range(len(h_bis))]
raices_biseccion = [h_bis[i][1] for i in range(len(h_bis))]

bases_nr = [h_nr[i][0] for i in range(len(h_nr))]
raices_nr = [h_nr[i][1] for i in range(len(h_nr))]

bases_nrm = [h_nrm[i][0] for i in range(len(h_nrm))]
raices_nrm = [h_nrm[i][1] for i in range(len(h_nrm))]

bases_secante = [h_sec[i][0] for i in range(len(h_sec))]
raices_secante = [h_sec[i][1] for i in range(len(h_sec))]

plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f1")
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.plot(bases_nr, raices_nr, color='red', label='Newton-Raphson')
plt.plot(bases_nrm, raices_nrm, color='green', label='Newton-Raphson modificado')
plt.plot(bases_secante, raices_secante, color='purple', label='Metodo de la secante')
plt.legend(loc = 'best')
plt.xlim(1, 20)
plt.show()

Para que sea mas notorio como fueron evolucionando todos los metodos, repetimos para un rango mas acotado

plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f1 con zoom")
plt.plot(bases_nr, raices_nr, color='red', lw=3, label='Newton-Raphson')
plt.plot(bases_nrm, raices_nrm, color='green', lw=3 , label='Newton-Raphson modificado')
plt.plot(bases_secante, raices_secante, color='purple', lw=2, label='Metodo de la secante')
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.legend(loc = 'best')
plt.xlim(1, 7)
plt.show()

En el grafico podemos observar como claramente Newton-Raphson es el que mas rapido converge; en la tercer iteracion ya esta muy cerca de la raiz. Se evidencia tambien como, para esta funcion, biseccion es el mas lento de todos.

Ahora, probamos los mismos algoritmos con f2(x) y observamos los resultados obtenidos.

 ### Bisección con f2(x)

Usando las definicion del algoritmo creadas anteriormente, corremos para las mismas tolerancias:

print("Biseccion con tolerancia 1e^-5")
tolerancia = 1e-5
raiz1, h_bis = biseccion(f2, lim_inferior, lim_superior, tolerancia, max_iteraciones)
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))

print()
print()
print("Biseccion con tolerancia 1e^-13")

tolerancia = 1e-13
raiz2, h_bis = biseccion(f2, lim_inferior, lim_superior, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))


Al igual que con f1, observamos que biseccion converge claramente de forma mas lenta que el resto de los metodos. Sin embargo, comparando con el grafico, pareceria ser que efectivamente hay una raiz muy cerca de 1.12, por lo que evidenciamos el correcto funcionamiento del algoritmo.

 ### Newton-Raphson con f2(x)

print("Newton-Raphson con tolerancia de 1e-5")

tolerancia = 1e-5
semilla = 1
raiz1, h_nr = newton_raphson(f2, df2, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_nr = newton_raphson(f2, df2, semilla, tolerancia, max_iteraciones)
print("Newton-Raphson con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))


Observamos una reducción muy grande de velocidad de convergencia con Newton-Raphson en f2, incluso peor que bisección. 

Esto sucede porque la derivada de f2 en la raiz es muy cercana a 0, y, por como funciona el metodo de Newton-Raphson, cuando esto sucede las iteraciones se acercan de forma mucho mas lenta. Se puede observar graficamente pensando cada iteracion tomando la recta tangente, y como esta depende de la derivada en el punto, sera casi plana.

Probamos ahora con Newton-Raphson modificado, viendo si se mantiene la tendencia:

 ### Newton-Raphson modificado con f2(x)

print("Newton-Raphson modificado con tolerancia de 1e-5")

tolerancia = 1e-5
raiz1, h_nrm = newton_raphson_mod(f2, df2, ddf2, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_nrm = newton_raphson_mod(f2, df2, ddf2, semilla, tolerancia, max_iteraciones)
print("Newton-Raphson modificado con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))


Vemos que, usando Newton-Raphson modificado, se anula el denominador de dU. Por lo tanto, no se cumplen las hipotesis necesarias para poder usar el metodo.

Finalmente, usamos el método de la secante:

 ### Método de la secante con f2

tolerancia = 1e-5
semilla_1 = 0
semilla_2 = 2
raiz1, h_sec = secante(f2, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-5")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_sec = secante(f2, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

Sabemos que este método funciona mejor para funciones muy volátiles, produciendo una secante empinada entre los puntos. Para este caso, donde esto no sucede en el intervalo dado, vemos que son necesarias muchísimas iteraciones para llegar a una aproximación con tolerancias muy chicas.

Vemos una comparativa de las raices candidatas para cada metodo:

#Comparativa de historiales
bases_biseccion = [h_bis[i][0] for i in range(len(h_bis))]
raices_biseccion = [h_bis[i][1] for i in range(len(h_bis))]

bases_nr = [h_nr[i][0] for i in range(len(h_nr))]
raices_nr = [h_nr[i][1] for i in range(len(h_nr))]

bases_nrm = [h_nrm[i][0] for i in range(len(h_nrm))]
raices_nrm = [h_nrm[i][1] for i in range(len(h_nrm))]

bases_secante = [h_sec[i][0] for i in range(len(h_sec))]
raices_secante = [h_sec[i][1] for i in range(len(h_sec))]

plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f2")
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.plot(bases_nr, raices_nr, color='red', label='Newton-Raphson')
plt.plot(bases_nrm, raices_nrm, color='green', label='Newton-Raphson modificado')
plt.plot(bases_secante, raices_secante, color='purple', label='Metodo de la secante')
plt.legend(loc = 'best')
plt.show()

Acercando un poco mas:

bases_biseccion = [h_bis[i][0] for i in range(len(h_bis))]
raices_biseccion = [h_bis[i][1] for i in range(len(h_bis))]

bases_nr = [h_nr[i][0] for i in range(len(h_nr))]
raices_nr = [h_nr[i][1] for i in range(len(h_nr))]

bases_nrm = [h_nrm[i][0] for i in range(len(h_nrm))]
raices_nrm = [h_nrm[i][1] for i in range(len(h_nrm))]

bases_secante = [h_sec[i][0] for i in range(len(h_sec))]
raices_secante = [h_sec[i][1] for i in range(len(h_sec))]

plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f2 con zoom")
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.plot(bases_nr, raices_nr, color='red', label='Newton-Raphson')
plt.plot(bases_nrm, raices_nrm, color='green', label='Newton-Raphson modificado')
plt.plot(bases_secante, raices_secante, color='purple', label='Metodo de la secante')
plt.legend(loc = 'best')
plt.xlim(0, 16)
plt.show()

Podemos observar como Newton-Raphson modificado converge muy rapidamente, mientras que el resto tarda un poco mas, siendo en este caso el mas lento el metodo de la secante

Por último, corremos los algoritmos en f3(x)

 ### Bisección en f3(x)

print("Biseccion con tolerancia 1e^-5")
tolerancia = 1e-5
raiz1, h_bis = biseccion(f3, lim_inferior, lim_superior, tolerancia, max_iteraciones)
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))

print()
print()
print("Biseccion con tolerancia 1e^-13")

tolerancia = 1e-13
raiz2, h_bis = biseccion(f3, lim_inferior, lim_superior, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_bis)):
    print(str(h_bis[i][0]) + "\t" + str(h_bis[i][1]))

Vemos que son necesarias una considerable cantidad de iteraciones para que converja, especialmente para la segunda tolerancia. 
Analizando la raiz obtenida y comparando con el gráfico, parece ser muy cercana a 1.5, al igual que se observa.

 ### Newton-Raphson en f3

print("Newton-Raphson con tolerancia de 1e-5")

tolerancia = 1e-5
semilla = 1
raiz1, h_nr = newton_raphson(f3, df3, semilla, tolerancia, max_iteraciones)

print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_nr = newton_raphson(f3, df3, semilla, tolerancia, max_iteraciones)
print("Newton-Raphson con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr)):
    print(str(h_nr[i][0]) + "\t" + str(h_nr[i][1]))

Los resultados obtenidos indican que este algoritmo claramente no converge para la semilla dada, ya la solución correcta según el gráfico y el método de bisección usado en el paso anterior sugieren que la raíz es aproximadamente 1,5.

Probamos con una semilla más cercana a lo obtenido con bisección, para así verificar que la razón por la cual no convergió es una mala elección de la semilla.

tolerancia = 1e-13
semilla = 1.3
raiz2, h_nr_nueva_raiz = newton_raphson(f3, df3, semilla, tolerancia, max_iteraciones)
print("Newton-Raphson con tolerancia de 1e-13, semilla = 1.3")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nr_nueva_raiz)):
    print(str(h_nr_nueva_raiz[i][0]) + "\t" + str(h_nr_nueva_raiz[i][1]))


Efectivamente, al usar una semilla más cercana al valor real, obtenemos muy rápidamente una aproximación válida de la raíz. Vemos si esto se mantiene con Newton-Raphson modificado:

 ### Newton-Raphson modificado con f3

print("Newton-Raphson modificado con tolerancia de 1e-5")

semilla = 1
tolerancia = 1e-5
raiz1, h_nrm = newton_raphson_mod(f3, df3, ddf3, semilla, tolerancia, max_iteraciones)


print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))

print()
print()
tolerancia = 1e-13
raiz2, h_nrm = newton_raphson_mod(f3, df3, ddf3, semilla, tolerancia, max_iteraciones)
print()
print("Newton-Raphson modificado con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_nrm)):
    print(str(h_nrm[i][0]) + "\t" + str(h_nrm[i][1]))

Vemos que no converge porque entre la semilla y la raiz hay un punto en el que la derivada de la funcion vale cero

Finalmente, vemos los resultados que nos da buscar la raíz en esta función con el método de la secante:

 ### Método de la secante con f3

tolerancia = 1e-5
semilla_1 = 0
semilla_2 = 2
max_iteraciones = 50
raiz1, h_sec = secante(f3, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-5")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

print()
print()

tolerancia = 1e-13
raiz2, h_sec = secante(f3, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec)):
    print(str(h_sec[i][0]) + "\t" + str(h_sec[i][1]))

Vemos que para los valores x0=0 y x1=2 como semillas, el metodo no converge. Es decir, estas semillas no son buenas. Observamos que sucede si usamos semillas mas acordes:

semilla_1 = 1
raiz2, h_sec_mejor = secante(f3, semilla_1, semilla_2, tolerancia, max_iteraciones)
print("Metodo de la secante con tolerancia de 1e-13")
print("*******************************************")
print("Iteracion \t Raiz \t Tolerancia: " + str(tolerancia))
print("*******************************************")
for i in range(len(h_sec_mejor)):
    print(str(h_sec_mejor[i][0]) + "\t" + str(h_sec_mejor[i][1]))

Efectivamente, la razon por la cual no convergia eran las elecciones de las aproximaciones iniciales. Usando x0=1 y x1=2, converge solamente en 2 iteraciones.

Hacemos la comparativa de todos los metodos:

#Comparativa de historiales
bases_biseccion = [h_bis[i][0] for i in range(len(h_bis))]
raices_biseccion = [h_bis[i][1] for i in range(len(h_bis))]

bases_nr = [h_nr[i][0] for i in range(len(h_nr))]
raices_nr = [h_nr[i][1] for i in range(len(h_nr))]

bases_nr_2 = [h_nr_nueva_raiz[i][0] for i in range(len(h_nr_nueva_raiz))]
raices_nr_2 = [h_nr_nueva_raiz[i][1] for i in range(len(h_nr_nueva_raiz))]

bases_nrm = [h_nrm[i][0] for i in range(len(h_nrm))]
raices_nrm = [h_nrm[i][1] for i in range(len(h_nrm))]

bases_secante = [h_sec[i][0] for i in range(len(h_sec))]
raices_secante = [h_sec[i][1] for i in range(len(h_sec))]



plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f3")
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.plot(bases_nr, raices_nr, '--', color='red', label='Newton-Raphson')
plt.plot(bases_nr_2, raices_nr_2, color='brown', label='Newton-Raphson con mejor aproximacion')
plt.plot(bases_nrm, raices_nrm, '--',color='green', label='Newton-Raphson modificado')
plt.plot(bases_secante, raices_secante, '--', color='purple', label='Metodo de la secante')
plt.legend(loc = 'best')
plt.show()

Observamos como converge nada mas para el metodo de biseccion, y para Newton-Raphson con una mejor eleccion de la raiz. Nos concentramos especificamente en estos dos:

plt.figure()
plt.grid(True)
plt.title("Comparativa de metodos para f3 con zoom")
plt.plot(bases_biseccion, raices_biseccion, color='blue', label='Metodo de biseccion')
plt.plot(bases_nr_2, raices_nr_2, color='red', label='Newton-Raphson con mejor aproximacion')
plt.xlim(1, 8.5)
plt.ylim(0.99, 1.62)
plt.legend(loc = 'best')
plt.show()

En este ultimo grafico vemos como claramente Newton-Raphson sigue siendo mas rapido que Biseccion

 ## 3. c)

Para hallar las raíces reales en el intervalo, usamos el 'método de Brent', usando el módulo 'scipy'.
Este método es considerado uno de los mejores para la búsqueda de raíces 

ref: (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html) 

from scipy import optimize

Empezamos buscando las raíces de f1:

lim_inf = 0
lim_sup = 2

raiz1 = optimize.brentq(f1, lim_inf, lim_sup)

print("La raiz real es: " + str(raiz1))

Vemos que las encontradas con los métodos anteriores dentro del error indicado son correctas, tomando como referencia del valor real el valor obtenido con este método.

Ahora, corremos el mismo algoritmo con f2:

raiz2 = optimize.brentq(f2, lim_inf, lim_sup)

print("La raiz real es: " + str(raiz2))

Al igual que con f1, los resultados obtenidos con los métodos de bisección, Newton-Raphson y secante nos brindaron resultados correctos dentro de lo esperado.

Finalmente comparamos el valor real de f3 con lo obtenido:

raiz3 = optimize.brentq(f3, lim_inf, lim_sup)

print("La raiz real es: " + str(raiz3))

El resultado es el mismo obtenido por bisección, y por Newton-Raphson al elegir una semilla mejor que x=1.0



 ## 3. d)

 ### f1(x)


Primero, calculamos los órdenes de convergencia y constantes asintóticas para todos los métodos al ser aplicados en la primer función:

'''
Bisección
'''
lim_inferior = 0
lim_superior = 2
tolerancia = 1e-13
max_iteraciones = 50
raiz_b, historial_b = biseccion(f1, lim_inferior, lim_superior, tolerancia, max_iteraciones)

'''
Newton-Raphson
'''
semilla = 1
raiz_nr, historial_nr = newton_raphson(f1, df1, semilla, tolerancia, max_iteraciones)

'''
Newton-Raphson modificado
'''
raiz_nrm, historial_nrm = newton_raphson_mod(f1, df1, ddf1, semilla, tolerancia, max_iteraciones)

'''
Metodo de la secante
'''
semilla_1 = 0
semilla_2 = 2
raiz_sec, historial_sec = secante(f1, semilla_1, semilla_2, tolerancia, max_iteraciones)

Definimos ahora los metodos que usamos para calcular orden de convergencia

def alpha_n(x_n, x_sig, x_n_1, x_n_2):
    '''
    Recibe para un n dado sus dos anteriores, y calcula para estos valores una aproximacion del orden de convergencia
    Parametros:
        x_n -> Valor obtenido para un n dado
        x_sig -> Valor obtenido para x_n+1
        x_n_1 -> Valor anterior a x_n obtenido
        x_n_2 -> valor anterior a x_n_1 obtenido
    Retorno:
        El valor de alpha computado, o None si se quiere dividir por 0
    '''
    numerador = np.log(np.abs((x_sig - x_n) / (x_n - x_n_1)))
    denominador = np.log(np.abs((x_n - x_n_1)/(x_n_1 - x_n_2)))
    if np.abs(denominador) < 1e-15:
        print("Denominador demasiado cercano a 0: " + str(denominador))
        return None
    return (numerador / denominador)

def historial_ordenes(historial_raices):
    '''
    Recibe una lista con el historial de raices con tuplas de la forma (n_iter, raiz_candidato)
    devuelve una lista con el historial de las aproximaciones del orden de convergencia, con tuplas de la forma (n_iter, alpha)
    En caso de error, devuelve None
    '''
    h = []
    for x in range(2, len(historial_raices) - 1):
        x_n = historial_raices[x][1]
        x_sig = historial_raices[x+1][1]
        x_n_1 = historial_raices[x-1][1]
        x_n_2 = historial_raices[x-2][1]
        alpha = alpha_n(x_n, x_sig, x_n_1, x_n_2)
        if alpha is None: return None     
        h.append((x, alpha))
    return h


Evaluamos y graficamos los ordenes de convergencia paso a paso de los distintos metodos para f1:

#Biseccion
ordenes_bis_hist = historial_ordenes(historial_b)
base_bis = []
orden_bis = []
for i in range(len(ordenes_bis_hist)):
    base_bis.append((ordenes_bis_hist[i])[0])
    orden_bis.append((ordenes_bis_hist[i])[1])


#Newton-Raphson
ordenes_nr_hist = historial_ordenes(historial_nr)
base_nr = []
orden_nr = []
for i in range(len(ordenes_nr_hist)-1):
    base_nr.append((ordenes_nr_hist[i])[0])
    orden_nr.append((ordenes_nr_hist[i])[1])

#Newton-Raphson modificado
ordenes_nrm_hist = historial_ordenes(historial_nr)
base_nrm = []
orden_nrm = []
for i in range(len(ordenes_nrm_hist)-1):
    base_nrm.append((ordenes_nr_hist[i])[0])
    orden_nrm.append((ordenes_nr_hist[i])[1])

ordenes_secante_hist = historial_ordenes(historial_sec)
base_sec = []
orden_sec = []
for i in range(len(ordenes_secante_hist)):
    base_sec.append((ordenes_secante_hist[i])[0])
    orden_sec.append((ordenes_secante_hist[i])[1])

plt.figure()
plt.title("Historial de ordenes de convergencia para f1")
plt.plot(base_bis, orden_bis, 'k.', lw=2, color='blue', label='Biseccion')
plt.plot(base_nr, orden_nr, 'k. ', lw=1, color='green', label='Newton-Raphson')
plt.plot(base_nrm, orden_nrm, 'k. ', lw=1, color='red', label='Newton-Raphson modificado')
plt.plot(base_sec, orden_sec, 'k. ', lw=2, color='purple', label='Metodo de la secante')

plt.grid(True)
plt.legend(loc = 'best')
plt.show()

Vemos que, tal como esperabamos por la teoria, el orden de convergencia de biseccion es 1, el de Newton-Raphson normal y modificado es 2 (son los mismos valores), y para el metodo de la secante, alpha vale aproximadamente 1,6.

Para calcular la constante asintotica, usamos los alpha calculados y el valor 'real' de la raiz, tomando como una muy buena aproximacion el calculado usando la libreria Scipy.

def lambda_n(alpha, x_n, x_sig, raiz_real):
    num = abs(x_sig - raiz_real)    
    den = abs(x_n - raiz_real) ** alpha
    if np.abs(den) < 1e-15: return None
    return num / den

def historial_constante_asintotica(historial, raiz_real, alpha):
    '''
    Parametros:
        historial -> historial de las raices candidatas, lista con tuplas de la forma (n_iter, raiz_candidata)
        raiz_real -> la raiz real o una muy buena aproximacion a la misma
        alpha -> el orden de convergencia o una aproximacion del mismo
    Devuelve una lista de tuplas con la forma (n_iter, lambda)
    '''
    lambdas = []
    for i in range(len(historial) - 1):
        x_n = historial[i][1]
        x_sig = historial[i+1][1]
        n_iter = historial[i][0]
        const_asintotica = lambda_n(alpha, x_n, x_sig, raiz_real)
        lambdas.append((n_iter, const_asintotica))
    return lambdas
        


#Biseccion
alpha_biseccion = orden_bis[1]
lambda_bis_hist = historial_constante_asintotica(historial_b, raiz1, alpha_biseccion)
base_bis = []
lambda_bis = []
for i in range(len(lambda_bis_hist)):
    base_bis.append((lambda_bis_hist[i])[0])
    lambda_bis.append((lambda_bis_hist[i])[1])

#Newton-Raphson
alpha_nr = orden_nr[2]
lambda_nr_hist = historial_constante_asintotica(historial_nr, raiz1, alpha_nr)
base_nr = []
lambda_nr = []
for i in range(len(lambda_nr_hist)):
    base_nr.append((lambda_nr_hist[i])[0])
    lambda_nr.append((lambda_nr_hist[i])[1])

#Newton-Raphson modificado
alpha_nrm = alpha_nr
lambda_nrm_hist = historial_constante_asintotica(historial_nrm, raiz1, alpha_nrm)
base_nrm = []
lambda_nrm = []
for i in range(len(lambda_nrm_hist)):
    base_nrm.append((lambda_nrm_hist[i])[0])
    lambda_nrm.append((lambda_nrm_hist[i])[1])

#Metodo de la secante
alpha_sec = orden_sec[4]
lambda_sec_hist = historial_constante_asintotica(historial_sec, raiz1, alpha_sec)
base_sec = []
lambda_sec = []
for i in range(len(lambda_sec_hist)):
    base_sec.append((lambda_sec_hist[i])[0])
    lambda_sec.append((lambda_sec_hist[i])[1])



plt.figure()
plt.title("Historial de constantes asintoticas para f1")
plt.plot(base_bis, lambda_bis , lw=2, color='blue', label='Biseccion')
plt.plot(base_nr, lambda_nr, lw=2, color='green', label='Newton-Raphson')
plt.plot(base_nrm, lambda_nrm,  lw=2, color='red', label='Newton-Raphson modificado')
plt.xlim(1, 5)
plt.ylim(0, 2)
plt.grid(True)
plt.legend(loc = 'best')
plt.show()

Vemos que para Newton-Raphson modificado y el normal es aproximadamente 0,4 y para biseccion, vale cerca de 0,25 pero con algunos picos.

 ### f2(x)

Primero, obtenemos los historiales:

'''
Bisección
'''
lim_inferior = 0
lim_superior = 2
tolerancia = 1e-13
max_iteraciones = 50
raiz_b, historial_b = biseccion(f2, lim_inferior, lim_superior, tolerancia, max_iteraciones)

'''
Newton-Raphson
'''
semilla = 1
raiz_nr, historial_nr = newton_raphson(f2, df2, semilla, tolerancia, max_iteraciones)

'''
Newton-Raphson modificado
'''
raiz_nrm, historial_nrm = newton_raphson_mod(f2, df2, ddf2, semilla, tolerancia, max_iteraciones)

'''
Metodo de la secante
'''
semilla_1 = 0
semilla_2 = 2
raiz_sec, historial_sec = secante(f2, semilla_1, semilla_2, tolerancia, max_iteraciones)

#Biseccion
ordenes_bis_hist = historial_ordenes(historial_b)
base_bis = []
orden_bis = []
for i in range(len(ordenes_bis_hist)):
    base_bis.append((ordenes_bis_hist[i])[0])
    orden_bis.append((ordenes_bis_hist[i])[1])

#Newton-Raphson
ordenes_nr_hist = historial_ordenes(historial_nr)
base_nr = []
orden_nr = []
for i in range(len(ordenes_nr_hist)):
    base_nr.append((ordenes_nr_hist[i])[0])
    orden_nr.append((ordenes_nr_hist[i])[1])

#Newton-Raphson modificado
ordenes_nrm_hist = historial_ordenes(historial_nr)
base_nrm = []
orden_nrm = []
for i in range(len(ordenes_nrm_hist)):
    base_nrm.append((ordenes_nr_hist[i])[0])
    orden_nrm.append((ordenes_nr_hist[i])[1])

ordenes_secante_hist = historial_ordenes(historial_sec)
base_sec = []
orden_sec = []
for i in range(len(ordenes_secante_hist)):
    base_sec.append((ordenes_secante_hist[i])[0])
    orden_sec.append((ordenes_secante_hist[i])[1])

plt.figure()
plt.title("Historial de ordenes de convergencia para f2")
plt.plot(base_bis, orden_bis, 'k. ', color = 'blue', label='Biseccion')
plt.plot(base_nr, orden_nr, '--', lw=4,color='green', label='Newton-Raphson')
plt.plot(base_nrm, orden_nrm, lw=1, color='red', label='Newton-Raphson modificado')
plt.plot(base_sec, orden_sec, lw=1, color='purple', label='Metodo de la secante')
plt.xlim(1, 25)
plt.grid(True)
plt.legend(loc = 'best')
plt.show()

Vemos que todos los metodos tienen orden de convergencia 1 para esta funcion. En el caso de Newton-Raphson, no es 2 por lo explicado cuando aplicamos el algoritmo en f2.

Ahora, calculamos las constantes asintoticas

#Biseccion
alpha_biseccion = orden_bis[10]
lambda_bis_hist = historial_constante_asintotica(historial_b, raiz1, alpha_biseccion)
base_bis = []
lambda_bis = []
for i in range(len(lambda_bis_hist)):
    base_bis.append((lambda_bis_hist[i])[0])
    lambda_bis.append((lambda_bis_hist[i])[1])

#Newton-Raphson
alpha_nr = orden_nr[10]
lambda_nr_hist = historial_constante_asintotica(historial_nr, raiz1, alpha_nr)
base_nr = []
lambda_nr = []
for i in range(len(lambda_nr_hist)):
    base_nr.append((lambda_nr_hist[i])[0])
    lambda_nr.append((lambda_nr_hist[i])[1])

#Newton-Raphson modificado
alpha_nrm = alpha_nr
lambda_nrm_hist = historial_constante_asintotica(historial_nrm, raiz1, alpha_nrm)
base_nrm = []
lambda_nrm = []
for i in range(len(lambda_nrm_hist)):
    base_nrm.append((lambda_nrm_hist[i])[0])
    lambda_nrm.append((lambda_nrm_hist[i])[1])

#Metodo de la secante
alpha_sec = orden_sec[6]
lambda_sec_hist = historial_constante_asintotica(historial_sec, raiz1, alpha_sec)
base_sec = []
lambda_sec = []
for i in range(len(lambda_sec_hist)):
    base_sec.append((lambda_sec_hist[i])[0])
    lambda_sec.append((lambda_sec_hist[i])[1])



plt.figure()
plt.title("Historial de constantes asintoticas para f2")
plt.plot(base_bis, lambda_bis , lw=2, color='blue', label='Biseccion')
plt.plot(base_nr, lambda_nr, lw=2, color='green', label='Newton-Raphson')
plt.plot(base_nrm, lambda_nrm,  lw=2, color='red', label='Newton-Raphson modificado')
plt.plot(base_sec, lambda_sec,  lw=3, color='purple', label='Metodo de la secante')
plt.grid(True)
plt.xlim(0, 25)
plt.legend(loc = 'best')
plt.show()

Vemos como para todos los casos, la constante asintotica tiende a 1.

 ### f3(x)

Obtenemos los historiales:

'''
Bisección
'''
lim_inferior = 0
lim_superior = 2
tolerancia = 1e-13
max_iteraciones = 50
raiz_b, historial_b = biseccion(f3, lim_inferior, lim_superior, tolerancia, max_iteraciones)

'''
Newton-Raphson
'''
semilla = 1
raiz_nr, historial_nr = newton_raphson(f3, df3, semilla, tolerancia, max_iteraciones)

'''
Newton-Raphson modificado
'''
raiz_nrm, historial_nrm = newton_raphson_mod(f3, df3, ddf3, semilla, tolerancia, max_iteraciones)

'''
Metodo de la secante
'''
semilla_1 = 0
semilla_2 = 2
raiz_sec, historial_sec = secante(f3, semilla_1, semilla_2, tolerancia, max_iteraciones)

Luego, calculamos los ordenes de convergencia y graficamos:

#Biseccion
ordenes_bis_hist = historial_ordenes(historial_b)
base_bis = []
orden_bis = []
for i in range(len(ordenes_bis_hist)):
    base_bis.append((ordenes_bis_hist[i])[0])
    orden_bis.append((ordenes_bis_hist[i])[1])

#Newton-Raphson
ordenes_nr_hist = historial_ordenes(historial_nr)
base_nr = []
orden_nr = []
for i in range(len(ordenes_nr_hist)):
    base_nr.append((ordenes_nr_hist[i])[0])
    orden_nr.append((ordenes_nr_hist[i])[1])

#Newton-Raphson modificado
ordenes_nrm_hist = historial_ordenes(historial_nr)
base_nrm = []
orden_nrm = []
for i in range(len(ordenes_nrm_hist)):
    base_nrm.append((ordenes_nr_hist[i])[0])
    orden_nrm.append((ordenes_nr_hist[i])[1])

#Secante
ordenes_secante_hist = historial_ordenes(historial_sec)
base_sec = []
orden_sec = []
for i in range(len(ordenes_secante_hist)):
    base_sec.append((ordenes_secante_hist[i])[0])
    orden_sec.append((ordenes_secante_hist[i])[1])

plt.figure()
plt.title("Historial de ordenes de convergencia para f3")
plt.plot(base_bis, orden_bis, 'k. ', color = 'blue', label='Biseccion')
plt.plot(base_nr, orden_nr, lw=1,color='green', label='Newton-Raphson')
plt.plot(base_nrm, orden_nrm, 'k. ',lw=1, color='red', label='Newton-Raphson modificado')
plt.plot(base_sec, orden_sec, 'k. ',lw=1, color='purple', label='Metodo de la secante')
plt.grid(True)
plt.ylim(0.1, 1.3)
plt.legend(loc = 'best')
plt.show()

Vemos que los ordenes convergen a 1. Sin embargo, esto no es del todo claro ya que hubo metodos que no convergieron. Por lo tanto, consideramos los casos donde elejimos mejores semillas; para el metodo de la secante converge en tan solo dos iteraciones usando x0=1 y x1=2, por lo que sabemos que es claramente mejor que orden 1.

Vemos ahora las constantes asintoticas:

#Biseccion
alpha_biseccion = orden_bis[1]
lambda_bis_hist = historial_constante_asintotica(historial_b, raiz1, alpha_biseccion)
base_bis = []
lambda_bis = []
for i in range(len(lambda_bis_hist)):
    base_bis.append((lambda_bis_hist[i])[0])
    lambda_bis.append((lambda_bis_hist[i])[1])

#Newton-Raphson
alpha_nr = orden_nr[2]
lambda_nr_hist = historial_constante_asintotica(historial_nr, raiz1, alpha_nr)
base_nr = []
lambda_nr = []
for i in range(len(lambda_nr_hist)):
    base_nr.append((lambda_nr_hist[i])[0])
    lambda_nr.append((lambda_nr_hist[i])[1])

#Newton-Raphson modificado
alpha_nrm = alpha_nr
lambda_nrm_hist = historial_constante_asintotica(historial_nrm, raiz1, alpha_nrm)
base_nrm = []
lambda_nrm = []
for i in range(len(lambda_nrm_hist)):
    base_nrm.append((lambda_nrm_hist[i])[0])
    lambda_nrm.append((lambda_nrm_hist[i])[1])

#Metodo de la secante
alpha_sec = orden_sec[20]
lambda_sec_hist = historial_constante_asintotica(historial_sec, raiz1, alpha_sec)
base_sec = []
lambda_sec = []
for i in range(len(lambda_sec_hist)):
    base_sec.append((lambda_sec_hist[i])[0])
    lambda_sec.append((lambda_sec_hist[i])[1])


plt.figure()
plt.title("Historial de constantes asintoticas para f3")
plt.plot(base_bis, lambda_bis , lw=2, color='blue', label='Biseccion')
plt.plot(base_nr, lambda_nr, lw=2, color='green', label='Newton-Raphson')
plt.plot(base_nrm, lambda_nrm,  lw=2, color='red', label='Newton-Raphson modificado')
plt.plot(base_sec, lambda_sec,  lw=3, color='purple', label='Metodo de la secante')
plt.grid(True)
plt.legend(loc = 'best')
plt.xlim(0, 28)
plt.show()

Vemos que para biseccion, que converge el algoritmo, lambda vale aproximadamente 1.

 ### Comparativa de los metodos

Como conclusion, pudimos observar que, con una eleccion buena de la semilla, el metodo que converge de forma mas veloz es Newton-Raphson, tanto su version normal como la modificada. En caso de no elegir una buena, podria no converger. Una deseventaja de estos metodos, es que es necesario que la derivada sea distinta de 0 en todos los puntos del intervalo; a su vez, si es un valor chico (la funcion no es volatil), el orden de convergencia se altera y pasa a ser alpha = 1. 
Esto sucede similarmente con el metodo de la secante, con la ventaja de que no es necesario tener la derivada; sin embargo, necesitamos dos aproximaciones iniciales en vez de 1. 

En cambio, el metodo de biseccion, vemos que con solo cumplir la hipotesis de que existe exactamente una raiz en el intervalo, el algoritmo converge. Si bien lo hace mas lento que el resto de los metodos, es mas confiable.