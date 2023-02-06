# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:45:20 2021

@author: HP
"""

import numpy as np

#dzielenie wielomianu przez dwumian
#a to tablica współczynników wielomianu przez którego dzielimy (od współczynnika przy najwyższej potędze x)
#c to wartosc z dwumianu (x - c) przez którego dzielimy

def Gayny_Paulina_horner(a, c):
    if len(a) <= 1: #gdy w(x) to tylko liczba lub jest puste
        return "nie można podzielić tego wielomianu"
    b = np.zeros(len(a) - 1)
    b[0] = a[0] #bn-1 = an gdzie n to długosc a, u nas tablica współczynników od największych więc np. an to a[0], bn-1 to b[0] (największe współczynniki tych tablic)
    for i in range(1, len(b)):
        b[i] = a[i] + c*b[i - 1] #np. bn-2 = an-1 + c*bn-1 (zapis jest inny bo liczymy od pierwszych elementów tablic)
    #po zakończeniu pętli wyliczamy resztę r
    r = a[len(a) - 1] + c*b[len(b) - 1]
    return b, r

A = [1, 0, 3, -2] #x^3 + 3x - 2
B = [9, 12, -8, 0, 3] #9x^4 + 12 x^3 - 8x^2 + 3
C = [2, 1] #2x + 1

c = 2 #(x-2)
d = -1 #(x+1)

print("współczynniki wielomianu będącego wynikiem dzielenia wielomianu o współczynnikach z\n",A,"przez x -",c,"oraz reszta r z dzielenia:\n", Gayny_Paulina_horner(A, c),"\n")
print("współczynniki wielomianu będącego wynikiem dzielenia wielomianu o współczynnikach z\n",B,"przez x + 1 oraz reszta r z dzielenia:\n", Gayny_Paulina_horner(B, d),"\n")      
print("współczynniki wielomianu będącego wynikiem dzielenia wielomianu o współczynnikach z\n",C,"przez x + 1 oraz reszta r z dzielenia:\n", Gayny_Paulina_horner(C, d),"\n")       