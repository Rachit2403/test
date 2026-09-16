import random
options = ("r", "p", "s")

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (r, p, s): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("IT'S A TIE!!!")
    elif player == "r":
        if computer == "s":
            print("COMPUTER WINS!!!")
        else:
            print("PLAYER WINS!!!")
    elif player == "p":
        if computer == "r":
            print("PLAYER WINS!!!")
        else:
            print("COMPUTER WINS!!!")
    elif player == "s":
        if computer == "r":
            print("COMPUTER WINS!!!")
        else:
            print("PLAYER WINS!!!")
    if not input("Play again (y/n)?: ").lower() == "y":
        running = False
print("GOODBYE!!!")