#From Automate the Boring Stuff - Functions chapter

# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    if number%2==0:
        new_number = number//2
        print(new_number)
        return new_number
    else:
        new_number = 3*number+1
        print(new_number)
        return(new_number)

# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.

number = int(input("Enter an integer: "))
while number != 1:
    number = collatz(number)

