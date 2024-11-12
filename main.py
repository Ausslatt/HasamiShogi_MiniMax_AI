
from HasamiShogiGame import ShogiGame

def main():

    game = ShogiGame()
    

    game.get_square_occupant("a2")
    game.inc_red_captured()
    game.make_move("i1", "b1")
    game.make_move("i2", "a2")

    print(game.get_num_of_red_captured())


    game.show_board()



if __name__ == '__main__':
    main()