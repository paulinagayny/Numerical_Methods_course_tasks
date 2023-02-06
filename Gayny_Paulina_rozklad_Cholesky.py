# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:35:33 2021

@author: HP
"""
import numpy
import math

M1 =  numpy.array(
     [[1,1,1],
      [1,3,1],
      [1,1,4]])

M2 = numpy.array(
     [[2, 0, 0,0],
      [0, 9,-2,0],
      [0,-2,10,1],
      [0, 0, 1,2]])

#funkcja tworząca rozkład LL_T macierzy metodą Cholesky'ego

#zakładam że macierz A jest symetryczna względem diagonali i że jest okreslona dodatnio
#dla swoich macierzy testowych sprawdziłam te warunki

def Gayny_Paulina_rozklad_cholesky(A):
    n_A = len(A) #macierz kwadratowa, więc tyle samo kolumn i wierszy
    if n_A != len(A[0]): #gdy nie jest to macierz kwadratowa
        return "Nie można dokonać rozkładu LU"
    L = numpy.zeros([n_A, n_A])
    s_D = 0 #pomocnicza suma dla elementów z diagonali
    s = 0 #pomocnicza suma dla elementów spod diagonali
    for j in range(n_A): #wybór kolumny
        #w ustalonej kolumnie:
        
        for i in range(j, n_A):
            #dla elementów z diagonali
            if i == j:
                for k1 in range(j): #dla każdej poprzedniej kolumny w naszym wierszu
                    s_D = s_D + L[i][k1] * L[i][k1]
                L[i][j] = math.sqrt(A[i][j] - s_D)
                s_D = 0
            
            #dla elementów spod diagonali
            for k2 in range(j): #dla każdej poprzedniej kolumny w naszym wierszu
                s = s + L[i][k2] * L[j][k2]
            L[i][j] = (1/(L[j][j])) * (A[i][j] - s)
            s = 0
    return L

M11 = M1.copy()
L = Gayny_Paulina_rozklad_cholesky(M11)
print("\n A =\n", M1,"\nL=\n", L)
#sprawdzenie czy poprawne
L_T = numpy.transpose(L)
print("L * L_T =\n", L.dot(L_T))

M22 = M2.copy()
L = Gayny_Paulina_rozklad_cholesky(M22)
print("\n A=\n", M2,"\nL=\n", L)
#sprawdzenie czy poprawne
L_T = numpy.transpose(L)
print("L * L_T =\n", L.dot(L_T))
