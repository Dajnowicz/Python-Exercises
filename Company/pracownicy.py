import re
from datetime import date


class Osoba:
    def __init__(self, lista=[]):
        if lista.__len__() != 5:
            raise ValueError()

        self.imie = lista[0]
        self.nazwisko = lista[1]

        for x in range(2, 5):
            if "-" in str(lista[x]):
                self.telefon = lista[x]
                break;
        for x in range(2, 5):
            if (len(str(lista[x])) == 11 and "-" not in str(lista[x])):
                self.pesel = lista[x]
                break;
        for x in range(2, 5):
            if ("-" not in str(lista[x]) and int(lista[x]) < 100):
                self.wiek = lista[x]
                self.skorygujWiek()
                break;

    def skorygujWiek(self):

        today = date.today()

        rocznik = int(self.pesel[0:2])
        if (rocznik < 100 and rocznik > 20):
            rokUrodzenia = rocznik + 1900
        else:
            rokUrodzenia = rocznik + 2000
        if ((today.year - rokUrodzenia) == int(self.wiek)):
            self.wiek = self.wiek;
        else:
            self.wiek = (today.year - rokUrodzenia);

        # 970323
        # for per in lista:
        #     if re.match(r'[0-9]{1}', str(per)):
        #         self.wiek = per
        #     if re.match(r'[0-9]{11}', str(per)):
        #         self.pesel = per
        #     if re.match(r'[0-9]-[0-9]-[0-9]', str(per)):
        #         self.telefon = per
        # if any(re.match(r'[0-9]{1}') for line in lista)
        #     pasuje

        # regex = re.compile(r'[0-9]{1}')
        # self.wiek = list(filter(regex.match, lista))
        # regex = re.compile(r'[0-9]{11}')
        # self.pesel = list(filter(regex.match, lista))
        # regex = re.compile(r'[0-9]{1}')
        # self.telefon = list(filter(regex.match, lista))

        # for item in lista:
        #     for r in item:
        #         match = re.search(r'[0-9]{1}', r)
        #         if match:
        #             self.wiek = match.group(1)
        #         match = re.search(r'[0-9]{11}', r)
        #         if match:
        #             self.pesel = match.group(1)
        #         match = re.search(r'[0-9]-[0-9]-[0-9]', r)
        #         if match:
        #             self.telefon = match.group(1)

    def __str__(self):
        s = ""
        s += "Imie: " + str(self.imie) + "\n" + "Nazwisko: " + str(self.nazwisko) + "\n" + "Wiek: " + str(
            self.wiek) + "\n" + "Pesel: " + str(self.pesel) + "\n" + "Telefon: " + str(self.telefon) + '\n';
        return s;