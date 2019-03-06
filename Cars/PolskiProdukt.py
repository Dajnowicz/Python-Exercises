class PolskiProdukt:

    def __init__(self, wojewodztwo, miasto, firma):
        self.wojewodztwo = wojewodztwo
        self.miasto = miasto
        self.firma = firma

    def __str__(self):
        s = "Jestem z Polski" + "\n"
        s += "wojewodztwo = " + self.wojewodztwo


        return s