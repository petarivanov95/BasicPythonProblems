import random

# def generate_random_number():
#     random_number = random.randint(1,5)

random_number = random.randint(1,5)

list_guesses = []

user_guess = int(input("What was the number "))
list_guesses.append(user_guess)

if user_guess == random_number:
    print("Great! It took you only 1 try.")
else:
    while user_guess != random_number:
        user_guess = int(input("What is your guess "))
        list_guesses.append(user_guess)
        if user_guess == random_number:
            print("Great! It took you {} tries.".format(len(list_guesses)))
