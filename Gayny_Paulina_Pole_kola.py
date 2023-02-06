# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:01:51 2021

@author: HP
"""

#policzenie powierzchni koła o promieniu r metodą chybił - trafił

import random
import math
import numpy

def Gayny_Paulina_Pole_kola(r, l_prob): #liczę na ćwiartce koła
    n = 0
    k = 0 #liczba tafień
    while n < l_prob:
        x_i = random.uniform(0, r)
        y_i = random.uniform(0, r)
        if math.sqrt(r * r - x_i * x_i) >= 0:
            if math.sqrt(r * r - x_i * x_i) >= y_i and y_i > 0:
                k = k + 1 #trafienie
           #else:
                #chybienie
        else:
            if math.sqrt(r * r - x_i * x_i) < y_i and y_i < 0:
                k = k - 1 #trafienie
            #else:
                #chybił
        n = n + 1
    calka = 4 * (k/l_prob)*(r)*(r)
    return calka

#TESTY
print("Prosty test, pole koła o promieniu 1:", Gayny_Paulina_Pole_kola(1, 10000))

#sprawdzę wartosc sredniej bezwzględnej roznicy między oczekiwaną wartoscią i tą otrzymaną, bo wydaje mi się to odpowiednie w tym przypadku
def test(ile_wywolan_calki, ile_prob_trafien):
    s_roznic = 0
    s_pomocnicza = 0
    for k in range(ile_wywolan_calki):
        wynik = Gayny_Paulina_Pole_kola(5, ile_prob_trafien)
        s_pomocnicza = s_pomocnicza + wynik
        s_roznic = s_roznic + abs(25 * 3.14 - wynik)
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
    

print("Srednia bezwzględna różnica między oczekiwaną (78,5) i otrzymaną wartoscia pola koła o promieniu 5 w kolejnosci od najbardziej do najmniej dokładnych przypadków, liczba wywołań całki:", l_wywolan)
for l in range(len(ile_prob_trafien)):
    wyn = ile_prob_trafien_i_roznic_sorted[l, 2]
    rozn = ile_prob_trafien_i_roznic_sorted[l, 1]
    ile_prob_traf = ile_prob_trafien_i_roznic_sorted[l, 0]
    print("Średni wynik:",wyn, "; Różnica przy", ile_prob_traf, "próbach trafień:", rozn)


