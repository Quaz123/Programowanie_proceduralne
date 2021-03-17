class Telewizor:
    def __init__(self, kanal=1, glosnosc=1):
        self.kanal = kanal
        self.glosnosc = glosnosc

    def __str__(self):
        return f"Telewizor: numer kanalu: {self.kanal}, glosnosc: {self.glosnosc}"

    @property
    def kanal(self):
        return self._kanal

    @kanal.setter
    def kanal(self, value):
        if isinstance(value, int) and 1 <= value <= 120:
            self._kanal = value
        else:
            print("Ustawiono wartosc domyslna na 1")
            self._kanal = 1

    @property
    def glosnosc(self):
        return self._glosnosc

    @glosnosc.setter
    def glosnosc(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._glosnosc = value
        else:
            print("Ustawiono wartosc domyslna na 20")
            self._glosnosc = 20


tv1 = Telewizor(10, -10)
print(tv1)
