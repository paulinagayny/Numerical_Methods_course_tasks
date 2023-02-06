# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:42:00 2021

@author: HP
"""
import numpy

#funkcja do algorytmu interpolacji wielomianowej Lagrange'a
#x - wektor wartosci, dla których chcemy wyliczyć wartosci wielomianu interpolacyjnego
#xw, yw - węzły interpolacyjne (dane)
#n - stopień wielomianu

#nie wiem dlaczego musimy podawać jako argument n, nie widzę w tym sensu - wystarczy xw/yw
def Gayny_Paulina_Lagrange(x, xw, yw, n):
    if len(xw) != len(yw):
        return "Wprowadzono niewłasciwe węzły interpolacyjne"
    if n != len(xw) - 1: #stopień wielomianu (n) powinien być równy liczbie niewiadomych - 1. Jesli n jest mniejsze - interpolacja danymi węzłami jest źle okreslona, bo nie wykorzystamy wszystkich. Jesli n jest wieksze - nie mamy węzłów (danych) do stworzenia takiego wielomianu. Nie ma to sensu
        print("Nie ma potrzeby używać wielomianu tego stopnia. Użyto wielomianu stopnia", len(x))

    P = numpy.zeros(len(xw))
    y = numpy.zeros(len(x)) #wektor obliczonych wartosci wielomianow Lagrange'a - nasza odpowiedź
    s = 0 #pomocnicza suma
    
    #znajdowanie wielomianu Lagrange'a
    for k in range(len(x)): #x którego obliczamy (nie ma nic wspólnego z samą interpolacją)
        s = 0 #czyszczenie
    
        #własciwa częsć poswięcona interpolacji wielomianowej Lagrange'a
        for i in range(len(xw)): #sumowanie wszystkich pi*yi dla danego x-a
            P[i] = 1 #żeby się nie wyzerowało
            for j in range(len(xw)): #wyliczanie kolejnych pi
                if i != j:
                    P[i] = P[i] * ((x[k] - xw[j])/(xw[i] - xw[j]))
            #po otrzymaniu kolejnego pi
            s = s + P[i] * yw[i]
        #gdy już mamy całą sumę (mamy wartosc wielomianu Lagrange'a dla wejsciowego x)
        y[k] = s
    return y

#przykład z wykładu (powinien wyjsc L(x) = 3 - 1/3 x + 1/3 x^2)
xw = [-2, 1, 4]
yw = [5, 3, 7]
n = len(xw) - 1
x = [1, 0, -1, 3]
print(Gayny_Paulina_Lagrange(x, xw, yw, n))
        
xw = [-1, 1, 3]
yw = [3, -2, 1]
n = len(xw) - 1
x = [1, 4, 0, 10]
print(Gayny_Paulina_Lagrange(x, xw, yw, n))