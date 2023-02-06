# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 01:28:04 2021

@author: HP
"""
import math
from numpy import *

#algorytm Jacobiego służący do znajdowania wartosci własnych zadanej symetrycznej macierzy A o wartosciach rzeczywistych

# A - symetryczna, rzeczywista macierz o rozmiarze n × n
# eps - precyzja obliczeń
def Gayny_Paulina_Jacobi(A, eps):
    
    A_T = transpose(A)
    
    if len(A) != len(A[0]) or array_equal(A, A_T) == False:
        return
    
    maks_p = 1 #pozycja maksymalnego - startowo pierwszy pod diagonalą
    maks_q = 0
    
    while abs(A[maks_p][maks_q]) > eps:
      #1 - wyszukanie największego co do modułu elementu poza diagonalą
      for i in range(1, len(A)):
          for j in range(i): #pod diagonalą szukam
              if abs(A[i][j]) > abs(A[maks_p][maks_q]):
                  maks_p = i
                  maks_q = j
                  
      #2 - wyliczenie kąta obrotu
      if A[maks_p][maks_p] - A[maks_q][maks_q] == 0:
          teta = math.pi/4
      else:
          teta = (1/2)*math.atan((2*A[maks_p][maks_q])/(A[maks_p][maks_p] - A[maks_q][maks_q]))
          
      T = identity(len(A))
      T[maks_p][maks_p] = math.cos(teta)
      T[maks_q][maks_q] = math.cos(teta)
      T[maks_p][maks_q] = -math.sin(teta)
      T[maks_q][maks_p] = math.sin(teta)
      #print(T)
      T_inv = linalg.inv(T)
      #print(T_inv)
      
      #print(A[maks_p][maks_q] > eps, " 1", A[maks_p][maks_q], " ", teta, maks_p, maks_q)
      
      #3 - wyliczenie nowej macierzy A
      A = T_inv.dot(A)
      A = A.dot(T)
      
      #ponownie liczę maksymalny element - może dałoby się ładniej ale tak oszczędzę czasu
      for i in range(1, len(A)):
          for j in range(i): #pod diagonalą szukam
              if abs(A[i][j]) > abs(A[maks_p][maks_q]):
                  maks_p = i
                  maks_q = j
      
      #print(A[maks_p][maks_q] > eps, " 2", A[maks_p][maks_q], " ", teta)
      
    return A

#uwaga: wartosci własne liczą się prawidłowo we wszystkich kombinacjach jakie próbowałam, natomiast w przypadku gdy app = aqq i kąt obrotu jest pi/4 kolejne macierze przestają być symetryczne, ale nie wpływa to na wynik. Niestety nie mam już czasu się nad tym zastanawiać

A = [[1, 4], 
     [4, 1]]

print(Gayny_Paulina_Jacobi(A, 0.001), "\n")

A = [[7, 4], 
     [4, 1]]

print(Gayny_Paulina_Jacobi(A, 0.001), "\n")


A = [[1, 2, 3],
     [2, 2, 3], 
     [3, 3, 1]]

print(Gayny_Paulina_Jacobi(A, 0.001), "\n")
      

A = [[1, 2, 3, 7],
     [2, 3, 3, 8], 
     [3, 3, 1, 5],
     [7, 8, 5, 2]]

print(Gayny_Paulina_Jacobi(A, 0.001), "\n")