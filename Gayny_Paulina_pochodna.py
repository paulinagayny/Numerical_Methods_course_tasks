# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:13:30 2021

@author: HP
"""

import math
import numpy as np

h = 1
wynik = ["krok","iloraz","h","pochodna"]

kroki = 30

for k in range(60): #30 kroków
    iloraz=(math.exp(10+h) - math.exp(10))/h
    zapis = [k, iloraz, h, math.exp(10)]
    wynik = np.vstack([wynik, zapis])
    h = h/2
    
print(wynik)