# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:42:03 2021

@author: HP
"""
import matplotlib.pyplot as plt
import math
from numpy import *

x = linspace(-5, 5, 10000)

y1 = x**2 -2*x + 1 #x^2 - 2x - y + 1 = 0
y2 = x**2 + 3 #x^2 - y + 3 = 0

plt.plot(x, y1, 'r') 
plt.plot(x, y2, 'b') 
plt.show()

def Gayny_Paulina_Newton_wielowymiarowy(x, y, eps):
    
    i = 0
    x_y = [x, y]
    x_next = [0, 0]
    norm = math.sqrt(x**2 + y**2)
    
    while(norm > eps):
        f1 = x_y[0]**2 - 2*x_y[0] - y + 1
        f2 = x_y[0]**2 - x_y[1] + 3
        J = array([[2*x_y[0] - 2, -1],
             [2*x_y[0], -1]])
        print(linalg.det(J))
        J_inv = linalg.inv(J)
        M = [f1, f2]
        
        x_next = x_y - J_inv.dot(M)
        x_y = x_next
        norm = math.sqrt(x_y[0]**2 + x_y[1]**2)
        print(norm)
    if norm < eps:
        return x_y
    
P = Gayny_Paulina_Newton_wielowymiarowy(-10, 2, 0.01)
print("Miejsce zerowe dla f1 w", P)
    