# coding=utf-8
import numpy as np
from numpy import ones_like, cos, pi, sin, allclose
T = 1.

def fourier_series_coeff_numpy(f, T, k_max):
    """Calcula el primer coeficiente de la serie de Fourier 2 * k_max + 1 de una función periódica.

    Dada una función periódica f (t) con período T, esta función devuelve el
    coeficientes a0, {a1, a2, ...}, {b1, b2, ...} tales que:

    f (t) ~ = a0 / 2 + sum_ {i = 1} ^ {k_max} (a_i * cos (2 * pi * i * t / T) + b_i * sin (2 * pi * i * t / T) )

    Parámetros
    ----------
    f: la función periódica, una invocable como f (t)
    T: el período de la función f, de modo que f (0) == f (T)
    N_max: la función devolverá el primer N_max + 1 coeficiente de Fourier.

    Devoluciones
    -------
    si return_complex == False, la función devuelve:

    a0: flotar
    a, b: numerosos arreglos flotantes que describen respectivamente el coeficiente de coseno y seno.

    si return_complex == True, la función devuelve:

    c: matriz numérica unidimensional de valores complejos de tamaño k_max + 1

    """

    # usamos una frecuencia de muestra más grande que la frecuencia de la señal
    f_sample =  2 * k_max
    
    ti_array, dt = np.linspace(0, T, f_sample, endpoint=False, retstep=True)

    x = np.fft.rfft(f(ti_array)) / ti_array.size

    xi  = x * 2
    return xi[0].real, xi[1:-1].real, -xi[1:-1].imag, ti_array, f(ti_array)

def f(t):
    """funcion periódica en [0,T]"""

    size = len(t)
    x_i = []

    anterior = 0
    siguiente = 1

    for ti in t:
        if (ti < T/2):
            x_i.append(1)
        else:
            x_i.append(-1)
    return x_i


#descomentar para prueba
# k_max = 144
# a0, a, b, ti_array, xi = fourier_series_coeff_numpy(f, T, k_max)
# print("a0: ", a0)
# print("a: ", a)
# print("b: ", b)
# print("ti_array: ", ti_array)

