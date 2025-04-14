import curses
from game import Game
from players import HumanPlayer, ComputerPlayer
from base.multi_choice_input import multi_choice_input

def get_play_mode(stdscr):
    question = 'Select game mode:'
    options = ['vs Computer', 'Pass n Play']
    return multi_choice_input(stdscr, question, options)

def main():
    player_1 = HumanPlayer('player_1', 'x')
    player_2 = None
    choice = curses.wrapper(get_play_mode)

    if(choice == 0):
        player_2 = ComputerPlayer('computer', 'o')

    elif(choice == 1):
        player_2 = HumanPlayer("player_2", 'o')

    elif(choice == None):
        print("Game exited!")
        return

    game = Game(player_1, player_2)
    game.play()

main()