class Fraction:

    def __init__(self, top, bottom):
        self.num = top          # the numerator is on top
        self.den = bottom       # the denominator is on bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
 
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


f1 = Fraction(2, 3)
print(f1)

f1.num = 5
print(f1)