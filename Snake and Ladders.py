import random as rd
import os


# Player class to create player instance.

class Player:

    def __init__(self,name,srnm,score,playing):

        self.name = name
        self.srnm = srnm
        self.score = score
        self.playing = playing


     # Roll Dice function    
    def Roll_Dice(self,ifRolled):

        if ifRolled == 'y':
            d_Count = rd.randint(1, 6)
            return d_Count
        else:
            pass

    # Show score
    def GetScore(self):
        return self.score

    # Add Score
    def AddScore(self,d_Count):

        self.score = self.score + d_Count
        return self.score

    # Snake - reduce score
    def ReduceScore(self,d_Count):

        self.score = self.score - d_Count
        return self.score

    # playing change flag
    def winner(self):

        self.playing = 0
        return self.playing
 


# Create Board class
class Board:

    start = 0
    end = 100
    snakes = {8:4,13:9,22:5}
    ladders = {11:5,25:8,35:2}

    # Display Score
    def ShowScore(self,player):

        print('--------------------------------------')

        for i in players:
            print(f"{player[i].name} Score: {player[i].score}")

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
        playing = 1
        player[i] = Player(name,srnm,score,playing)
    return player

player = jls_extract_def()

# Start game Play

board = Board()

os.system('cls\n')

while sum(player.playing) == 1:
    print('Snake and Ladders!!!!')
    board.ShowScore(player)
    print(f"\n{player[i].name}'s turn")
    ifRolled = Input('Roll dice?')

    d_count = player[i].Roll_Dice()
    print(d_count)
    p1_score = player[1].GetScore()
    print(p1_score)

    if p1_score + d_count > 100:
        p1_score = p1_score
    elif p1_score + d_count == 100:
        print('player 1 won')
    else:
        p1_score = player[1].AddScore(d_count)
    # p1_score = 36

    snakes = board.snakes
    ladders = board.ladders

    if p1_score in ladders.keys():
        d_count = ladders[p1_score]
        p1_score = player[1].AddScore(d_count)
        print(player[1].GetScore())
    elif p1_score in snakes.keys():
        d_count = snakes[p1_score]
        p1_score = player[1].ReduceScore(d_count)
    else:
        print(p1_score)
        


# p1_score = player[1].AddScore(d_count)
# print(p1_score)
# d_count = player[1].Roll_Dice()
# print(d_count)
# p1_score =  player[1].AddScore(d_count)
# print(p1_score)


# print(player[2].name)

# d_count = player[2].Roll_Dice()
# print(d_count)
# p2_score = player[2].GetScore()
# print(p2_score)
# p2_score = player[2].AddScore(d_count)
# print(p2_score)
# d_count = player[2].Roll_Dice()
# print(d_count)
# p2_score =  player[2].AddScore(d_count)
# # print(p2_score)
# # print("\n")

print(board.snakes)
print(board.ladders)

board.ShowScore(player)


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
#   Ladder
        # if p1_score in ladder.keys()
        #     p1_score = p1.score + ladder[score]]
        #     return p1_score
        #     print ('{p1} climbed a ladder')
        #     display.score(ladder)
#   Snake(p1_score)
        # else if p1_score in snakes.keys()
        #     p1_score = p1.score - snake[score]]
        #     return p1_score
        #     print ('{p1} bit by snake')
        #     display.score(snake)
#   normal
        # else if p1_score != 100
        #     return p1_score
        #     print ('{p1} moved to {p1_Score}')
        #     display.score(normal)
#   playing
        # else
        #      print(f"{p1} Won the game")
        #      display.score(playing)
            
# Display Score
#     Normal
#     Snake
#     Ladder
#     playing
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
    # playing


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