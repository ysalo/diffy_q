import numpy as np
from matplotlib import pyplot as plt
from math import *
import random

#plot settings
fig = plt.figure()
ax = fig.gca()

ax.set_ylabel('y-axis')
ax.set_xlabel('x-axis')
ax.set_xticks(np.arange(-10, 11, 1))
ax.set_yticks(np.arange(-10, 11, 1))
ax.set_ylim([-10, 10])
ax.set_xlim([-10, 10])
# plt.axhline(0, color='black')
# plt.axvline(0, color='black')

'''
Graph a single line segment with the (x,y) coordinate,
slope and lenght.
'''
def graph_segment(x, y, slope, length):
    #find the offset of where the point should be
    x_offset = length * cos(atan(slope))
    y_offset = length * sin(atan(slope))

    #draw the segment at from the center of the point
    x_neg = x - x_offset
    y_neg = y - y_offset
    x_pos = x + x_offset
    y_pos = y + y_offset
    ax.plot([x_neg, x_pos], [y_neg, y_pos ],color='skyblue')

'''
Convert user input string to an executable function. 
CAUTION eval() will convert what ever the user writes, which could cause problems. 
'''
def get_differential():
    expression = input('Enter the differential equation using Python math syntax in terms of x and y\ndy/dx = ')
    ax.set_title("dy/dx = " + expression)
    diff = lambda x,y: eval(expression)
    return diff

'''
Graph the slope field of a give equation.
'''
def graph_field(equation):
    step = 0.5 #determines the number of line segments
    length = step / 2  #determines the length of the line segments
    x = -10
    y = -10
    #could probably do something more clever
    while x <= 10:         
        while y <= 10:
            try:
                slope = equation(x,y)
                graph_segment(x,y,slope,length) 
            except ZeroDivisionError:
                pass
            finally:
                y += step
        y = -10
        x += step
        
         
def main():
    equation = get_differential()
    graph_field(equation)
    plt.show() 

main()