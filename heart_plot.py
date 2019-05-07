## this function plots a red heart assembled from a line
## by Sean X.L. with Python 3.6
## function employed:
##   f(x) = x^(2/3) + 0.9*(3.3-x^2)^(1/2)*sin(a*pi*x)
##   set x from -1.81 to +1.81,  a is set to be 20.

import math
import matplotlib.pyplot as plt

def heart_plot(a=20):
    '''draw a heart of line'''
    x = [xx/100 for xx in range(-181, +182, 1)]
    y = [(xx**2)**(1/3)+0.9*(3.3-xx**2)**0.5*math.sin(math.pi*a*xx) for xx in x]
    plt.plot(x,y,'r-')
    plt.show()
    return

if __name__ == "__main__":
    heart_plot()
    print("A heart is plotted")

