#Helper function using recursion, returns the n factorial.
def factorial(n):
    if(n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return n*factorial(n-1)

#calculates the sum of the digits from n factorial.
def sum_digits(n):
    fact = factorial(n)
    factorial_result = str(fact)
    length_of_number = len(str(fact))

    result = 0
    
    for i in range(0, length_of_number):
        result += int(factorial_result[i])
    
    return result

#prints the sum of the digits of n factorial
print(sum_digits(100))
