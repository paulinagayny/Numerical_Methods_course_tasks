# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:49:06 2021

@author: HP
"""
import math
# A*x = b, A to macierz współczynników układu równań, b - wektor wyrazów wolnych
#eliminacja Gaussa-Jordana bez wyboru elementu podstawowego
#korzystając z napisanego już algorytmu na eliminację Gaussa z zeszłych zajęć

M1 = [[1,1,1],
      [1,2,1],
      [3,0,4]]

M2 = [[-2,4,3,5],
      [1,-1,7,1],
      [3,0,-3,1],
      [1,1,0,2]]

b1 = [2,1,-1]

b2 = [1,3,2,0]

def Gayny_Paulina_gauss_jordan(A, b):
    R = A
    n_M = len(A) #wiersze
    if n_M != len(b) or len(b) == 0 or n_M == 0 or len(A[0]) == 0: #jeżeli różna liczba wierszy
        return "wynikiem jest zbiór pusty"
    for i in range(n_M): #wiersz który jest odejmowany (dlaczego aż do n_M????)
        m_pomocniczy = (1/R[i][i])
        #doprowadzenie do jedynki na diagonali przez przemnożenie całego wiersza
        b[i] = m_pomocniczy * b[i]
        for f in range(i, n_M): #wszystkie kolumny w tym wierszu
            R[i][f] = m_pomocniczy * R[i][f]
        for j in range(n_M): #zerowany wiersz
            if j != i:
                m = (R[j][i])/(R[i][i]) #mnożnik obliczany przy każdym zerowanym wierszu
                b[j] = b[j] - m*b[i]
                for k in range(i, n_M): #dla każdej kolumny wiersza którego zerujemy
                    R[j][k] = R[j][k] - m*R[i][k]             
    return b

print ("wektor x =", Gayny_Paulina_gauss_jordan(M1, b1))
print("wektor x =", Gayny_Paulina_gauss_jordan(M2, b2))
print("wektor x =", Gayny_Paulina_gauss_jordan(M1, b2))
print("wektor x =", Gayny_Paulina_gauss_jordan(M2, b1))

x1 = (273/16)*math.pi*math.pi*math.pi*math.pi
x2 = (73/8)*math.pi*math.pi*math.pi
x3 = (21/4)*math.pi*math.pi
x21 = (73/8)*math.pi*math.pi*math.pi
x22 = (21/4)*math.pi*math.pi
x23 = (7/2)*math.pi
x31 = (21/4)*math.pi*math.pi
x32 = (7/2)*math.pi
x33 = 4
M3 = [[ x1, x2, x3],
      [ x21, x22, x23],
      [ x31, x32, x33]]
b3 = [-(33/8)*math.pi*math.pi*math.pi, (-9/4)*math.pi*math.pi, (-5/2)*math.pi]
print("wektor x =", Gayny_Paulina_gauss_jordan(M3, b3))