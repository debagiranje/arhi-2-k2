"""
Направити класу KvadratniPolinom чији објекти као атрибут имају lista_koeficijenata. Потребно је направити сљедеће методе објекта:

dodaj_koeficijent(k, s) - метода увећава коефицијент испред xs за k. 		
obrisi_koeficijent(s) - метода брише коефицијент испред xs.				
korijeni() - метода враћа рјешење квадратне једначине.				    

Преклопити оператор __add__ (или направити методу plus(p1, p2) која сабира два квадратна полинома и враћа нови полином настао из сабирања).			   	        

Направити бар десет објеката класе KvadratniPolinom и смјестити их у листу, а потом све полиноме из листе сабрати и наћи коријен новонасталог полинома.			
На примјер, за квадратни полином   имамо да је lista_koeficijenata =[2,0,6].

"""

import math
from functools import reduce

class KvadratniPolinom():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.lista_koeficijenata = [a, b, c]

    def __str__(self):
        return f"{self.lista_koeficijenata}"

    
    def dodaj_koeficijent(self, k, s):
        self.lista_koeficijenata = self.lista_koeficijenata[::-1]

        self.lista_koeficijenata[s] += k

        return self.lista_koeficijenata[::-1]

    def obrisi_koeficijent(self, s):
        self.lista_koeficijenata = self.lista_koeficijenata[::-1]

        self.lista_koeficijenata[s] = 0
        return self.lista_koeficijenata
    
    def korijeni(self):
        D = self.b**2 -4*self.a*self.c
        
        if D < 0:
            return False
        elif D == 0:
            x =  (-(self.b)+math.sqrt(D))/(2*self.a)
            xs = "ima jedan korijen: " + str(x)

            return xs
        else:
            x1 = (-(self.b)+math.sqrt(D))/(2*self.a)
            x2 = (-(self.b)-math.sqrt(D))/(2*self.a)

            xs = "rjesenja su: x1 = " + x1 + " , x2 = " + x2
            
            return xs

    def __add__(self, other):
        self.a += other.a 
        self.b += other.b 
        self.c += other.c

        self.lista_koeficijenata = [self.a, self.b, self.c]

        return self.lista_koeficijenata


p1 = KvadratniPolinom(2,0,6)
p2 = KvadratniPolinom(3,0,6)
p3 = KvadratniPolinom(3,0,-9)
p4 = KvadratniPolinom(6,2,5)
p5 = KvadratniPolinom(0,4,1)
p6 = KvadratniPolinom(5,6,2)
p7 = KvadratniPolinom(0,0,0)
p8 = KvadratniPolinom(-5,4,-3)
p9 = KvadratniPolinom(1,1,1)
p10 = KvadratniPolinom(3,2,1)


novi = []
lista =  [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

print(p1.dodaj_koeficijent(2, 1))



    

print(novi)




        
    
