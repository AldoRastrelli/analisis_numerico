from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

colors =  ["blue", "green", "pink", "violet", "yellow", "red"]

def graph(xis_array, tis_array, ks_max):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set(xlabel="ti", ylabel="x")
    
    for i in range(len(xis_array)):
        
        xi = xis_array[i]
        print("PARES para k: ", ks_max[i])
        print("xi, len: ", xi.size)
        print(xi)
        print("ti, len: ", len(tis_array))
        print(tis_array[0:xi.size])

        plt.plot(tis_array[0:xi.size], xi, label= "k" + str(ks_max[i]), color = colors[i])
        plt.legend(loc='upper right')
        
    # show the plot
    plt.show()
    return