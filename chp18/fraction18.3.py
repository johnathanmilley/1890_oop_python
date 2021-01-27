import copy

def sameRational(f1, f2):
    return f1.getNum()*f2.getDen() == f2.getNum() * f1.getDen()

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


myfraction = Fraction(3, 4)

yourfraction = copy.copy(myfraction)

print(myfraction == yourfraction)
print(myfraction)
print(yourfraction)