# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:48:33 2021

@author: HP
"""

M1 = [[1,1,1],
      [1,2,1],
      [3,0,4]]

M2 = [[-2,4,3,5],
      [1,-1,7,1],
      [3,0,-3,1],
      [1,1,0,2]]

M3 = [[2,3,2],
      [4,6,3],
      [-2,-1,2]] #przykład z wykładu

b1 = [2,1,-1]

b2 = [1,3,2,0]

b3 = [4, 1, -2] #przykład z wykładu

# A*x = b, A to macierz współczynników układu równań, b - wektor wyrazów wolnych
# algorytm elimincacji gaussa z częsciowym wyborem elementu podstawowego
# szczerze mówiąc to wygląda to jakby liczyło się mniej dokładnie mimo wyboru elementu maksymalnego i dzielenia przez niego
def Gayny_Paulina_gauss_pivot(A, b):
    R = A
    n_M = len(A) #wiersze
    if n_M != len(b) or len(b) == 0 or n_M == 0 or len(A[0]) == 0: #jeżeli różna liczba wierszy
        return "wynikiem jest zbiór pusty"
    for i in range(n_M - 1):
        #częsciowy wybor elementu podstawowego - każda kombinacja wierszy
        maks = i #indeks wiersza elementu maksymalnego w danej kolumnie diagonali
        for t in range(i, n_M):
            #czesc szukajaca elementu maksymalnego
            if R[t][i] != 0 and R[t][i] > R[maks][i]:
                maks = t
            for g in range(i + 1, n_M):
                #częsc sprawdzajaca czy nie ma zera
                if R[i][i] == 0:
                    Gayny_Paulina_zamiana_wierszy(t, g, R)
                    temp = b[t]
                    b[t] = b[g]
                    b[g] = temp
        Gayny_Paulina_zamiana_wierszy(maks, i, R)
        temp = b[maks]
        b[maks] = b[i]
        b[i] = temp
        if R[i][i] == 0:
            i = i + 1 #pomijamy ten wiersz wtedy
        for j in range(i + 1, n_M):
            m = (R[j][i])/(R[i][i])
            b[j] = b[j] - m*b[i]
            for k in range(i, n_M):
                R[j][k] = R[j][k] - m*R[i][k]          
    return Gayny_Paulina_ukladU(R, b) #bo doprowadzilismy do postaci gornej trójkątnej

def Gayny_Paulina_zamiana_wierszy(w1, w2, M):
    k_M = len(M[0])
    for k in range(k_M): #dla wszystkich kolumn w podanych wierszach
        temp = M[w1][k]
        M[w1][k] = M[w2][k]
        M[w2][k] = temp
    return M

def Gayny_Paulina_ukladU(U, b):
    x = b #wymiarowo takie same
    m_U = len(U) #liczba wierszy macierzy U
    n_U = len(U[0]) #liczba kolumn macierzy U
    s = 0 #pomocnicza suma
    
    if m_U != len(b) or len(b) == 0 or m_U == 0 or n_U == 0: #jeżeli różna liczba wierszy
        return "wynikiem jest zbiór pusty"
    
    x[len(x) - 1] = (b[len(x) - 1])/(U[m_U - 1][n_U - 1]) #pierwszy element obliczamy bezposrednio
    if len(x) == 1:
        return x
    
    k = m_U - 2
    l = n_U - 1
    while (k >= 0): #od przedostaniego wiersza do pierwszego: obliczanie pomocniczej sumy
        while (l > k): #od ostatniej kolumny w wierszu do przedostatniej niezerowej w danym wierszu
            s += U[k][l] * x[l]
            #print(s, "kolumna", l, "wiersz", k)
            l = l - 1
        x[k] = (b[k] - s)/(U[k][k]) #takiego x-a obliczamy jaka jest następna kolumna po ostatniej skończonej
        #print(s)
        s = 0
        k = k - 1
        l = n_U - 1 #przywracamy
    return x

print ("wektor x =", Gayny_Paulina_gauss_pivot(M1, b1))
print("wektor x =", Gayny_Paulina_gauss_pivot(M2, b2))
print("wektor x =", Gayny_Paulina_gauss_pivot(M1, b2))
print("wektor x =", Gayny_Paulina_gauss_pivot(M2, b1))
print("wektor x =", Gayny_Paulina_gauss_pivot(M3, b3))    #przykład z wykładu