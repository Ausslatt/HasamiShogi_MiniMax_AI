
from HasamiShogiGame import ShogiGame

def main():

    game = ShogiGame()
    game._move_piece("e1", "c1")
    game.show_board()




if __name__ == '__main__':
    main()