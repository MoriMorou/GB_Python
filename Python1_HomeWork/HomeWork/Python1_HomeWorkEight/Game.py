from pip._vendor.distlib.compat import raw_input

from HomeWork.Python1_HomeWorkEight.Board import Board


class Game:
    def __init__(self, size):
        print("Board size is", size)
        self.board = Board(size)

    def play_ai_vs_player(self):
        while not self.board.is_ended():
            self.board.paint()
            try:
                position = raw_input('Player, select a position: x and y\n')
                self.board.player_position(position)
                self.board.AI_position()
            except ValueError:
                print('Ops! Non-existent or occupied position. Try it again, please.')
        self.board.paint()

        if self.board.is_a_player_win():
            print('Congratulations! You win!\n')
        elif self.board.is_a_AI_win():
            print('Ooops! You lose. Smile, AI wants to win too.\n')
        else:
            print('Result: TIE!!!\n')

    def play_player_vs_player(self):
        while not self.board.is_ended():
            self.board.paint()
            try:
                position = raw_input('Player One, select a position: x and y\n')
                self.board.player_one_position(position)
                self.board.paint()
                position = raw_input('Player Two, select a position: x and y\n')
                self.board.player_two_position(position)
            except ValueError:
                print('Ops! Non-existent or occupied position. Try it again, please.')
                continue
        self.board.paint()
