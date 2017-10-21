# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# creating a random input from computer side to make it more fun
import random 

def assign_computer_choice(rand_number):
    if rand_number == 1 :
        return "rock"
    elif rand_number == 2:
        return "paper"
    elif rand_number == 3:
        return "scissors"


def user_had_rock(computer_choice):
    if computer_choice == "rock":
        print("There is a tie. \t\t=> AGAIN\n")
    elif computer_choice == "paper":
        print("You LOST. \t You were against => {}".format(computer_choice))
    elif computer_choice == "scissors":
        print("You WON. \t You were against => {}".format(computer_choice))


def user_had_paper(computer_choice):
    if computer_choice == "rock":
        print("You WON. \t You were against => {}".format(computer_choice))
    elif computer_choice == "paper":
        print("There is a tie. \t\t=> AGAIN\n")
    elif computer_choice == "scissors":
        print("You LOST. \t You were against => {}".format(computer_choice))


def user_had_scissors(computer_choice):
    if computer_choice == "rock":
        print("You LOST. \t You were against => {}".format(computer_choice))
    elif computer_choice == "paper":
        print("You WON. \t  You were against => {}".format(computer_choice))
    elif computer_choice == "scissors":
        print("There is a tie. \t\t=> AGAIN\n")
        

print("What you want to choose : ( ROCK, PAPER, SCISSORS )")
user_choice = input("> ")

number = random.randint(1,3)
computer_choice = assign_computer_choice(number)

while user_choice != "0":
    if user_choice.lower() == "scissor":
        print("""/*** WE CAN'T ACCEPT THIS, ACUTALLY ITS A PAIR OF "SCISSORS" ***\\ \n""")
    elif user_choice.lower() == "rock":
        user_had_rock(computer_choice)
    elif user_choice.lower() == "paper":
        user_had_paper(computer_choice)
    elif user_choice.lower() == "scissors":
        user_had_scissors(computer_choice)

    user_choice = input("What you want to choose : ( ROCK, PAPER, SCISSOR )\
                         \nOR Hit '0' Zero to Quit. \n> ")   
    number = random.randint(1,3)
    computer_choice = assign_computer_choice(number) 
