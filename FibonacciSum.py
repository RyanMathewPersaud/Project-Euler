#calculates the sum of all even numbers in the fibonacci sequence
def evenFibonacciSum(limit):
    
    #variables and list of numbers in the fibonacci sequence
    previous = 0
    current = 1
    total = 0
    temp = 0
    sequenceList = []

    #gets all numbers in fibonacci sequence under the limit and appends
    #all of the even values into sequenceList
    while current <= limit:
        temp = current
        if current % 2 == 0:
            sequenceList.append(current)
        current += previous
        previous = temp

    #calculates and returns the sum of sequenceList
    total = sum(sequenceList)
    return total

a = evenFibonacciSum(4000000)
print(a)
        
        

    
