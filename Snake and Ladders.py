# To keep rolling dice with user input till user user commands to stop.

# Valid Inputs --> y,yes,n,no,end.
# Dice value (Max, Min) --> (1,6)
# Module --> random

# Import Modules --> random
# Define Max Min values

# Ask user wants to roll dice
# While users enters invalid input keep asking to enter input again.
# If user enters valid input to roll dice then 
    # print output values
        # Generate random value
    # and continue to ask again from begining.
# Else IF user enters Valid input to Stop Rolling Dice then
    # Print Output values
    # Break
# Else
    # Print Output values
    # Continue

import random as rd
import os

while True:
    os.system('cls')
    p_count = int(input('Enter no. of Players:  ') or 0)
    if p_count < 2 or p_count > 5:
        print('Enter value more than 1 and max 5')
        continue
    else:
        p_count = p_count
        break

class player:
    def __init__(self,name,srnm,counter):
        self.name = name
        self.srnm = srnm
        self.counter = counter

    def Roll_Dice():
        minval = 1
        maxval = 6
        yes = {'y','yes'}
        no = {'n','no','end'}

        os.system('cls')
        
        while True:
            usrin = input('Roll Dice?') or 'y'
            os.system('cls')
            if usrin in yes:
                print('..........Rolling Rolling.. Rolling.........')
                print(rd.randint(minval, maxval))
                continue
            elif usrin in no:
                print('Stopped Rolling')
                break
            else:
                print('Enter Valid responses - Roll Dice:', yes,'Stop Rolling:', no)
                continue

play = dict()
for i in (1,p_count):
    name = input('Enter name of player')
    srnm = i
    counter = 0
    play[i] = player(name, srnm, counter)
    i = i+1

n1 = play1.name
print(n1)

    

Players
    Name
    score
    +role dice
dice
    Range (1,6)
board
    Counters
    snakes
    Ladders
    Start
    End
score
    Add
        Normal
        Ladder
    Delete
        Snake
Display Score
    Normal
    Snake
    Ladder
    Winner
rules




#--> create_players()
    # Ask user for number of players
    # Ask Player Name
    # Create player and set score

# Start_Game
    # Randomly generate first player to start - players play sequence.
    # Set player sequence
    # Ask to Start game

# snakes in [1,2,3,4,5,6]
# Ladders in [1,2,3,4,5,6]

# Roll_Dice():

# Scoring()
    # Read Scores, 
    # ADD Score, 
    # Update Scores, - (Keep adding Score till one player reaches 100 and wins.)
        # To check Ladder
        # To check Snake - (Deduct from Score when player reach specific spot less than 100.)
        # To Check Win - Max Score 100
   
## Score_Six()
    # extra_turn

## Next Counts to Snake and ladder

# Display_Score()
    # Game on
    # Snake
    # Ladder
    ## Bounce
    # Winner

# if __name__ == '__main__':
#     Roll_Dice()
