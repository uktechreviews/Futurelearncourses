from random import randint

print ("Can you guess my number?, I am going to think of a number between 1 and 10")

computer_choice = randint(1,10)
#print (computer_choice)


def game():
    win = False
    count = 0
    while win != True:
        guess = int(input("Enter a number between 1 and 10 "))
        count +=1
        if guess == computer_choice:
            print ("You got it")
            win = True
        elif guess < computer_choice:
            print ("Too low")
            win = False
        elif guess > computer_choice:
            print ("Too high")
            win = False
    return count

goes =game()
print ("It took you " + str(goes) + " goes")
