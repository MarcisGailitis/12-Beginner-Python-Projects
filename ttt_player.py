import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move, given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get the square based on minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # define max player yourself and other_player
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # we should return position AND score, as we need to keep track of the score for the min to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            # each score should maximize, (be larger)
            best = {'position': None, 'score': -math.inf}
        else:
            # if other player's turn, minimize as small as possible
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step1: make a move try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            # now we alternate players
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            # otherwise this will going to be messed up from recursion
            sim_score['position'] = possible_move

            # step 4: update dict, if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8): ')
            # we are going to check that this is a correct value by trying to cast
            # it to an intiger and if it is not, then we say it is invalid
            # if that spot is not available on the board, then it is also not valid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
