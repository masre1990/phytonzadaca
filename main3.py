secret=13
guess = int(input("Guess the secret number betweem 1 and 20:"))

if guess == secret:
    print("Bingo!")
else:
    print("Try again!")