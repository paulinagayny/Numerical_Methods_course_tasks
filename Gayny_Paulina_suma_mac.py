# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 01:17:30 2021

@author: HP
"""

A=[[1,2],[3,4],[5,7]]
B=[[-1,-2],[-2,-4],[-4,-6]]
E=[[1,4,-2],[7,0,-3]]
F=[[-2,-3,2],[-5,3,3]]

def Gayny_Paulina_suma_mac(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        return "nie można dodać podanych macierzy"
    rows=len(A)
    columns=len(A[0])
    C=A #można dodawać tylko macierze o tym samym rozmiarze więc to nie przeszkadza.
    for x in range (len(A)):
        for y in range(len(A[0])):
            C[x][y]=A[x][y]+B[x][y]
    return C
            
print('suma macierzy',A,'i',B,'to:\n',Gayny_Paulina_suma_mac(A, B))

print('\nsuma macierzy',A,'i',E,'to:\n',Gayny_Paulina_suma_mac(A, E))

print('\nsuma macierzy',E,'i',F,'to:\n',Gayny_Paulina_suma_mac(E, F))