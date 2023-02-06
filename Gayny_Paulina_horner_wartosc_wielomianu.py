# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:44:33 2021

@author: HP
"""
#a to tablica współczynników wielomianu
#x to liczba od jakiej liczymy wartosc wielomianu
def Gayny_Paulina_horner(a, x):
    suma = 0 #zaczynamy od a0, ale to zapewnione w pętli
    for k in range(len(a)):
        suma = a[k] + x*suma #wielomian = współczynnik + x*dotychczasowy_wielomian (dopóki mamy współczynniki)
    return suma

A = [1, 0, 4, 2]
B = [-3,3, 0, 2]

print("Wartosc wielomianu o współczynnikach z A dla 3 to\n", Gayny_Paulina_horner(A, 3))
print("Wartosc wielomianu o współczynnikach z B dla -2 to\n", Gayny_Paulina_horner(B, -2))
print("Wartosc wielomianu o współczynnikach z A dla 2E7 to\n", Gayny_Paulina_horner(A, 2E7))