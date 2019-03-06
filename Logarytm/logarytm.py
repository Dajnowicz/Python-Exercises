import math

class ZlaPodstawa(Exception):
    def __str__(self):
        return "Zla Podstawa"

class ZlyArgument(Exception):
    def __str__(self):
        return "Zly Argument"

class RoznePodstawy(Exception):
    def __str__(self):
        return "Rozne Podstawy"


class Logarytm:
    def __init__(self, podstawa, argument, ):

        if podstawa == 1 or podstawa <=0:
            raise ZlaPodstawa()
        self.podstawa = podstawa

        if argument <=0:
            raise ZlyArgument()
        self.argument = argument

    def __add__(self,other):
        if self.podstawa == other.podstawa:
            return Logarytm(self.podstawa, self.argument*other.argument)
        else:
            raise RoznePodstawy()

    def __str__(self):
        s = "log" + str(self.podstawa) + "(" + str(self.argument) + ")"
        return s

    def redukuj(self):
        print ("do zrobienia")

    def oblicz(self):
        o = math.log(self.argument,self.podstawa)
        return o


