"""
1.	Napraviti klasu Krug i u njoj definisati sljedeće:
a)	Atribut klase “omotač” koji predstavlja poluprečnik kruga u tački (0,0) koji pokriva sve kreirane objekte klase Krug.
b)	Konstruktor koji za argumente uzima poluprečnik_kruga, apscisa_x, ordinata_y. U konstruktoru realizovati da “omotač” ispunjava definiciju pod a).
c)	Preklopiti (predefinisati) operator __str__.
d)	Metodu koja računa površinu kruga.
e)	Napraviti classmetod-u koja računa površinu omotača.
f)	Napraviti staticmethod koja računa udaljenost između dva kruga, a vraća 0 ako se krugovi sijeku ili dodiruju.


"""
import math

class Krug():

    omotac = 0

    def __init__(self, pp, x, y):
        self.pp = pp
        self.x = x
        self.y = y
        if Krug.omotac < math.sqrt(abs(self.x + self.y)) + self.pp:
            Krug.omotac = math.sqrt(abs(self.x + self.y)) + self.pp

    def __str__(self):
        return f"krug poluprecnika: {self.pp}, ima centar u x = {self.x}, y = {self.y}"
    
    def povrsina(self):
        return self.pp**2 * math.pi
    
    @classmethod
    def povrsina_omotac(klasa):
        return klasa.omotac**2 * math.pi
    
    @staticmethod
    def udaljenost(prvi,drugi):
        ud = math.sqrt((drugi.x-prvi.x)**2 + (drugi.y-prvi.y)**2) - (prvi.pp + drugi.pp)

        if ud > 0:
            return ud
        
        return 0


lista = []

k1 = Krug(1, 2, 2)
lista.append(k1.omotac)
print(k1.omotac)
k2 = Krug(4, -1, -2)
lista.append(k2.omotac)
print(k2.omotac)
k3 = Krug(2, -1, -1)
print(k3.omotac)
lista.append(k3.omotac)

k4 = Krug(1, 2, 5)
print(k4.omotac)

k5 = Krug(10, 5, 6)
print(k5.omotac)

k6 = Krug(1,1,1)
print(k5.omotac)

"""
print(k1.__str__())
print(k2.__str__())

print("-"*30)

print(Krug.udaljenost(k1,k4))
print(Krug.udaljenost(k1,k2))

print("-"*30)

print(max(lista)) # pp kruga koji pokriva sve krugove (od omotaca koji su u listi)

print("-"*30)
print(Krug.omotac) 
print(Krug.povrsina_omotac()) # odstampa povsinu omotaca posljednjeinstanciranog objekta (k4)

"""

