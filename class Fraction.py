# Name: Steven Marco Navarrette
# Date: 1/23/2024
# Description: Class code of fractions with numerators and denominators as attributes

# creation of class
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    # getter
    @property
    def num(self):
        return self._num
    # setter

    @num.setter
    def num(self, value):
        self._num = value
    # getter

    @property
    def den(self):
        return self._den
    # setter
    
    @den.setter
    def den(self, value):
        if value != 0:
            self._den = value

    # Function to return fraction as a float type
    def getreal(self):
        return float(self.num) / self.den

    # string method to format how the fractions print out
    def __str__(self):
        return "Your fractions are: " + str(self.num) + "/" + str(self.den)

    # A function I had to create to fix the print statement
    def __repr__(self):
        return "<__main__.Fraction: Your fraction is -> " + str(self.num) + "/" + str(self.den)


# Main code
fractions = []
n = int(input("How many fractions do you want to add to your list: "))
for i in range(n):
    num = (input("Enter a numerator: "))
    den = (input("Enter the denominator for this fraction: "))
    frac = Fraction(num, den)
    fractions.append(frac)
print(fractions)
