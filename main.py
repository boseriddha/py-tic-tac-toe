"""
This is a tic-tac-toe game.
"""
import time
from player import Player, HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        # this is the main game board
        self.board = self.make_board()
        # this is the attribute holding the winner of a game instance
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for i in range(9)]

    @staticmethod
    def print_nums_board():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        return moves

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
                return True
        return False

    def check_winner(self, square, letter):
        # check the row
        row_index = square // 3
        row = [self.board[row_index*3 + i] for i in range(3)]
        if all([spot == letter for spot in row]):
            return True

        # check column
        column_index = square % 3
        column = [self.board[column_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in range(0, 9, 4)]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in range(2, 7, 2)]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

# main function to play the game
def play(game: TicTacToe, x_player: Player, o_player: Player, print_game=True):
    if print_game:
        game.print_nums_board()

    # uppercase letters only
    letter = 'X'

    while game.empty_squares():
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # making the move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')
            # checking the winner
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
            letter = 'O' if letter == 'X' else 'X'
        # delay for the computer
        time.sleep(.8)

        # condition for no winner
        if print_game:
            print('It\'s a tie!')

# driver code
if __name__ == "__main__":
    t = TicTacToe()
    print("Enter a choice:")
    print('Player X:')
    val1 = input('1. Human Player\n2. Computer Player')
    print('Player O:')
    val2 = input('1. Human Player\n2. Computer Player')
    if val1 == 1:
        x_player = HumanPlayer('X')
    else:
        x_player = ComputerPlayer('X')

    if val2 == 1:
        o_player = HumanPlayer('O')
    else:
        o_player = ComputerPlayer('O')

    play(t, x_player, o_player, print_game=True)