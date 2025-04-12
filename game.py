from pyfiglet import figlet_format

class Game:

    def __init__(self, size = 3):
        self.size = size
        self.available_moves = [i for i in range(size**2)]
        self.spots = [' ' for i in range(size**2)]
        self.current_letter = 'x'
        self.winner = None

    def print_game(self):
        rows = [self.spots[i*self.size:(i+1)*self.size] for i in range(self.size)]
        for row in rows:
            print(' | '.join([str(i) for i in row]))


    def check_winner(self):
        for i in range(self.size):
            row_set = set(self.spots[i*self.size:(i+1)*self.size])
            col_set = set(self.spots[i : : self.size])

            # horizontal match
            if(('x' in row_set or 'o' in row_set) and len(row_set) == 1):
                print(figlet_format(f'Congratulations!'))
                return True
            
            # vertical match
            if(('x' in col_set or 'o' in col_set) and len(col_set) == 1):
                print(figlet_format(f'Congratulations!'))
                return True
            
        diagnal_set_1 = set(self.spots[0 : : self.size+1])
        diagnal_set_2 = set(self.spots[self.size-1 : -1 : self.size-1])

        # diagonal match
        if(('x' in diagnal_set_1 or 'o' in diagnal_set_1) and len(diagnal_set_1) == 1):
            print(figlet_format(f'Congratulations!'))
            return True

        if(('x' in diagnal_set_2 or 'o' in diagnal_set_2) and len(diagnal_set_2) == 1):
            print(figlet_format(f'Congratulations!'))
            return True

        return False

    def make_move(self, spot):
        if(self.spots[spot] != ' '):
            print('Spot is already occupied!')
            return False
        self.spots[spot] = self.current_letter
        self.current_letter = 'o' if self.current_letter == 'x' else 'x'
        self.available_moves.remove(spot)
        return True
