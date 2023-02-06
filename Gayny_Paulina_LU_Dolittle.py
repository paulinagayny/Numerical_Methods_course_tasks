# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 01:44:49 2021

@author: HP
"""

#rozkład LU metodą Dolittle'a
#przyjmuję wartosci na diagonali macierierzy L równe 1
#      A        =        L           *         U
#[[a11, a12, a13],  [[1,  0,   0],       [[u11, u12, u13],
#[a21, a22, a23], = [l21, 1,   0],   *   [0,   u22, u23],
#[a31, a32, a33]]   [l31, l32, 1]]       [0,    0,  u33]]

import numpy

def Gayny_Paulina_LU_Dolittle(A):
    #zakładam że pracujemy na macierzach kwadratowych
    n_A = len(A)
    if n_A != len(A[0]):
        return "Nie można dokonać rozkładu LU"
    L = numpy.identity(len(A))
    U = numpy.zeros([len(A), len(A)])
    U[0][0] = A[0][0]
    s = 0 #pomocnicza suma
    for i in range(1, n_A):
        for k in range(n_A):
            L[i][k] = A[i][k]/U[]