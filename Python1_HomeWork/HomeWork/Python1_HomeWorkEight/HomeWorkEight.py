from pip._vendor.distlib.compat import raw_input

from HomeWork.Python1_HomeWorkEight.Game import Game


class Menu:

    def menu(self):

        while True:
            mode = raw_input('Choose the game mode: \n1. Player vs Computer.\n2. Two players\n3. Exit game.')
            if mode not in "12" or len(mode) != 1:
                print("Error, pleas try one more time")
                continue
            elif mode == '1':
                game = Game(3)
                game.play_ai_vs_player()
            elif mode == '2':
                game = Game(3)
                game.play_player_vs_player()
            else:
                break

game = Menu()
game.menu()