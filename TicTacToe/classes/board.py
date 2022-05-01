""" The Game Board"""

class Board():
    """ The Board """
    board = [["-" for j in range(3)] for i in range(3)]

    def print_board(self):
        """ Print the gameboard """
        print('')
        #using the enumerate() function to print the gameboard
        for enumerated_tuple in enumerate(self.board):
            print( ' '.join(enumerated_tuple[1]))
        print('')

    def set_stone(self, symbol, row, col):
        """ Place the symbol on desired field of gameboard"""
        self.board[row][col] = symbol

    def place_is_ok(self, row, col):
        """ checks, if place is settable and in range of board"""
        try:
        # Convert it into integer
            rowint = int(row)
        except ValueError:
            return False
        try:
            colint = int(col)
        except ValueError:
            return False

        return  0 <= rowint-1 < 3 and 0 <= colint-1 < 3 and self.board[rowint-1][colint-1] == "-"

    def is_winning(self, symbol):
        """ check the possible winning options """
        three_in_a_row = self.is_winning_row(symbol)
        three_in_a_column = self.is_winning_col(symbol)
        three_in_a_diagon = self.is_winning_dia(symbol)

        return three_in_a_row or three_in_a_column or three_in_a_diagon

    def is_winning_row(self, symbol):
        """ check the rows for possible winning """
        winning_string = symbol+symbol+symbol

        if ''.join(self.board[0]) == winning_string:
            return True
        elif ''.join(self.board[1]) == winning_string:
            return True
        elif ''.join(self.board[2]) == winning_string:
            return True
        else:
            return False

    def is_winning_col(self, symbol):
        """ check the cols for possible winning """
        winning_string = symbol+symbol+symbol

        if self.board[0][0] + self.board[1][0] + self.board[2][0] == winning_string:
            return True
        elif self.board[0][1] + self.board[1][1] + self.board[2][1] == winning_string:
            return True
        elif self.board[0][2] + self.board[1][2] + self.board[2][2] == winning_string:
            return True
        else:
            return False

    def is_winning_dia(self, symbol):
        """ check the diagonals for possible winning """
        winning_string = symbol+symbol+symbol

        if self.board[0][0] + self.board[1][1] + self.board[2][2] == winning_string:
            return True
        elif self.board[0][2] + self.board[1][1] + self.board[2][0] == winning_string:
            return True
        else:
            return False
