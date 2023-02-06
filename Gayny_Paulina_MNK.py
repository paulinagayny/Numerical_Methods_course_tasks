# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:21:27 2021

@author: HP
"""
import numpy
import math

#moja implementacja rozwiązywania układu dolnego trójkątnego
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

#moja implementacja rozkładu Cholesky'ego
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

#CEL 1
#funkcja do aproksymacji sredniokwadratowej metodą najmniejszych kwadratów
#wielomianem o dowolnym, zadanym stopniu n
#x, y to wartosci punktów,
#n to stopień szukanego wielomianu,
#Funkcja ma zwracać współczynniki wielomianu aproksymacyjnego: a = [a0, a1,···, an]
def Gayny_Paulina_MNK(x, y, n):
    if len(x) != len(y) or n <= 0:
        return "Wprowadzono błędne dane"
    #należy zbudować macierz A i stworzyć układ równań normalnych
    A = numpy.zeros([len(x), n + 1])
    #budowanie macierzy A
    for k in range(n + 1): #która potęga xi (kolumna)
        for l in range(len(x)): #który xi w danej potędze (wiersz)
            A[l][k] = math.pow(x[l], k)
    A_T = numpy.transpose(A)
    A_finale = A_T.dot(A) #macierz współczynników układu
    #stworzenie układu równań normalnych A_T*A*a = A_T*y
    b = A_T.dot(y)
    #następnie wystarczy rozwiązać układ - ponieważ macierz współczynników układu jest symetryczna i okreslona dodatnio
    #używamy metody Cholesky'ego
    A_L = Gayny_Paulina_rozklad_cholesky(A_finale)
    A_U = A_L.transpose()
    a = numpy.zeros([len(A_T), 1])
    #y_pom = A_U.dot(a)
    y_pom = Gayny_Paulina_UkladL(A_L, b)
    a = Gayny_Paulina_ukladU(A_U, y_pom)
    return a

#sprawdzam poprawnosc - przyklad z ćwiczeń zad.2
x = [-1, 2, 5]
y = [5, -4, -13]
n = 1
print(Gayny_Paulina_MNK(x, y, n))
#sprawdzam poprawnosc - przyklad z ćwiczeń zad.3
x = [-1, 0, 1, 2]
y = [4, -1, 0, 7]
n = 2
print(Gayny_Paulina_MNK(x, y, n))