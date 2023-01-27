import random as rd
import time
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

    # Ladder - Add Score
    def LadderScore(self,d_Count):

        self.score = d_Count
        return self.score    

    # Snake - reduce score
    def SnakeScore(self,d_Count):

        self.score = d_Count
        return self.score

    # playing change flag
    def winner(self):

        self.playing = 0
        return self.playing


# Create Board class
class Board:

    start = 0
    end = 20
    snakes = {32:10,36:6,48:26,62:18,88:24,95:56,97:78}
    ladders = {4:14,8:30,21:42,28:76,50:67,71:92,80:99}

    # Display Score
    def ShowScore(self,player):

        print('--------------------------------------')
        for i in players:
            print(f"{player[i].name} Score: {player[i].score}")
        print('--------------------------------------')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    


######################################################################################
os.system('cls\n')

while True:

    try:
        p_count = int(input('Enter no. of Players (2 - 5):  ') or 0)
        if p_count > 1 and p_count <= 5:
            os.system('cls')
            print(f'No. of players set to {p_count}')
            break
    except ValueError:
        print('Enter value more than 1 and upto 55')
        continue
    else:
        print('Enter value more than 1 and upto 5')
        continue

# Create players instances

players = range(1,p_count+1)

def jls_extract_def():
    player = {}
    for i in players:
        name = input('Enter name of player: ')
        srnm = 0
        score = 0
        playing = 1
        player[i] = Player(name,srnm,score,playing)
    return player

player = jls_extract_def()

#### Creating Board instance ####

board = Board()
ladders = board.ladders
snakes = board.snakes
end = board.end

os.system('color')
x = 0
for i in range(24):
  colors = ""
  for j in range(5):
    code = str(x+j)
    colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
  print(colors)
  x = x + 5

#### Start game Play ####

i = 1
while sum(player[i].playing for i in player.keys()) > 1:

    # os.system('cls\n')

    # if sum(player[i].playing for i in player.keys()) > 1 and player[i].playing == 1:
    # if player[i].playing == 1:
    #     i = i
    # else:
    #     i += 1
    #     continue
    
        print('Snake and Ladders!!!!')
        board.ShowScore(player)

        # Ask Player to Roll Dice

        print(f"\n{player[i].name}'s turn")
        ifRolled = input('Roll dice?' or 'y')
        
        d_count = player[i].Roll_Dice(ifRolled)
        print(f"Dice Count: {d_count}")
        p_score = player[i].GetScore()
        print(f"{player[i].name} old score was: {p_score}")

        if p_score + d_count > end:
            p_score = p_score
        else:
            p_score = player[i].AddScore(d_count)

        if p_score in ladders.keys():
            p_score = ladders.get(p_score)
            p_score = player[i].LadderScore(p_score)
            print(f"{bcolors().BOLD}{player[i].name} climbed a 'ladder{bcolors.ENDC}")
            print(player[i].GetScore())
            print(f"{player[i].name} new score is: {p_score}")
            time.sleep(3)

        elif p_score in snakes.keys():
            p_score = snakes.get(p_score)
            p_score = player[i].SnakeScore(p_score)
            print(f"{player[i].name} bit by snake")
            print(player[i].GetScore())
            print(f"{player[i].name} new score is: {p_score}")
            time.sleep(3)

        elif p_score == end:
            print(f"{player[i].name} new score is: {p_score}")
            print(f"{player[i].name} won the game.")
            player[i].winner()
            time.sleep(3)

            if sum(player[j].playing for j in player.keys()) == 1:
                break

        else:
            print(f"{bcolors().OKGREEN}{bcolors().BOLD}{player[i].name} new score is: {p_score}{bcolors().ENDC}{bcolors().ENDC}")
            time.sleep(3)

        if i + 1 in player.keys():
            i += 1
        else:
            i = 1

    # else:
    #     if i + 1 in player.keys():
    #         i += 1
    #     else:
    #         i = 1

board.ShowScore(player)
print('Game ends')



x = 0
for i in range(24):
  colors = ""
  for j in range(5):
    code = str(x+j)
    colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
  print(colors)
  x = x + 5


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
        # if p_score in ladder.keys()
        #     p_score = p1.score + ladder[score]]
        #     return p_score
        #     print ('{p1} climbed a ladder')
        #     display.score(ladder)
#   Snake(p_score)
        # else if p_score in snakes.keys()
        #     p_score = p1.score - snake[score]]
        #     return p_score
        #     print ('{p1} bit by snake')
        #     display.score(snake)
#   normal
        # else if p_score != 100
        #     return p_score
        #     print ('{p1} moved to {p_score}')
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