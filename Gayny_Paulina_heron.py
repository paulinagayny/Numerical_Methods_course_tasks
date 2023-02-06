# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:27:57 2021

@author: HP
"""

def Gayny_Paulina_heron(a, x, eps): #pierw. kw. z liczby a, x to wartosć startowa, epsilon do warunku przerwania
    if a <= 0:
       return "nie istnieje rzeczywisty pierwiastek z danej liczby"  
    blad = eps + 1 #żeby wejsć do pętli.
    while blad > eps:
        x_next = (1/2)*(x + a/x)
        blad = abs(x_next - x)
        #print(x_next)
        x = x_next
    return x_next

epsilon = 0.0001
x0 = 2 #oczywiscie lepiej by było jakbym wzięła jak najbliższą liczbę do a, ale tak też się policzy, tylko trochę dłużej - wydaje mi się że to nie przeszkadza
liczby = [3, 100, 1000, 6.234532E13, -9]

for k in range(len(liczby)):
    print("Pierwiastek kwadratowy z", liczby[k], " to (z dokładnoscią do", epsilon, ")\n", Gayny_Paulina_heron(liczby[k], x0, epsilon))

#nie jestem tak do konca pewna czy błąd bezwględny między dwoma kolejnymi obliczanymi wartosciami to to samo co dokladnosc wyniku, ale głupio mi pisać że "pierwiastek to" skoro to nie jest dokładnie to.