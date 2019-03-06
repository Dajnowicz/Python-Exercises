from PolskiProdukt import PolskiProdukt;


class Samochod:
    def __init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg="", kolor=""):
        self.marka = marka
        self.rokProdukcji = rokProdukcji
        self.przebieg = przebieg
        self.kolor = kolor
        self.liczbaDrzwi = liczbaDrzwi

    def __str__(self):
        s = "Marka = " + self.marka + "\n"
        s += "Rok produkcji = " + str(self.rokProdukcji) + "\n"
        s += "Przebieg = " + str(self.przebieg) + "\n"
        s += "kolor = " + str(self.kolor) + "\n"
        s += "Liczba drzwi = " + str(self.liczbaDrzwi) + "\n"

        return s


class Maluch(Samochod, PolskiProdukt):
    czyJezdzi = True

    def __init__(self, marka, rokProdukcji, glosnosc, przebieg, kolor):
        Samochod.__init__(self, marka, rokProdukcji, 2, przebieg, kolor)
        self.glosnosc = glosnosc

    def __str__(self):
        s = Samochod.__str__(self)
        s += "Glosnosc = " + str(self.glosnosc) + 'DB' + "\n"
        s += "czy jezdzi = " + str(self.czyJezdzi) + "\n"

        return s


class Porsche(Samochod):
    def __init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg, kolor, ileDoSetki):
        Samochod.__init__(self, marka, rokProdukcji, liczbaDrzwi, przebieg, kolor)
        self.ileDoSetki = ileDoSetki

    def __str__(self):
        s = Samochod.__str__(self) + "\n"
        s += "Ile do setki: " + str(self.ileDoSetki) + "s"

        return s