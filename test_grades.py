# a simple program that takes in input about one's points on a test and determines the test grade

# The standard values for the grade cutoffs
A = 90
B = 80
C = 70
D = 60

#takes in the user's input for their score
result = int(input("What was your score? "))

if result >= A:
    print("Your grade is A")
elif result >= B:
    print("Your grade is B")
elif result >= C:
    print("Your grade is C")
elif result >= D:
    print("Your grade is D")
else:
    print("Your grade is F")

