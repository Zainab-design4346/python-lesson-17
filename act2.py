import random
option=["rock","paper","scissors"]
user_choice=input("Enter your choice(rock, paper, scissors):")
computer_choice=random.choice(option)
print(f"computer choice:{computer_choice}")
print(f"your choice:{user_choice}")

if user_choice==computer_choice:
    print("It is a tie")
elif user_choice=="rock" and computer_choice=="scissors":
    print("Rock smashes scissors, YOU WIN!")
elif user_choice=="paper" and computer_choice=="rock":
    print("Paper covers rock, YOU WIN!")
elif user_choice=="scissors" and computer_choice=="paper":
    print("Scissors cut paper, YOU WIN!")
else:
    print("Computer wins!")