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

rps_game()
