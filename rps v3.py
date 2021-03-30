import random

choices = ["Rock", "Paper", "Scissors"]

def rps_round():
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
        return ("draw")

    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You win :)")
        return ("player_wins")

    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You win :)")
        return ("player_wins")

    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You Win :)")
        return ("player_wins")

    else:
        print("The computer wins :(")
        return ("computer_wins")

def rps_game():
    player_score = 0
    computer_score = 0
    while True:
        winner=rps_round()
        print (winner)
        if winner == "player_wins":
            player_score +=1
        elif winner == "computer_wins":
            computer_score +=1
        print("The computer scored "+str(computer_score))
        print("You scored "+str(player_score))

rps_game()

