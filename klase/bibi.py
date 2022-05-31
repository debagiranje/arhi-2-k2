"""
Направити класу Ауто чији објекти имају као атрибуте: ид, марка, стање у резервоару, капацитет резервоара, потрошња (л/км) и број пређених километара.
Потребно је направити методе:

predji - за аргумент узима број километара, а враћа тачно ако ауто може да пређе те километре, у супротном нетачно. Такође, метода треба да смањи стање у резервоару за одређени број.

naspi - за аргумент узима број литара које ће се наточити у резервоар. Враћа тачно ако је пуњење могуће, у супротном враћа нетачно. Такође, метода треба да повећа стање резервоара аутомобила над којим је метода позвана.

Потребно је преклопити оператор __nonzero__ и __str__. Оператор __nonzero__ треба да врати тачно ако је ауто прешло мање од 300 000 km, у супротном враћа нетачно. Оператор __str__ враћа све информације о неком аутомобилу.
Потребно је направити статичку методу која као аргумент узима листу аута, а враћа ауто које је прешло најмање километара.
"""


class Auto():
    def __init__(self, ID, marka, r_stanje, r_kapacitet, potrosnja, predjeno):
        self.ID = ID
        self.marka = marka
        self.r_stanje = r_stanje
        self.r_kapacitet = r_kapacitet
        self.potrosnja = potrosnja
        self.predjeno = predjeno
    
    def predji(self, km):
        litre = km * self.potrosnja

        if self.r_stanje < litre:
            return False
        else:
            self.r_stanje -= litre

            return True

    def naspi(self, gorivo):
        if self.r_stanje + gorivo > self.r_kapacitet:
            return False
        else:
            self.r_stanje += gorivo
            return True
    
    def __nonzero__(self):
        if self.predjeno < 300000:
            return True
        
        return False

    def __str__(self):
        return f"automobil ID {self.ID}, marke {self.marka}, ima kapacitet rezervoara {self.r_kapacitet}l, a trenutno stanje mu je {self.r_stanje}l. \n Bibi je presao {self.predjeno}km, i trosi {self.potrosnja} l/km."

    @staticmethod
    def najmanji(bibi):
        naj = bibi[0].predjeno
        for bibi in lista:
            if bibi.predjeno < naj:
                naj = bibi.predjeno
                id = bibi.ID
        
        rez = "\n najmanje je presao bibi ID: " + str(id) + " ukupno km: " + str(naj)

        return rez

    
if __name__ == "__main__":

    b1 = Auto(1, "audi", 10, 30, 2, 35000)
    b2 = Auto(2, "bmw", 20, 30, 5, 8)
    b3 = Auto(3, "mechkitza", 20, 30, 5, 350000)
    b4 = Auto(4, "golfitsch", 50, 60, 1, 350)

    lista = []

    lista.append(b1)
    lista.append(b2)
    lista.append(b3)
    lista.append(b4)      

    for svaki in lista:
        print(svaki)
        print("\n")

    print(Auto.najmanji(lista))

    print(b2.__nonzero__())
    print(b3.__nonzero__())

    print(b4.naspi(20))
    print(b4.r_stanje)
    print(b4.naspi(5))
    print(b4.r_stanje)


    print(b4.predji(60))
    print(b4.r_stanje)
    print(b4.predji(5))
    print(b4.r_stanje)
