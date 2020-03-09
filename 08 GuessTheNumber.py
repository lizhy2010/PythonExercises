import random

gameOver = False
num = random.randint(1, 100)
tries = 0

# GAME LOOP
while not gameOver:

    print("\n\nGUESS THE NUMBER GAME!!")
    guess = input("What's your guess? (1 - 100): ")
    
    if guess.lower().strip() == 'exit':
        win = False
        gameOver = True
        
    elif guess.isdigit() and int(guess) > 0 and int(guess) < 101:
        if int(guess) < num:
            print("\nHigher!")
        elif int(guess) > num:
            print("\nLower!")
        elif int(guess) == num:
            win = True
            gameOver = True
        
    else:
        print("Invalid input.")
        
    tries += 1
else:
    print("\n\nGAME OVER!!")
    
    if win:
        print("YOU WIN!! IT'S %s" % num)
    else:
        print("You quit the game.")
        
    print("Number of tries: %s" % tries)
#END GAME LOOP