from pip._vendor.distlib.compat import raw_input

from HomeWork.Python1_HomeWorkEight.Game import Game


class Menu:

    def menu(self):

        while True:
            answer = raw_input('Choose the game mode: \n1. Player vs Computer.\n2. Two players\n3. Exit game.')
            if answer not in "12" or len(answer) != 1:
                print("Error, pleas try one more time")
                continue
            elif answer == '1':
                game = Game(5)
                game.play()
            # elif answer == '2':
            #     game = Game(3)
            #     game.play()
            else:
                break

game = Menu()
game.menu()