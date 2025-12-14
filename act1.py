import random
play=True
n=str(random.randint(10,20))
print("Let's guess number between 10 to 20")
print("The game will end when you guess the correct number")

while play:
    guess=input("Guess the number: ")
    if guess==n:
        print("You guessed the right number!")
        print("The number was ",n)
        break
    else:
         print("Try again")