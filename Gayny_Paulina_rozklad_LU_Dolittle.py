# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:32:19 2021

@author: HP
"""
import numpy
import math
from Gayny_Paulina_rozklad_LU_gauss import *

M1 =  numpy.array(
     [[1,1,1],
      [1,2,1],
      [3,0,4]])

M2 = numpy.array(
     [[-2,4,3,5],
      [1,-1,7,1],
      [3,0,-3,1],
      [1,1,0,2]])

#rozkład LU macierzy metodą Doolittle'a
#A = L * U
#przyjmuję wartosci na diagonali macierierzy L równe 1
#      A        =        L           *         U
#[[a11, a12, a13],  [[1,  0,   0],       [[u11, u12, u13],
#[a21, a22, a23], = [l21, 1,   0],   *   [0,   u22, u23],
#[a31, a32, a33]]   [l31, l32, 1]]       [0,    0,  u33]]

def Gayny_Paulina_rozklad_LU_Doolittle(A):
    n_A = len(A) #macierz kwadratowa, więc tyle samo kolumn i wierszy
    if n_A != len(A[0]): #gdy nie jest to macierz kwadratowa
        return "Nie można dokonać rozkładu LU"
    L = numpy.identity(n_A)
    U = numpy.zeros([n_A, n_A])
    s_L = 0 #pomocnicza suma dla macierzy L
    s_U = 0 #pomocnicza suma dla macierzy U
    for j in range(n_A): #wybór kolumny
        #w ustalonej kolumnie:
            
        for i in range(j + 1): #dla każdego wiersza aż do zrównania z indeksem kolumny (włącznie) obliczamy element dla macierzy U 
            for k in range(i): #obliczamy pomocniczą sumę z poprzednich elementów
                s_U = s_U + L[i][k] * U[k][j]
            #po wyjsciu z pętli liczącej sumę pomocniczą możemy obliczyć wartosć elementu
            U[i][j] = (1/(L[i][i])) * (A[i][j] - s_U)
            s_U = 0
            
        for i_2 in range(j + 1, n_A): #obliczamy pozostałe wiersze w kolumnie j, tym razem dla macierzy L
            for k_2 in range(j): #obliczamy pomocniczą sumę z poprzednich elementów
                s_L = s_L + L[i_2][k_2] * U[k_2][j]
            L[i_2][j] = (1/(U[j][j])) * (A[i_2][j] - s_L)
            s_L = 0
    return L, U

M11 = M1.copy()
L, U = Gayny_Paulina_rozklad_LU_Doolittle(M11)

print("\n\nmetoda Dolittle'a\nPrzykład1\n", M1,"\n=\n", L, "\n*\n", U)
#sprawdzenie czy poprawne
print("L * U =\n", L.dot(U))

M22 = M2.copy()
L, U = Gayny_Paulina_rozklad_LU_Doolittle(M22)
print("\n\nPrzykład2\n", M2,"\n=\n", L, "\n*\n", U)
#sprawdzenie czy poprawne
A_from_mult = L.dot(U)
print("L * U =\n", A_from_mult) #tutaj również widać stratę w dokładnosci
#z ciekawosci sprawdzę która metoda - Gaussa czy Dolittle - jest dokładniejsza (przy tej macierzy przynajmniej)
B_Dolittle = M2 - A_from_mult
print("macierz różnic\n", B_Dolittle)
#policzę pierwiastek z sumy kwadratow wszystkich roznic

def Blad(A):
    blad = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            blad = blad + A[i][j] * A[i][j]
    blad = math.sqrt(blad)
    return blad
    
print("\nbłąd dla metody Dolittle:", Blad(B_Dolittle))
print("błąd dla metody Gaussa:",  Blad(B_gauss))
print("Tyle razy większy jest bład dla metody Gaussa w porównaniu z metodą Dolittle'a:", Blad(B_gauss) / Blad(B_Dolittle))
#jak widać dla mojej macierzy 4x4 metoda Dolittle'a jest dużo dokładniejsza



            
    
    