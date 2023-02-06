# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:10:54 2021

@author: HP
"""
from matplotlib.pyplot import *
import numpy as np

#bisekcja - równy podział
#znajdowanie miejsca zerowego

#zał: 1. funkcja ciągła na przedziale [a, b] 
#2. w przedziale [a, b] musi znajdować się dokładnie jedno miejsce zerowe
# f(a)*f(b)<0 => funkcja zmienia znak w przedziale [a, b] (korzystamy z tw Darboux)

def funkcja_1(x):
    return x**2 + 2*x -3

x = np.linspace(-5, 5, 10000)
y = x**2 + 2*x -3
plot(x,y)
xlabel("x axis")
ylabel("y axis")
show()

def funkcja_2(x):
    return -3/x + 1

x = np.linspace(0.5, 5, 10000)
y = -3/x + 1
plot(x,y)
xlabel("x axis")
ylabel("y axis")
show()

def Gayny_Paulina_bisekcja(a, b, eps):
    if b - a < 0 or funkcja_2(a)*funkcja_2(b) > 0:
        return "Nieprawidłowo podany przedział"
    
    if b - a < eps: #rozwiązanie
        return (a + b)/2
    
    c = (a + b)/2
    if funkcja_2(c) == 0: #rozwiązanie
        return c
    if funkcja_2(a)*funkcja_2(c) < 0:
        return Gayny_Paulina_bisekcja(a, c, eps)
    else:
        return Gayny_Paulina_bisekcja(c, b, eps)
    
#zał: f.ciągła, różniczkowalna na przedziale [a, b]
#f. musi mieć w tym przedziale dokładnie jedno miejsce zerowe
#f. nie może mieć ekstremum w tym przedziale
#druga pochodna nie może zmienić znaku (w tym przedziale)
#f(x0)*f''(x0)>0
def Gayny_Paulina_styczne(x, b, eps):
    if b - x < 0 or funkcja_2(x)*funkcja_2(b) > 0:
        return "Nieprawidłowo podany przedział"
    
    if funkcja_2(x) == 0:
        return x
    if b - x < eps:
        return x
    
    while(abs(b - x) > eps and abs(funkcja_2(x)) > eps):
        x_next = x - funkcja_2(x)/(2*x + 2)
        x = x_next
    
    if abs(funkcja_2(x)) < eps or abs(b - x) < eps:
        return x
    
    
#x1 i x2 to x0 i x1 w wykładzie
def Gayny_Paulina_sieczne(x1, x2, eps):

    if funkcja_1(x1)*funkcja_1(x2) > 0:
        return "Nieprawidłowo podany przedział"
    
    while(abs(x1 - x2) > eps and abs(funkcja_1(x2)) > eps):
        x_next = x2 - ((x2 - x1)/(funkcja_1(x2) - funkcja_1(x1)))*funkcja_1(x2)
        x1 = x2
        x2 = x_next
    
    if abs(x1 - x2) < eps:
        return x2
    if abs(funkcja_1(x2)) < eps:
        return x2

#TESTOWANIE
x = Gayny_Paulina_bisekcja(1, 20, 0.01)
print("Miejsce zerowe dla f2 w", x)
x = Gayny_Paulina_styczne(1, 10, 0.01)
print("Miejsce zerowe dla f2 w", x)
x = Gayny_Paulina_sieczne(-5, 0, 0.01)
print("Miejsce zerowe dla f1 w", x)

x = Gayny_Paulina_bisekcja(2, 200, 0.01)
print("Miejsce zerowe dla f2 w", x)
x = Gayny_Paulina_styczne(1.5, 4, 0.01)
print("Miejsce zerowe dla f2 w", x)
x = Gayny_Paulina_sieczne(-6, -1, 0.01)
print("Miejsce zerowe dla f1 w", x)