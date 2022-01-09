import random

# ROCKPAPERSCISSORS
def user_choice(input):
    if input in ["rock", "ROCK", "R", "r", "Rock"]:
        print("User chose rock")
        return "rock"
    elif input in ["paper", "PAPER", "Paper", "P", "p"]:
        print("User chose paper")
        return "paper"
    elif input in ["Scissors", "scissors", "S", "s", "Scissors"]:
        print("User chose scissors")
        return "scissors"



# get value from the user

print("Enter rock, paper, or scissors")
input_from_the_user = input("Enter your choice:")

# create a function for user & call it
users_final_answer = user_choice(input_from_the_user)
print(users_final_answer)


# random choice by computer
computer_choice = ["rock", "paper", "scissors"]
random_choice = random.choice(computer_choice)
print("computer choice is",random_choice)
# condition
if str(users_final_answer)=="rock":
    if random_choice=="rock" :
        print("You chose rock. Computer Chose rock.It is a Tie")
    elif random_choice=="paper":
        print("You chose rock. Computer chose paper. Computer won")
    elif random_choice=="scissors":
        print("You chose rock.Computer chose scissors. Computer won")
elif str(users_final_answer)=="paper":
    if random_choice=="paper":
        print("You chose paper. Computer chose paper. It is a Tie")
    elif random_choice=="rock":
        print("You chose paper. Computer chose rock. You won")
    elif random_choice=="scissors":
        print("You chose paper. Computer chose scissors. Computer won")
elif str(users_final_answer)=="scissors":
    if random_choice=="scissors":
        print("You chose scissors. Computer chose scissors. It is a Tie")
    elif random_choice=="paper":
        print("You chose scissors. Computer chose paper. You won")
    elif random_choice=="rock":
        print("You chose scissors. Computer chose rock. Computer won")


#\\
