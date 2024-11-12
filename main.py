
from HasamiShogiGame import ShogiGame

def main():
    import random

    # Initialize the game
    game = ShogiGame()

    # Parameters for the Minimax depth
    minimax_depth = 3  # Adjust this for difficulty (higher values make AI more challenging but slower)

    
    game.show_board()

    while game.get_game_state() == 'UNFINISHED':
        active_player = game.get_active_player()
        print(f"\nIt's {active_player}'s turn.")

        if active_player == 'B':  # Switch active player here and line 30 to switch which color uses AI / random player
            print("AI (Black) is thinking...")
            best_move = game.best_move(minimax_depth)
            if best_move:
                origin, dest = best_move
                game.make_move(origin, dest)
                print(f"AI moves from {origin} to {dest}.")
            else:
                print("No valid moves for AI.")
        else:  
            valid_moves = game.get_all_valid_moves('R')
            if valid_moves:
                origin, dest = random.choice(valid_moves)
                game.make_move(origin, dest)
                print(f"Random Player (Red) moves from {origin} to {dest}.")
            else:
                print("No valid moves for Random Player.")

        # Show the updated board state
        game.show_board()

        # Check game state
        if game.get_game_state() != 'UNFINISHED':
            print(f"Game Over: {game.get_game_state()}")
            break

if __name__ == "__main__":
    main()
