import numpy as np
import math

INICIO_INTERVALO = 0
FINAL_INTERVALO = 2

class FuncionDerivable:

    def __init__(self, funcion, derivada, derivada_doble):
        self.funcion = funcion
        self.derivada = derivada
        self.derivada_doble = derivada_doble

def f1(x):
    return (x**2 - 2)

def df1(x):
    return 2 * x

def ddf1(x):
    return 2.0 + x * 0

def f2(x):
    return (x**5 - 6.6*x**4 + 5.12*x**3 + 21.312*x**2 - 38.016*x + 17.28)

def df2(x):
    return 5.0 * x**4 - 26.4 * x**3 + 15.36 * x**2 + 42.624 * x - 38.016

def ddf2(x):
    return 20.0 * x **3 - 79.2 * x** 2 + 30.72 * x + 42.624  

def f3(x):
    return ((x-1.5)*(math.e)**(-4*(x-1.5)**2))

def df3(x):
    return -8 * math.e**(-4 * (x-1.5)**2) * x **2 + 24 * math.e**(-4 * (x-1.5)**2) * x -17 * math.e**(-4 * (x-1.5)**2)

def ddf3(x):

    return 64 * math.e**(-4 * (x-1.5)**2) * x**3 - 288 * math.e**(-4 * (x-1.5)**2) * x**2 + 408 *math.e**(-4 * (x-1.5)**2) * x - 180 * math.e**(-4 * (x-1.5)**2)
