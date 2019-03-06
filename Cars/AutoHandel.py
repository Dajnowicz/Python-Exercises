import Samochod


class AutoHandel:
    listaSamochodow = []

    def dodajSamochod(self, samochod):
        self.listaSamochodow.append(samochod)

    def usunSamochod(self, samochod):
        self.listaSamochodow.remove(samochod)

    def __str__(self):
        return "Autohandel ma samochody:" + Samochod

    def wypiszAH(self):
        for val in self.listaSamochodow:
            print(val)


samochod1 = Samochod.Samochod('fiat', 1999, 5)
samochod2 = Samochod.Samochod('ford', 2000, 3, 333333, 'niebieski')
samochod3 = Samochod.Maluch('passat',2001,23,1000,'czerowny')
porsche = Samochod.Porsche('porsche', 2012, 3, 30000, 'czerwone', 3.2)

ah = AutoHandel()

ah.dodajSamochod(samochod1)
ah.dodajSamochod(samochod2)
ah.dodajSamochod(samochod3)
ah.dodajSamochod(porsche)

ah.wypiszAH()

print("------------------------\n")

ah.usunSamochod(samochod1)

ah.wypiszAH()