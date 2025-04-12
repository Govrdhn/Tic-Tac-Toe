from game import Game
from players import HumanPlayer, ComputerPlayer

human = HumanPlayer('Govardhan', 'x')
computer = ComputerPlayer('Computer', 'o')
game = Game(human, computer)

game.play()