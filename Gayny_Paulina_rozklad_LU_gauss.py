# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:19:03 2021

@author: HP
"""

import numpy

M1 =  numpy.array(
     [[1,1,1],
      [1,2,1],
      [3,0,4]])

M2 = numpy.array(
     [[-2,4,3,5],
      [1,-1,7,1],
      [3,0,-3,1],
      [1,1,0,2]])

#algorytm rozkładu LU przy wykorzystaniu eliminacji Gaussa
# A = L * U

def Gayny_Paulina_rozklad_LU_gauss(A):
    I = numpy.identity(len(A))
    L, U = Gayny_Paulina_gauss_pomocniczy(A, I) #przekazujemy macierz jednostkową którą przekształcimy do L
    return L, U

def Gayny_Paulina_gauss_pomocniczy(A, L): #taki "niby gauss" bo bez wektora wyrazów wolnych, po prostu doprowadzam do macierzy U
    #pod koniec A będzie macierzą U
    n_M = len(A) #wiersze
    if n_M == 0 or len(A[0]) == 0: #jeżeli różna liczba wierszy
        return "wynikiem jest zbiór pusty"
    for i in range(n_M - 1):
        for j in range(i + 1, n_M):
            m = (A[j][i])/(A[i][i])
            L[j][i] = m
            for k in range(i, n_M): #czesc dla U
                A[j][k] = A[j][k] - m*A[i][k]
    return L, A

M11 = M1.copy()
L, U = Gayny_Paulina_rozklad_LU_gauss(M11)
print("\nrozkład LU przy pomocy metody Gaussa\nPrzykład1\n", M1,"\n=\n", L, "\n*\n", U, "\n")
#sprawdzenie czy poprawne
print("L * U =\n", L.dot(U), "\n\n\n")

M22 = M2.copy()
L, U = Gayny_Paulina_rozklad_LU_gauss(M22)
print("\nPrzykład2\n", M2,"\n=\n", L, "\n*\n", U, "\n\n")
#sprawdzenie czy poprawne
print("L * U =\n", L.dot(U), "\n\n\n") #widać stratę w dokładnosci
A_from_mult = L.dot(U)
B_gauss = M2 - A_from_mult
print("macierz różnic\n", B_gauss)