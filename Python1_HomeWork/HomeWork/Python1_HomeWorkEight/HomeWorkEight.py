
import random

class Game:

    def __init__(self):
        self._field =[]
        self._size = 6
        self._player_one = 'X'
        self._player_two = 'O'
        self._AI = 'O'
        self._not_sing = '_'
        self._menu()

    def _menu(self):
        print('Game TIC TAC TOE.')
        mode = int(input('Choose the game mode: \n1. Player vs Computer.\n2. Two players\n3. Exit game.'))

        if mode == 1:
            self._AI_mode()
        elif mode == 2:
            self._two_players_mode()
        else:
            exit(1)

    def _AI_mode(self):
        pass

    def _two_players_mode(self):
        count = 0
        self._create_field()
        while True:
            self._print_field()
            x = int(input(" Player one print x"))
            y = int(input(" Player one print y"))
            self._field[x][y] = self._player_one
            count = count + 1
            if self._check_win(self, self._player_one):
                print("Player One WIN!!!")
                self._print_field()
                break
            x = int(input(" Player two print x"))
            y = int(input(" Player two print y"))
            self._field[x][y] = self._player_two
            count = count + 1
            if self._check_win(self, self._player_two):
                print("Player Two WIN!!!")
                self._print_field()
                break
            if count == random.randint(self._size, 2):
                self._print_field()
                break


    def _create_field(self):
        for i in range(self._size):
            self._field.append([])
            for j in range(self._size):
                self._field[i].append(self._not_sing)

    def _print_field(self):
        # for line in self._field:
        #     print(line)
        for i in range(len(self. _field)):
            for j in range(len(self._field[i])):
                print(self._field[i][j], end=' ')
            print()

    def _cell_is_busy(self, x, y):
        if x < 0 or y < 0 or x > self._size or y > self._size:
            return False
        return self._field[x][y] != self._not_sing

    def _check_win(self, player):
        sing = player
        #  проверка по строкам
        for i in self._size:
            if self._field[i][0] == sing and self._field[i][1] == sing and self._field[i][2] == sing:
                return True

        # проверка по столбцам
        for j in self._size:
            if self._field[0][j] == sing and self._field[1][j] == sing and self._field[2][j] == sing:
                return True

        # проверка диагоналей
        if self._field[0][0] == sing and self._field[1][1] == sing and self._field[2][2] == sing:
            return True

        if self._field[0][2] == sing and self._field[1][1] == sing and self._field[2][0] == sing:
            return True

        return False

game = Game()