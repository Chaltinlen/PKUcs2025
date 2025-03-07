from math import gcd
class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, other):
        n = self.numerator * other.denominator + self.denominator * other.numerator
        d = self.denominator * other.denominator
        g = gcd(n, d)
        return Fraction(n // g, d // g)
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

a, b, c, d = map(int, input().split())
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1 + f2)