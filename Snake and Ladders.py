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

        if self.score + d_Count > end:
            return self.score
        else:
            self.score = self.score + d_Count
            return self.score

    # Ladder - Add Score
    def LadderScore(self,d_Count):

        self.score = d_Count
        print(f"{bcolors().OKGREEN}{bcolors().BOLD}{player[i].name} climbed a Ladder{bcolors.ENDC}")
        print(player[i].score)
        print(f"{player[i].name} new score is: {self.score}")
        time.sleep(3)
        return self.score   

    # Snake - reduce score
    def SnakeScore(self,d_Count):

        self.score = d_Count
        print(f"{bcolors().OKRED}{bcolors().BOLD}{player[i].name} bit by Snake{bcolors.ENDC}")
        print(player[i].score)
        print(f"{player[i].name} new score is: {self.score}")
        time.sleep(3)
        return self.score

    # playing change flag
    def winner(self):

        self.playing = 0
        return self.playing


# Create Board class
class Board:

    start = 0
    end = 100

    # snakes = {1:11,2:22,3:33,4:44,5:55,6:66}
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
    OKRED = '\033[91m'
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
        print(f"{bcolors().OKRED}{bcolors().BOLD}Snake {bcolors().OKCYAN}{bcolors().BOLD}and {bcolors().OKGREEN}{bcolors().BOLD}Ladders!!!!{bcolors().ENDC}\n")
        p_count = int(input('Enter no. of Players (2 - 5):  ') or 0)
        if p_count > 1 and p_count <= 5:
            os.system('cls')
            print(f"{bcolors().OKRED}{bcolors().BOLD}Snake {bcolors().OKCYAN}{bcolors().BOLD}and {bcolors().OKGREEN}{bcolors().BOLD}Ladders!!!!{bcolors().ENDC}\n")
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

#### Start game Play ####

i = 1
while sum(player[i].playing for i in player.keys()) > 1:

    os.system('cls\n')

    # if sum(player[i].playing for i in player.keys()) > 1 and player[i].playing == 1:
    # if player[i].playing == 1:
    #     i = i
    # else:
    #     i += 1
    #     continue
    
    print(f"{bcolors().OKRED}{bcolors().BOLD}Snake {bcolors().OKCYAN}{bcolors().BOLD}and {bcolors().OKGREEN}{bcolors().BOLD}Ladders!!!!{bcolors().ENDC}\n")
    board.ShowScore(player)

    print(f"\nSnakes on {snakes}")
    print(f"Ladders on {ladders}")

    # Ask Player to Roll Dice

    print(f"\n{player[i].name}'s turn")
    ifRolled = input('Roll dice?' or 'y')
    
    d_count = player[i].Roll_Dice(ifRolled)
    print(f"Dice Count: {d_count}")
    p_score = player[i].GetScore()
    print(f"{player[i].name} old score was: {p_score}")

    p_score = player[i].AddScore(d_count)

    if p_score in ladders.keys():
        p_score = ladders.get(p_score)
        player[i].LadderScore(p_score)

    elif p_score in snakes.keys():
        p_score = snakes.get(p_score)
        player[i].SnakeScore(p_score)
        
    elif p_score == end:
        print(f"{player[i].name} new score is: {p_score}")
        print(f"{player[i].name} won the game.")
        player[i].winner()
        time.sleep(3)

        if sum(player[j].playing for j in player.keys()) == 1:
            break

    else:
        print(f"\n{bcolors().OKGREEN}{bcolors().BOLD}{player[i].name} new score is: {p_score}{bcolors().ENDC}{bcolors().ENDC}")
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
