import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to check for snakes and ladders
def check_snakes_ladders(position):
    # Define snakes and ladders positions
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    if position in snakes:
        print("Oops! You landed on a snake. You move down to position", snakes[position])
        return snakes[position]
    elif position in ladders:
        print("Great! You landed on a ladder. You move up to position", ladders[position])
        return ladders[position]
    else:
        return position

# Function to play the game
def play_game():
    player1 = 0
    player2 = 0
    player1_turn = True

    while True:
        if player1_turn:
            print("Player 1's turn")
        else:
            print("Player 2's turn")

        # Roll the dice
        roll = roll_dice()
        print("You rolled a", roll)

        if player1_turn:
            player1 += roll
            if player1 > 100:
                player1 = 100
            print("Player 1 is now at position", player1)
            player1 = check_snakes_ladders(player1)

            if player1 == 100:
                print("Player 1 wins!")
                break
        else:
            player2 += roll
            if player2 > 100:
                player2 = 100
            print("Player 2 is now at position", player2)
            player2 = check_snakes_ladders(player2)

            if player2 == 100:
                print("Player 2 wins!")
                break

        if roll != 6:
            player1_turn = not player1_turn

        input("Press Enter to continue...")
        print("\n")

# Start the game
play_game()
