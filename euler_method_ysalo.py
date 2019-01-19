import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt


'''
Convert user input string to an executable function. 
CAUTION eval() converts user input into executable code. 
'''
def get_differential():
    expression = input('Enter the differential equation using Python math syntax in terms of x and y\ndy/dx = ')
    diff = lambda x,y: eval(expression)
    return diff

'''
Run eulers method to approximate the solution. 

Parameters: 
    equation: differential 
    stop: the desired guess 
    init_x: initial x 
    init_y: initial y 
    h: step interval
'''
def euler_method(equation, stop,init_x, init_y, h):
    #list to return with cord_y being the guesses at cord_x
    cord_x = []
    cord_y = []
    y_curr = init_y
    x_curr = init_x 
    h_curr = h

    while ( not compare_floats(x_curr, stop + h)):
        try: 
            cord_x.append(x_curr)
            cord_y.append(y_curr)
            y_prev = equation(x_curr, y_curr)
            y_curr = y_curr + h * y_prev
            x_curr = init_x + h_curr
        except ZeroDivisionError:
            pass
        finally: 
            if(abs(x_curr) > abs(stop + h)):
                raise ValueError('The step is too large.')
            h_curr += h

    return (cord_x,cord_y)

def compare_floats(f1,f2):
    return abs(f1 - f2) <= 0.000001

def main():
    #user input
    equation = get_differential()
    stop = float(input('approximate unil x_n = '))
    init_x = float(input('initial condition x_0 = '))
    init_y = float(input('f(x_0) = '))
    h = float(input('h = '))

    cord_x, cord_y = euler_method(equation, stop,init_x, init_y, h)
    df = pd.DataFrame({'x ' : cord_x, '\u2248y(x) ' : cord_y}) #dataframes are easy to print and graph
    df.index += 1 #for printing
    with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
        print(df)

    '''plot the approximate solution curve'''
    df.plot(x = 'x ', y= '\u2248y(x) ') 
    plt.show()

main()