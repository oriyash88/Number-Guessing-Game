import random

r = random.randrange(0,101)

print("Welcome to my 'Number Guessing Game'")
print("Please type a number between 0 and 100 "  )
guesses = 0
print(r)
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please type a number.")
        quit()

    if user_guess == r:
        print("Yue got it!")
        break
    else:
        if user_guess > r:
            print("You were above the number!")
        if user_guess < r:
            print("You were below the number!")
print("You got it in",guesses, "guesses")
print("Your score for this round is:", 101-guesses)