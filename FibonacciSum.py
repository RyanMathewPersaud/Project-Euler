#calculates the sum of all even numbers in the fibonacci sequence
def evenFibonacciSum(limit):
    
    #variables and list of numbers in the fibonacci sequence
    previous = 0
    current = 1
    total = 0
    temp = 0
    sequenceList = []

    #gets and appends all numbers in fibonacci sequence under the limit
    #and appends the values in sequenceList
    while current <= limit:
        temp = current
        sequenceList.append(current)
        current += previous
        previous = temp

    #calculates the sum of only the even numbers in the fibonacci sequence
    for i in sequenceList:
        if i % 2 == 0:
            total += i
            
    #returns the sum of only the even numbers in the fibonacci sequence
    return total

a = evenFibonacciSum(4000000)
print(a)
        
        

    
