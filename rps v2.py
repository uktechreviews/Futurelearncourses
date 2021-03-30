import random

choices = ["Rock", "Paper", "Scissors"]

def rps_game():
    print ("Type R for Rock")
    print ("type P for Paper")
    print ("type S for scissors")
    player = input ("select your choice [R,P,S] ")
    player_choice = "None selected"
    if player == "R":
        player_choice = "Rock"
    if player == "P":
        player_choice = "Paper"
    if player == "S":
        player_choice = "Scissors"
    computer_choice = random.choice(choices)
    print ("You selected " + player_choice)
    print ("The computer selected " + computer_choice)

    if player_choice == computer_choice:
        print("draw ")

    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You win :)")

    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You win :)")

    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You Win :)")

    else:
        print("The computer wins :(")


rps_game()
