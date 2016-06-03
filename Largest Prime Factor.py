<<<<<<< Updated upstream
=======
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

<<<<<<< Updated upstream
    #Gets list of all Prime Factors
    def primeFactors(self):
        i = 2
        while i * i <= self.product:
            if self.product % i == 0:
                self.factorList.append(i)
                self.product /= i
=======
    def is_prime(self,x):
        if x >1:
            n = x //2
            for i in range(2, n+1):
                if x % i == 0:
                    return False
            return True
        else:
            return False

    #helper function used to get the list of all factor of the number given
    def getAllFactors(self):
        #counter variable
        i = 1

        #Add all factors of self.product to factorList
        while i <= self.product//2:
            if self.product % i == 0:
                print(i);
                if a.is_prime(i):
                    self.factorList.append(i)
>>>>>>> Stashed changes
            i += 1
        if self.product > 1:
            self.factorList.append(self.product)

    #returns largest prime factor
    def largestPrimeFactors(self):
        self.primeFactors()
        return int(max(self.factorList))
            
<<<<<<< HEAD
=======
        

<<<<<<< Updated upstream
>>>>>>> origin/master
a = Factor(600851475143)
print(a.largestPrimeFactors())
=======
    #function to determine the largest prime factor of the number given
    def getLargestPrimeFactor(self):
##
##        #variable used to keep track of the current value of the number given
##        currentVal = self.factorList[-1]
##
##        #if the length of the factor list is 1, the number given was 1
##        if len(self.factorList) == 1:
##            return 1
##
##        #if the second last number is 1, the number given was a prime number
##        elif self.factorList[-2] == 1:
##            return self.factorList[-1]
##
##        #index variable, set to 2 because everything is divisible by 1
##        i = 2
##
##        #divides currentVal given by factors until currentVal equals 1
##        while currentVal != 1:
##            #if currentVal is divisible by i, divide currentVal by i
##            if currentVal % i == 0:
##                currentVal = currentVal/i
##                #reduces size of self.factorList
##                self.smallerThanOrEqualTo(currentVal)
##                #if i is larger than the self.largest, i is largest prime factor
##                if i > self.largest:
##                    self.largest = i
##                #dividing currentVal by factors starting from 1st factor in list
##                i = 1
##            #incrementing i
##            i += 1
        #returning largest prime factor
        return self.factorList[-1]

a = Factor(600851475143)
a.getAllFactors()
print(a.getLargestPrimeFactor())
>>>>>>> Stashed changes
>>>>>>> Stashed changes
