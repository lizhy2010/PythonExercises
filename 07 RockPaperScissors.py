# Rock Paper Scissors

gameOver = False

while not gameOver:
    print("\n\nRock, Paper, Scissors!")
    print("Player One!")
    
    while True:
        playerA = input("What hand you gonna play? ").lower().strip()
        if playerA in ['rock', 'paper', 'scissors']:
            break
        else:
            print("Rock, paper, scissors only.")
    
    print("\n\nRock, Paper, Scissors!")
    print("Player Two!")
    
    while True:
        playerB = input("What hand you gonna play? ").lower().strip()
        if playerB in ['rock', 'paper', 'scissors']:
            break
        else:
            print("Rock, paper, scissors only.")
            
    if playerA == playerB:
        print("\n\nIt's a DRAW!!")
    else:
        if playerA == 'rock':
            if playerB == 'scissors':
                print("\n\nPLAYER ONE WINS!!")
            elif playerB == 'paper':
                print("\n\nPLAYER TWO WINS!!")
        elif playerA == 'scissors':
            if playerB == 'paper':
                print("\n\nPLAYER ONE WINS!!")
            elif playerB == 'rock':
                print("\n\nPLAYER TWO WINS!!")
        elif playerA == 'paper':
            if playerB == 'rock':
                print("\n\nPLAYER ONE WINS!!")
            elif playerB == 'scissors':
                print("\n\nPLAYER TWO WINS!!")

    reset = input("\n\nNew game? (y/n): ")
    
    if reset[0] == 'y':
        gameOver = False
    else:
        gameOver = True
else:
    print("\n\nGAME OVER!")
