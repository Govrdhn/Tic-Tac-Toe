from random import choice

class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

# computer player
class ComputerPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)
    
    def get_move(self, game):
        opponent_letter = 'o' if self.letter == 'x' else 'x'
        final_spot = None
        spots = [i for i in range(game.size**2)]

        # possible combinations for winning
        winning_paths = [sub for i in range(game.size) for sub in (spots[i*game.size:(i+1)*game.size], spots[i : : game.size])]
        winning_paths.append(spots[0 : : game.size+1])
        winning_paths.append(spots[game.size-1 : -1 : game.size-1])
        preferred_path = None

        # paths with available spots
        for path in winning_paths:
            if(len(set(path) & set(game.available_moves)) > 0):
                preferred_path = path

        # for path with empty spots, oppponents letter and not containing self.letter
        for path in winning_paths:
            spots_in_path = [game.spots[i] for i in path]
            spots_in_preferred_path = [game.spots[i] for i in preferred_path]
            if(len(set(path) & set(game.available_moves)) > 0):
                if(spots_in_path.count(opponent_letter) > spots_in_preferred_path.count(opponent_letter)):
                    if(self.letter not in spots_in_path):
                        preferred_path = path

        # for path with empty spots, self.letter and not with opponent's letter
        for path in winning_paths:
            spots_in_path = [game.spots[i] for i in path]
            spots_in_preferred_path = [game.spots[i] for i in preferred_path]
            if(set(path) <= set(game.available_moves) or (opponent_letter not in spots_in_path)):
                if(spots_in_path.count(self.letter) > spots_in_preferred_path.count(self.letter)):
                    if(spots_in_path.count(self.letter) >= spots_in_preferred_path.count(opponent_letter)):
                        preferred_path = path

        final_spot = choice(list(set(preferred_path) & set(game.available_moves)))
        return final_spot

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