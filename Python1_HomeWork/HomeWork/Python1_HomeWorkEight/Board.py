

from random import choice


class Board:
    winner_player = 'Player'
    winner_AI = 'AI'
    winner_player_one = 'Player One'
    winner_player_two = 'Player Two'
    tie = 'Tie'

    def __init__(self, size):
        self.winner = self.tie
        self.size = size
        self.matrix = []
        self.positions = []
        self.generate(size)

    def generate(self, size):
        self.matrix = [[_ for _ in range(size)] for _ in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.matrix[i][j] = '_'
                self.positions.append(str(i + 1) + str(j + 1))

    def paint(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()

    def player_position(self, position):
        self.set_position(position, 'X')

    def player_one_position(self, position):
        self.set_position(position, 'X')

    def player_two_position(self, position):
        self.set_position(position, 'O')

    def AI_position(self):
        self.set_position(choice(self.positions), 'O')

    def set_position(self, position, value):
        try:
            self.positions.index(position)
        except ValueError:
            raise ValueError

        self.matrix[int(position[:1]) - 1][int(position[1:]) - 1] = value
        self.positions.remove(position)

        if self.is_ended():
            pass

    def get_winner(self):
        return self.winner

    def is_a_tie(self):
        return self.winner == self.tie

    def is_a_player_win(self):
        return self.winner == self.winner_player

    def is_a_AI_win(self):
        return self.winner == self.winner_AI

    def is_a_player_one_win(self):
        return self.winner == self.winner_player_one

    def is_a_player_two_win(self):
        return self.winner == self.winner_player_two

    def is_ended(self):
        for i in range(0, self.size):
            if self.check_col(i, 'X') or self.check_row(i, 'X') or self.check_left_dg('X') or self.check_right_dg('X'):
                self.winner = self.winner_player
                break
            if self.check_col(i, 'O') or self.check_row(i, 'O') or self.check_left_dg('O') or self.check_right_dg('O'):
                self.winner = self.winner_AI
                break
            if self.check_col(i, 'X') or self.check_row(i, 'X') or self.check_left_dg('X') or self.check_right_dg('X'):
                self.winner = self.winner_player_one
                break
            if self.check_col(i, 'O') or self.check_row(i, 'O') or self.check_left_dg('O') or self.check_right_dg('O'):
                self.winner = self.winner_player_two
                break
        return len(self.positions) == 0 or self.winner != self.tie

    def check_col(self, column, value):
        for i in range(0, self.size):
            if self.matrix[i][column] != value:
                return False
        return True

    def check_row(self, row, value):
        for i in range(0, self.size):
            if self.matrix[row][i] != value:
                return False
        return True

    def check_left_dg(self, value):
        for i in range(0, self.size):
            if self.matrix[i][i] != value:
                return False
        return True

    def check_right_dg(self, value):
        for i in range(0, self.size):
            if self.matrix[i][self.size - i - 1] != value:
                return False
        return True
