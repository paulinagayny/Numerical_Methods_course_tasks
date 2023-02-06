# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:16:56 2021

@author: HP
"""

#trzeba sprawdzić czy macierz jest diagonalnie dominująca, bo to warunek
#na to żeby metoda tworzyła ciąg zbieżny do rozw. układu Ax = b
#Macierz dominująca to macierz, której wartosci bezwzględne elementów na 
#głównej przekątnej są większe lub
#równe od sumy warto±ci bezwzgl¦dnych pozostaªych elementów w wierszach
def Czy_macierz_diagonalnie_dominujaca(A):
    s = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i!=j:
                s = s + A[i][j]
        #po przejsciu wszystkich kolumn
        if A[i][i] < s:
            return 0
        s = 0
                
#funkcja do algorytmu Jacobiego iteracyjnego rozwiązywania równań liniowych
#bez wykorzystania wzorów macierzoweych, czyli jak rozumiem korzystamy
#ze wzorów na składowe wektora niewiadomych
def Gayny_Paulina_jacobi(A, b, eps):
    if Czy_macierz_diagonalnie_dominujaca(A) == 0:
        return "Metoda Jacobiego nie może być zastosowana"
    