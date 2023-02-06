# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:19:42 2021

@author: HP
"""
import math
import numpy

#zastosowanie obrotów Givensa do zerowania wartosci wektora

#v = [v1, v2, ... , vn]
#w = ||v|| * [1, 0, 0, ...]
def Gayny_Paulina_Givens(v):
    i = len(v) - 2
    while i >= 0:
        fi = math.atan(v[i + 1]/v[i]) #kąt obrotu
        
        I = numpy.identity(len(v))
        I[i][i] = math.cos(fi)
        I[i + 1][i + 1] = math.cos(fi)
        I[i][i + 1] = math.sin(fi)
        I[i + 1][i] = -math.sin(fi)
        
        v = I.dot(v)
        
        i = i - 1
    w = v
    return w

v = [3, 2]
w = Gayny_Paulina_Givens(v)
print(w, "\n") #myslę że rząd wielkosci E-16 jest wystarczająco blisko zera żeby można było uznać te elementy za "wyzerowane"

v = [2, 3, 4]
w = Gayny_Paulina_Givens(v)
print(w, "\n")

v = [5, -3, 40]
w = Gayny_Paulina_Givens(v)
print(w, "\n")

v = [10, 1, 1, 1]
w = Gayny_Paulina_Givens(v)
print(w)