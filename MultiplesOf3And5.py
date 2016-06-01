'''
Name of Project: MultiplesOf3And5
Author: Ryan Persaud
Date: June 1, 2016
Description: Finding the sum of multiples of both 3 or 5 where the multiple is under 1000



'''
#Finding the sum of multiples of 3 or 5,where the multiple is under 1000

#Calculates sum of all numbers under the limit where num1 or num2 are factors
def sumOfMultiples(num1, num2, limit):
    #total represents the sum of the multiples, i is while loop counter
    total = 0
    i = 0

    '''if num1 or num2 are factors of i and i is lower than the limit
    then add i to the total since i is a multiple of num1 or num2
    '''
    while i < limit:
        if (i % num1 == 0) or (i % num2 == 0):
            total += i
        i+=1
    return total

#Prints the sum of multiples of 3 or 5 under 1000
a = sumOfMultiples(3, 5, 1000)
print(a)
