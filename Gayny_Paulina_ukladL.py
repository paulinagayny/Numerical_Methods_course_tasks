# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:10:25 2021

@author: HP
"""

L1 = [[1,0,0],
      [3,2,0],
      [2,1,4]]

L2 = [[-5,0,0,0],
      [7,-1,0,0],
      [2,1,-3,0],
      [-2,4,3,5]]

b1 = [2,1,-1]

b2 = [1,3,2,0]

#L*x=b gdzie L to macierz dolna trójkątna [,]
#b to wektor wyrazów wolnych

def Gayny_Paulina_UkladL(L, b):
    x = b #wymiarowo takie same
    m_L = len(L) #liczba wierszy macierzy L
    n_L = len(L[0]) #liczba kolumn macierzy L
    s = 0 #pomocnicza suma
    
    if m_L != len(b) or len(b) == 0 or m_L == 0 or n_L == 0: #jeżeli różna liczba wierszy
        return "wynikiem jest zbiór pusty"
    
    x[0] = (b[0])/(L[0][0]) #pierwszy element obliczamy bezposrednio
    for k in range(1, m_L): #od 2 wiersza: obliczanie pomocniczej sumy
        for l in range(k): #do przedostatniej kolumny niezerowej w danym wierszu
            s += L[k][l] * x[l]
            #print(s, "kolumna", l, "wiersz", k)
        x[k] = (b[k] - s)/(L[k][k]) #takiego x-a obliczamy jaka jest następna kolumna po ostatniej skończonej
        s = 0
    return x
            
 
print ("wektor x =", Gayny_Paulina_UkladL(L1, b1))
print("wektor x =", Gayny_Paulina_UkladL(L2, b2))
print("wektor x =", Gayny_Paulina_UkladL(L1, b2))
print("wektor x =", Gayny_Paulina_UkladL(L2, b1))