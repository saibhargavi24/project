print("____________ NUMBER GUESSING GAME ____________")
print("Let's play the game...I'm thinking a number between 1 to 100.")

import random
number = random.randint(1,100)
level = input("Choose the game mode: Type 'E' for Easy or 'H' for Hard: ")
easy_attempts = 10
hard_attempts = 5
def game_mode(level):
    if level == 'E':
        return easy_attempts
    elif level == 'H':
        return hard_attempts
    else:
        return None

attempts = game_mode(level)

def check_number(guess,number):
    if guess > number:
        print("Your guess is too high! Try again...\n")
        return False
    elif guess < number:
        print("Your guess is too low! Try again...\n")
        return False
    else:
        print("Congratulations!!You won..The number is",number)
        return True

if attempts is None:
    print("Please choose valid level")
else:
    while attempts > 0:
        print(f"You have {attempts} attempts now")
        guess = int(input("What's your guess?: "))
        if check_number(guess,number):
            break
        attempts -= 1
    if attempts == 0:
        print("Sorry, you didn't guess the number. Better luck next time! The number was", number)
        
