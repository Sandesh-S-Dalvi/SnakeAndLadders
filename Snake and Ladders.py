import random as rd
import os


# Player class to create player instance.

class Player:

    def __init__(self,name,srnm,score):

        self.name = name
        self.srnm = srnm
        self.score = score


     # Roll Dice function    
    def Roll_Dice(self):

        d_Count = rd.randint(1, 6)
        return d_Count


    # Show score
    def GetScore(self):
        return self.score


    # Add Score
    def AddScore(self,score,d_Count):

        self.score = self.score + d_Count
        return self.score


    # Snake - reduce score
    def ReduceScore():

        score = score - snake
        return score
 


# Create Board class
class Board:

    start = 0
    end = 100
    snakes = {8:4,13:9,22:16}
    ladders = {11:18,25:36,35:48}

# Display Score
def ShowScore():

    print('--------------------------------------')
    print(f"{player[1].name} Score: {p1_score}  Next Ladder: {ladder}  Next Snake: {Snake} ")
    print(f"{player[2].name} Score: {p2_score}")
    print('--------------------------------------')
    


######################################################################################



# Ask for No. of Players in game.

while True:

    os.system('cls')

    p_count = int(input('Enter no. of Players:  ') or 0)

    if p_count < 2 or p_count > 5:

        print('Enter value more than 1 and upto 5')
        continue

    else:

        p_count = p_count

        break

# Create players instances

players = range(1,p_count+1)

def jls_extract_def():
    player = {}
    for i in players: #[:p_count]:
        name = input('Enter name of player: ')
        srnm = 0
        score = 0
        player[i] = Player(name,srnm,score)
    return player

player = jls_extract_def()

# Play

board = Board()

os.system('cls\n')

print('Snake and Ladders!!!!\n')

print('--------------------------------------')

for i in players:
    print(f"{player[i].name} Score: {player[i].score}")

print('--------------------------------------')

print(player[1].name)

d_count = player[1].Roll_Dice()
print(d_count)
p1_score = player[1].GetScore()
print(p1_score)
p1_score = player[1].AddScore(p1_score,d_count)
print(p1_score)
d_count = player[1].Roll_Dice()
print(d_count)
p1_score =  player[1].AddScore(p1_score,d_count)
# print(p1_score)


print(player[2].name)

d_count = player[2].Roll_Dice()
print(d_count)
p2_score = player[2].GetScore()
print(p2_score)
p2_score = player[2].AddScore(p2_score,d_count)
print(p2_score)
d_count = player[2].Roll_Dice()
print(d_count)
p2_score =  player[2].AddScore(p2_score,d_count)
# print(p2_score)
# print("\n")
print('--------------------------------------')
print(f"{player[1].name} Score: {p1_score}")
print(f"{player[2].name} Score: {p2_score}")
print('--------------------------------------')
    


# Players

#     Name
#     score

#     +role dice
# dice

#     Range (1,6)

# board
#     snakes
#     Ladders
#     Start
#     End
# score
#     Add
#         Normal
#         Ladder
#         Delete
#         Snake
# Display Score
#     Normal
#     Snake
#     Ladder
#     Winner
# rules





#--> create_players()

    # Ask user for number of players

    # Ask Player Name

    # Create player and set score


# Start_Game

    ## Randomly generate first player to start - players play sequence.

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


# Start Game
# Player 1 rolls Dice - Roll dice
# P1 checks Score - Display count
# Moves counter - Add count
# Check for - If Else
    # Gen
    # Snake
    # Ladder
# Message - Snake ladder
# P1 places Counter

# Repeat for Player 2