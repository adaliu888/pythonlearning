class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
