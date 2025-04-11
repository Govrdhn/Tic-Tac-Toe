from pyfiglet import figlet_format

class Game:

    def __init__(self):
        self.available_moves = [i for i in range(9)]
        self.spots = [' ' for i in range(9)]
        self.current_letter = 'x'
        self.winner = None

    def print_game(self):
        rows = [self.spots[i*3:(i+1)*3] for i in range(3)]
        for row in rows:
            print(' | '.join([str(i) for i in row]))

    def check_winner(self):
        if(self.spots[0] == self.spots[1] == self.spots[2] == ('x' or 'o')): #fixthis
            print(figlet_format(f'Winner is {self.spots[0]} player'))
            return True
        return False

    def make_move(self, spot):
        if(self.spots[spot] != ' '):
            print('Spot is already occupied!')
            return False
        self.spots[spot] = self.current_letter
        self.current_letter = 'o' if self.current_letter == 'x' else 'x'
        return True
