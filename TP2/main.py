# coding=utf-8
from matrices import buildMatrixA, buildMatrixB, T
from gauss import gauss
from fourier import fourier_series_coeff_numpy, f
import numpy as np
from graph import graph 
from numpy import ones_like, cos, pi, sin, allclose

def main():
    k_max = 1
    a0, a, b, ti_array, xi = fourier_series_coeff_numpy(f, T, k_max)
    matrixA = buildMatrixA(ti_array.tolist(), k_max)
    matrixB = buildMatrixB(ti_array.tolist(), k_max, xi)
    # print(matrixA, matrixB)
    coefs = gauss(matrixA, matrixB)
    print("AX = B. Gauss con pivoteo parcial => X = ", coefs)
    
    graficar(coefs)

def graficar(coefs):

    ks_max = [ 1, 3, 13, 34, 55, 144]
    #ks_max = [ 3]
    st_array = []

    for k_max in ks_max:
        a0, a, b, ti, xi = fourier_series_coeff_numpy(f, T, k_max)
        st_array.append(s_t(coefs, ti.tolist(), xi, k_max))
    
    print(st_array)
    graph(st_array, ti.tolist(), ks_max)

    return 

def s_t(coefs, ti, xi, k_max):

    coef_a0 = coefs[0]
    coef_a1 = coefs[1]
    coef_b1 = coefs[2]
    
    sum = 0 
    N = k_max * 3
    for i in range(N):

        si = (xi[i] - (coef_a0 + coef_a1 * cos(2 * pi / T * ti[i]) + coef_b1 * sin(2 * pi / T * ti[i]))) **2
        # print("A1cos(wot): " + str(coef_a1 * cos(2 * pi / T * ti[i])))
        # print("b1sin(wot): " + str(coef_b1 * sin(2 * pi / T * ti[i])))
        # print("ti: " + str(ti[i]))
        # print("xi: " + str(xi[i]))
        # print("A0: " + str(coef_a0))
        # print("A1: " + str(coef_a1))
        # print("B1: " + str(coef_b1))
        # print("si: " + str(si))
        # print(" ")
        sum += si
    
    return sum

main()

