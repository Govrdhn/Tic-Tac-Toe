from game import Game 
from players import HumanPlayer, ComputerPlayer

human = HumanPlayer('x')
computer = ComputerPlayer('o')
game = Game()

while True:
    move_spot = None
    if(game.current_letter == 'x'):
        move_spot = human.get_move(game)
    else:
        print('computer:')
        move_spot = computer.get_move(game)
    if(not game.make_move(move_spot)):
        continue
    game.print_game()
    if(game.check_winner()):
        break