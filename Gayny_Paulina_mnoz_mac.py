# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 01:22:52 2021

@author: HP
"""

A=[[-1,-2,0],[-2,-4,6]]
B=[[1,2],[3,4],[5,7]]
D=[[-1,-2,0],[-2,-4,6],[0,4,5]]

def Gayny_Paulina_mnoz_mac(A,B):
    
    rowsA=len(A) #liczba wierszy macierzy A
    rowsB=len(B) #liczba wierszy macierzy B
    columnsA=len(A[0]) #liczba kolumn macierzy A
    columnsB=len(B[0]) #liczba kolumn macierzy B
    
    if columnsA!=rowsB: #mnożąc rozmiary muszą być takie że M1 mxn x M2 nxk = M mxk
        return "nie można wykonać mnożenia podanych macierzy"
    
    C=Gayny_Paulina_stworz_macierz(rowsA,columnsB) #stworzenie pustej macierzy o potrzebnym rozmiarze 
    
    x=0 #wiersz A
    x2=0 #wiersz B
    y=0 #kolumna A
    y2=0 #kolumna B
    
    for m in range (rowsA): #przechodzimy przez wszystkie wiersze m macierzy C
        for n in range(columnsB): #wszystkie kolumny n macierzy C dla ustalonego m wiersza C
            y2=n #przy przechodzeniu do następnej n kolumny C jestesmy w kolejnej, tej samej co kolumna C kolumnie B
            x=m #rozpatrywany w tym momencie wiersz A jest taki jak wiersz C
            while x < rowsA and y < columnsA and x2 < rowsB and y2 < columnsB:
                C[m][n]+=A[x][y]*B[x2][y2]
                y+=1 #następna kolumna A
                x2+=1 #następny wiersz B
    
            y=0 #resetujemy kolumnę dla A dla kolejnego elementu C
            x2=0 #resetujemy wiersz B dla kolejnego elementu C
            
    return C

def Gayny_Paulina_stworz_macierz(rows, columns): #stworzenie macierzy o potrzebnych wymiarach
    M = [] #deklaracja listy
    for x in range(rows): #bo od 0
        M.append([]) #na koniec listy dodaję element [] (następną listę) tyle razy ile ma być wierszy
        for y in range(columns):
            M[-1].append(0) #do ostatniego elementu listy (tego przed chwilą dodanego) czyli do listy [] dołączam zera - tyle ile jest kolumn
    return M

print('iloczyn macierzy',A,'i',B,'to:\n',Gayny_Paulina_mnoz_mac(A, B))

print('\niloczyn macierzy',A,'i',D,'to:\n',Gayny_Paulina_mnoz_mac(A, D))

print('\niloczyn macierzy',B,'i',D,'to:\n',Gayny_Paulina_mnoz_mac(B, D))

print('\niloczyn macierzy',D,'i',B,'to:\n',Gayny_Paulina_mnoz_mac(D, B))