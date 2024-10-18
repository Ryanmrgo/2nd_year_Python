class Fraction:

    def __init__(self, num=0, den=1):
        self.numerator = num
        self.denominator = den

    def setFraction(self, num, den):
        self.numerator = num
        self.denominator = den

    def getFraction(self):
        tempfraction = Fraction(self.numerator, self.denominator)
        return tempfraction
    
    def getDenominator(self):
        return self.denominator
    
    def getNumerator(self):
        return self.numerator

    def __str__(self):  
        return str(self.numerator) + '/' + str(self.denominator)

    def convert(self):
        return self.numerator / self.denominator

    def addFraction(self, fraction):
        ''' Adding two fractions '''
        common_denominator = self.denominator * fraction.denominator
        new_numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        return Fraction(new_numerator, common_denominator)

    def subFraction(self, fraction):
        ''' Subtracting two fractions '''
        common_denominator = self.denominator * fraction.denominator
        new_numerator = self.numerator * fraction.denominator - fraction.numerator * self.denominator
        return Fraction(new_numerator, common_denominator)

    def compareFraction(self, fraction):
        ''' Comparing two fractions '''
        self_value = self.numerator / self.denominator
        fraction_value = fraction.numerator / fraction.denominator
        if self_value > fraction_value:
            return f"{self} is greater than {fraction}"
        elif self_value < fraction_value:
            return f"{self} is less than {fraction}"
        else:
            return f"{self} is equal to {fraction}"



if __name__ == "__main__":
    
    F1 = Fraction(10, 2)
    F2 = Fraction()
    F2.setFraction(20, 4)
    F3 = F1.addFraction(F2)
    print('Sum of two fractions:', F3)
    print('Sum of two fractions in number format:', F3.convert())

    """"""""""""""""""""""""""""""""""""""""""
    F4 = Fraction(5, 2)
    F5 = Fraction(3, 4)
    F6 = F4.subFraction(F5)
    print('Subtraction of two fractions:', F6)
    print('Subtraction of two fractions in number format:', F6.convert())

    """"""""""""""""""""""""""""""""""""""""""
    F7 = Fraction(3, 4)
    F8 = Fraction(1, 2)
    print(F7.compareFraction(F8))
