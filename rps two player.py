import random

choices = ["Rock", "Paper", "Scissors"]

def rps_round(player1_choice,player2_choice):
    if player1_choice == player2_choice:
        print("draw ")
        return ("draw")

    elif player1_choice == "Rock" and player2_choice == "Scissors":
        print("player 1 wins")
        return ("player1_wins")

    elif player1_choice == "Paper" and player2_choice == "Rock":
        print("player 1 wins")
        return ("player1_wins")

    elif player1_choice == "Scissors" and player2_choice == "Paper":
        print("player 1 wins")
        return ("player1_wins")

    else:
        print("player 2 wins")
        return ("player2_wins")


def pick_rps():
    player = input ("select your choice [R,P,S] ")
    player_choice = "None selected"
    if player == "R":
        player_choice = "Rock"
    if player == "P":
        player_choice = "Paper"
    if player == "S":
        player_choice = "Scissors"
    return player_choice

def rps_game():
    player1_score = 0
    player2_score = 0
    game_over = False
    print ("Type R for Rock")
    print ("type P for Paper")
    print ("type S for scissors")
    wins = int(input ("How many wins would you like "))
    while game_over != True:
        print ("Player 1")
        player1_choice = pick_rps()
        print ("Player 2")
        player2_choice = pick_rps()
        winner=rps_round(player1_choice,player2_choice)
        if winner == "player1_wins":
            player1_score +=1
        elif winner == "player2_wins":
            player2_score +=1
        if player1_score >5:
            game_over = True
            return ("player 1")
        if player2_score > 5:
            game_over = True
            return ("Player 2")


champion = rps_game()


