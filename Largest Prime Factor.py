'''
Title: Largest Prime Factor
Name: Ryan Persaud, Arjun Dhiman
Date: June 3, 2016
Description: Finds the largest prime factor of a number.
'''
#creating a class called factor
class Factor:

    #initializer function
    def __init__(self, product):

        #list of factors for the number given
        self.factorList = []
        #represents the current largest prime factor of the number given
        self.largest = 0
        #represents the number given by user
        self.product = product

    #Gets list of all Prime Factors
    def primeFactors(self):
        i = 2
        while i * i <= self.product:
            if self.product % i == 0:
                self.factorList.append(i)
                self.product /= i
            i += 1
        if self.product > 1:
            self.factorList.append(self.product)

    #returns largest prime factor
    def largestPrimeFactors(self):
        self.primeFactors()
        return int(max(self.factorList))
            
a = Factor(600851475143)
print(a.largestPrimeFactors())
