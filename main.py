from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a diificulty. Type 'easy' or 'hard':\n")
attempts = 5
number = random.randint(1,100)  #randint includes both 1 and 100 
# print(number)

if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == 'hard':
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("You have entered wrong choice. Game over.")
    exit()

should_not_continue = False

while not should_not_continue:
    if attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You guessed that right, {number} was the number I was thinking.")
            should_not_continue = True
        elif guess > number:
            attempts -=1
            if attempts == 0:
                print("You lost all your chances.")
                print(f"{number} was the number I was expecting.")
                break
            print(f"Too high. Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess < number:
            attempts -=1
            if attempts == 0:
                print("You lost all your chances.")
                print(f"{number} was the number I was expecting.")
                break
            print(f"Too low. Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")