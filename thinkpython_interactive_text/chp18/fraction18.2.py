# helper function: A helper function is a function that performs part of the computation of another function.
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

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

    # mutator method (changes the internal state of the object)
    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common


myfraction = Fraction(12, 16)
print(myfraction)

myfraction.simplify()
print(myfraction)