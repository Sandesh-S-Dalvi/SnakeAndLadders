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


# Add players 
    #--> create_players()

# Roll_Dice():

# Scoring()
    # Read Scores, 
    # ADD Score, 
    # Update Scores, - (Keep adding Score till one player reaches 100 and wins.)
        # Max Score 100
        # To check Snake - (Deduct from Score when player reach specific spot less than 100.)
        # To Check Win
   
## Score_Six()
    # extra_turn

## Next Counts to Snake and ladder

# Display_Score()
    # Game on
    # Snake
    # Ladder
    ## Bounce
    # Winner

if __name__ == '__main__':
    Roll_Dice()
