from scipy import optimize
import math

def main():

    print("\n** OBTENCIÓN DE RAÍCES CON SCIPY**\n")

    print("Intervalo: [0,2]")

    print("\nRaíz/raíces f1(x):")
    print(optimize.brentq(f1,0,2))

    print("\nRaíces f2(x):")
    print(optimize.brentq(f2,0,2))

    print("\nRaíces f3(x):")
    print(optimize.brentq(f3,0,2))

    return

def f1(x):
    return (x**2 - 2)

def f2(x):
    return (x**5 - 6.6*x**4 + 5.12*x**3 + 21.312*x**2 - 38.016*x + 17.28)

def f3(x):
    return ((x-1.5)*(math.e)**(-4*(x-1.5)**2))

main()