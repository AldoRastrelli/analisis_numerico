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
    #print("AX = B. Gauss con pivoteo parcial => X = ", coefs)
    
    graficar()

def graficar():

    ks_max = [ 1, 3, 13, 34, 55, 144]
    #ks_max = [ 5]
    x_array = []

    x_array = []
    for k_max in ks_max:
        a0, a, b, ti, xi = fourier_series_coeff_numpy(f, T, k_max)
        xi_array = get_values(a0, a, b, ti.tolist(), k_max) # array de xis para tis
        

        for i in range(len(xi_array)):
            xi_array[i] = xi[i] - xi_array[i]

        print(xi_array)

        x_array.append(xi_array)
    
    print(x_array)
    graph(x_array, ti.tolist(), ks_max)
    

    return 

def get_values(a0, a, b, ti, k_max):

    xi = []

    for t in ti:
        if(a.size == 0 and b.size == 0):
            xi.append(a0/2)
            continue
            
        xi.append(a0/2.+sum([a[k-1]* sin(2.* pi * k * t / T ) + b[k-1] * cos(2.* pi *
 k * t / T) for k in range(1, k_max+1)]))
        # suma = 0
        # for k in range(1,k_max+1):
        #     suma += a0/2 + (a[k-1] * sin( 2. * pi * (k) * t / T ) + b[k-1] * cos( 2. * pi * (k) * t / T))
        # xi.append(suma)

    print(xi)
    return xi

main()