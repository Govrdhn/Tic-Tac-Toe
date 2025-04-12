import math
import random

class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
    
# computer player
class ComputerPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)
    
    def get_move(self, game):
        spot = None
        while True:
            spot = math.trunc(random.random()*10)
            if(spot in game.available_moves):
                return spot

# manual player
class HumanPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)

    def get_move(self, game):
        gotSpot = False
        spot = None
        while not gotSpot:
            try:
                spot = int(input("Enter the spot:"))-1
                if(spot in game.available_moves):
                    gotSpot = True
                    return spot
                else:
                    raise ValueError
            except:
                print("Enter a valid spot!")
                continue