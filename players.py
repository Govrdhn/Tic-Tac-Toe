import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
# computer player
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        spot = None
        while True:
            spot = math.trunc(random.random()*10)
            if(spot in game.available_moves):
                return spot

# manual player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        gotSpot = False
        spot = None
        while not gotSpot:
            try:
                spot = int(input("Enter the spot:"))
                if(spot in game.available_moves):
                    gotSpot = True
                    return spot
                else:
                    raise ValueError
            except:
                print("Enter a valid spot!")
                continue

# x = ['x', 'x', 'x', 'o', 'o', 'x', ' ', 'x', ' ']
# rows = [x[i*3:(i+1)*3] for i in range(3)]
# for row in rows:
#             print(' | '.join([i for i in row]))

# if(x[0] == x[1] == x[2] == 'x' or 'o'):
#            print(f'Winner is {x[0]} player')
