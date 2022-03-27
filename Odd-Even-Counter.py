# Problem 16 from Chapter 5 from Gaddis
# Odd/Even Counter

import random

# Generates a list with random values

# the function below checks for the odd/even numbers that will be generated in a range
def odd_even_counter(myRange):
    myEvenCounter = 0
    myOddCounter = 0
    for num in range(myRange):
        random_number = random.randint(1,2)
        if random_number%2==0:
            myEvenCounter += 1
        else:
            myOddCounter += 1
    print("Odd:", myOddCounter)
    print("Even: ", myEvenCounter)

#below you can see the odds/evens as counted from 1000 runs
odd_even_counter(1000)
