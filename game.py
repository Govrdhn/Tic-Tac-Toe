from pyfiglet import figlet_format

class Game:

    def __init__(self, x_player, y_player, size = 3):
        self.size = size
        self.available_moves = [i for i in range(size**2)]
        self.spots = [' ' for i in range(size**2)]
        self.x_player = x_player
        self.y_player = y_player
        self.current_letter = 'x'
        self.current_player = x_player
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
                print(figlet_format(f'{self.current_player.name} won!'))
                return True
            
            # vertical match
            if(('x' in col_set or 'o' in col_set) and len(col_set) == 1):
                print(figlet_format(f'{self.current_player.name} won!'))
                return True
            
        diagnal_set_1 = set(self.spots[0 : : self.size+1])
        diagnal_set_2 = set(self.spots[self.size-1 : -1 : self.size-1])

        # diagonal match
        if(('x' in diagnal_set_1 or 'o' in diagnal_set_1) and len(diagnal_set_1) == 1):
            print(figlet_format(f'{self.current_player.name} won!'))
            return True

        if(('x' in diagnal_set_2 or 'o' in diagnal_set_2) and len(diagnal_set_2) == 1):
            print(figlet_format(f'{self.current_player.name} won!'))
            return True
        
        if(len(self.available_moves) == 0):
            print(figlet_format("It's a Draw!"))
            return False

        return False

    def make_move(self):
        spot = self.current_player.get_move(self)
        letter = self.current_player.letter
        if(self.spots[spot] != ' '):
            print('Spot is already occupied!')
            return False
        self.spots[spot] = letter
        self.available_moves.remove(spot)

        print(f'{self.current_player.name}:')
        self.print_game()

        if(self.check_winner()):
            self.available_moves = []
            return False

        self.current_player = self.y_player if self.current_player == self.x_player else self.x_player
        return True
    
    def play(self):
        while len(self.available_moves) > 0:
            if(not self.make_move()):
                continue