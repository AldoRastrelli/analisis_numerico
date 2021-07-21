# coding=utf-8
import numpy as np
from numpy import ones_like, cos, pi, sin, allclose
from gauss import gauss
T = 1

from fourier import fourier_series_coeff_numpy, f

def buildMatrixA(ti_array, k_max):

    matrixA = []

    fila1 = 0
    fila2 = 1
    fila3 = 2

    for i in range(3):
        matrixA.append([])

    # primer fila de la matriz
    matrixA[fila1].append(k_max*3)
    matrixA[fila1].append( calc_sum( k_max, ti_array, calc_cos) )
    matrixA[fila1].append( calc_sum( k_max, ti_array, calc_sen) )

    # segunda fila de la matriz
    matrixA[fila2].append( calc_sum( k_max, ti_array, calc_cos))
    matrixA[fila2].append( calc_sum( k_max, ti_array, calc_cos_cuad) )
    cos_sen = calc_sum( k_max, ti_array, calc_sen, calc_cos)
    matrixA[fila2].append( cos_sen )

    # tercera fila de la matriz
    matrixA[fila3].append(calc_sum( k_max, ti_array, calc_sen))
    matrixA[fila3].append( cos_sen )
    matrixA[fila3].append( calc_sum( k_max, ti_array, calc_sen_cuad) )

    return matrixA

def buildMatrixB(ti_array, k_max, xi_array):

    matrixB = []

    # primer fila de la matriz
    matrixB.append( calc_sum_xi( k_max, ti_array, xi_array) )

    # segunda fila de la matriz
    matrixB.append( calc_sum_xi( k_max, ti_array, xi_array, calc_cos) )
    
    # tercera fila de la matriz
    matrixB.append( calc_sum_xi( k_max, ti_array, xi_array, calc_sen) )

    return matrixB

def calc_sum( k_max, ti_array, funcF = lambda x: 1, funcG = lambda x: 1):
    res = 0.0
    for i in range(k_max*3):
        res += funcF(ti_array[i]) * funcG(ti_array[i])
    
    return res

def calc_sum_xi( k_max, ti_array, xi, funcF = lambda x: 1):
    res = 0.0
    for i in range(k_max*3):
        res += xi[i] * funcF(ti_array[i])   
    return res

# TODO deberia redondear a cero si es menor a 10*-15, np.isClose
def calc_cos(ti):
    # radianes
    return cos((2 * pi / T) * ti)

def calc_sen(ti):
    #radianes
    return sin((2 * pi / T) * ti)

def calc_cos_cuad(ti):
    # radianes
    return cos((2 * pi / T) * ti) ** 2

def calc_sen_cuad(ti):
    #radianes
    return sin((2 * pi / T) * ti) ** 2
