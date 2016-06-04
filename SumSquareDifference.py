def SSD(n):
    sum_of_100_natural_numbers = 0
    squares = list()
    
    for i in range(0, 101):
        sum_of_100_natural_numbers += i
        squares.append(i ** 2) 

    return (sum_of_100_natural_numbers ** 2) - sum(squares)

print(SSD(100))

