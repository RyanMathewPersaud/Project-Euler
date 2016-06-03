'''
Title: Largest Prime Factor
Name: Ryan Persaud
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

    #helper function used to get the list of all factor of the number given
    def getAllFactors(self):
        #counter variable
        i = 1

        #Add all factors of self.product to factorList
        while i <= self.product//2:
            if self.product % i == 0:
                self.factorList.append(i)
            i += 1
        return self.factorList

    #Removes all numbers from factorList that are greater than num
    def smallerThanOrEqualTo(self, num):
        #counter
        i = 0

        #checks which numbers in self.factorList ith item is greater than
        while i < len(self.factorList):
            #if ith item is greater than num, removes that element and all
            #elements larger than the ith element
            if self.factorList[i] >= num:
                self.factorList = self.factorList[:i]

            #increments i
            i += 1
     
        

    #function to determine the largest prime factor of the number given
    def getLargestPrimeFactor(self):

        #variable used to keep track of the current value of the number given
        currentVal = self.factorList[-1]

        #if the length of the factor list is 1, the number given was 1
        if len(self.factorList) == 1:
            return 1

        #if the second last number is 1, the number given was a prime number
        elif self.factorList[-2] == 1:
            return self.factorList[-1]

        #index variable, set to 2 because everything is divisible by 1
        i = 2

        #divides currentVal given by factors until currentVal equals 1
        while currentVal != 1:
            #if currentVal is divisible by i, divide currentVal by i
            if currentVal % i == 0:
                currentVal = currentVal/i
                #reduces size of self.factorList
                self.smallerThanOrEqualTo(currentVal)
                #if i is larger than the self.largest, i is largest prime factor
                if i > self.largest:
                    self.largest = i
                #dividing currentVal by factors starting from 1st factor in list
                i = 1
            #incrementing i
            i += 1
        #returning largest prime factor
        return self.largest

a = Factor(45)
a.getAllFactors()
print(a.getLargestPrimeFactor())
