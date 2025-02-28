import random
user = input("Enter your choice(Rock/Paper/ Scissor): ")
choices = ["rock", "paper", "scissors"]
com_choice = random.choice(choices)
if user == com_choice:
    result = "It's a tie!"
elif (user == "rock" and com_choice == "scissor") or \
     (user == "paper" and com_choice == "rock") or \
     (user == "scissor" and com_choice == "paper"):
    result = "You win!...."
else:
    result: "Computer win.."
print("Computer's Choice: ", com_choice)
print(result)