# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:28:24 2021

@author: HP
"""
import random
import math
import numpy

#całka z sinx od 0 do pi

#metoda chybił-trafił

def Gayny_Paulina_chybil_trafil(a, b, l_prob):
    n = 0
    k = 0 #liczba tafień
    while n < l_prob:
        x_i = random.uniform(a, b)
        y_i = random.uniform(0, 1)
        if math.sin(x_i) >= 0:
            if math.sin(x_i) >= y_i and y_i > 0:
                k = k + 1 #trafienie
           #else:
                #chybienie
        else:
            if math.sin(x_i) < y_i and y_i < 0:
                k = k - 1 #trafienie
            #else:
                #chybił
        n = n + 1
    calka = (k/l_prob)*(b - a)*(1-(0))
    return calka

#TESTY
print(Gayny_Paulina_chybil_trafil(0, math.pi, 10000))

#sprawdzę wartosc sredniej bezwzględnej roznicy między oczekiwaną wartoscią i tą otrzymaną, bo wydaje mi się to odpowiednie w tym przypadku
def test(ile_wywolan_calki, ile_prob_trafien):
    s_roznic = 0
    s_pomocnicza = 0
    for k in range(ile_wywolan_calki):
        wynik = Gayny_Paulina_chybil_trafil(0, math.pi, ile_prob_trafien)
        s_pomocnicza = s_pomocnicza + wynik
        s_roznic = s_roznic + abs(2 - wynik)
    srednia_roznica = s_roznic/ile_wywolan_calki
    sredni_wynik = s_pomocnicza/ile_wywolan_calki
    return srednia_roznica, sredni_wynik

l_wywolan = 100 #100 prób testowych wykonuję dla każdego przypadku
ile_prob_trafien = [10, 100, 1000, 10000, 50000]

ile_prob_trafien_i_roznice = numpy.zeros((len(ile_prob_trafien), 3))

for p in range(len(ile_prob_trafien)):
    ile_prob_trafien_i_roznice[p, 0] = ile_prob_trafien[p]
    sredn_rozn, sredn_wyn = test(l_wywolan, ile_prob_trafien[p])
    ile_prob_trafien_i_roznice[p, 1] = sredn_rozn
    ile_prob_trafien_i_roznice[p, 2] = sredn_wyn
    
#sortowanie po różnicach (kolumna 2 czyli 1)
ile_prob_trafien_i_roznic_sorted = ile_prob_trafien_i_roznice[ile_prob_trafien_i_roznice[:, 1].argsort()]
    

print("Srednia bezwzględna różnica między oczekiwaną (2) i otrzymaną wartoscia całki od 0 do pi z sinx w kolejnosci od najbardziej do najmniej dokładnych przypadków, liczba wywołań całki:", l_wywolan)
for l in range(len(ile_prob_trafien)):
    wyn = ile_prob_trafien_i_roznic_sorted[l, 2]
    rozn = ile_prob_trafien_i_roznic_sorted[l, 1]
    ile_prob_traf = ile_prob_trafien_i_roznic_sorted[l, 0]
    print("Średni wynik:", wyn, "Różnica przy", ile_prob_traf, "próbach trafień:", rozn)


