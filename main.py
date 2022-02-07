"""
This is a tic-tac-toe game.
"""
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