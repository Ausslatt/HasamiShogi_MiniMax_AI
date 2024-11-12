
import random
import copy

class ShogiGame:



    def __init__(self):
        """
        A 2D list representing the game board. The first element of each row is the row label, and the first element of each column is the column label. Game pieces are
        represented by 'R' for red pieces and 'B' for black pieces. Empty squares are denoted by '.'. Turn counter is initialized to 0, even numbers indicate it is Black's turn and odd is Red.
        A space on the board is represented by its row letter and column number index, space "a1" is the first red piece at the top left of a new board. A board's space_map allows easy conversion from alphabetical
        row labels to the corresponding index.
        """
        self._game_state = 'UNFINISHED'
        self._turn = 0
        self._num_of_red_captured = 0
        self._num_of_black_captured = 0
        self._active_player = self.get_active_player()
        self._board = [[" ", '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                       ['a', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                       ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['c', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['d', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['e', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['f', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['g', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['h', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['i', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        self.space_map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9}
        
     


    def show_board(self):
        for i in self._board: # prints a board to terminal.
            print(*i)

    def get_num_captured_pieces(self, color):
        if color == 'R':
            return self.get_num_of_red_captured()
        else:
            return self.get_num_of_black_captured()

    def get_game_state(self):
        return self._game_state

    def get_active_player(self):
        if self._turn % 2 == 0:
            return 'B'

        else:
            return 'R'

    def set_game_state(self, state):
        self._game_state = state

    def set_turn(self):
        self._turn += 1

    def get_num_of_red_captured(self):
        return self._num_of_red_captured

    def get_num_of_black_captured(self):
        return self._num_of_black_captured

    def inc_red_captured(self):
        self._num_of_red_captured += 1

    def inc_black_captured(self):
        self._num_of_black_captured += 1

    def _is_horizontal(self, origin, dest):
        if origin[0] == dest[0]:
            return True
        else:
            return False

    def _is_vertical(self, origin, dest):
        if origin[1] == dest[1]:
            return True
        else:
            return False

    def get_square_occupant(self, square):
        """
        Returns the piece occupying a square on the board. Validates that the square is on the board.
        
        @param square: a string representing a square on the board.
        @return: the piece occupying the square.

        """
        if not self.validate_square(square):
            return None
        
        row = self.space_map[square[0]] # row number from our space_map
        column = int(square[1]) # column number
        return self._board[row][column]
        
    def validate_square(self, square):
        """
        Checks if a square is on the board.

        @param square: a string representing a square on the board. 
        @return: True if the square is on the board, False otherwise.

        """
        rows = "abcdefghi"
        columns = "123456789"

        if square[0] not in rows or square[1] not in columns:
            Print("Square not on board")
            return False
        
        return True
    
    def set_square_occupant(self, square, piece=None):
        if piece is None:
            piece = '.'

        row = self.space_map[square[0]]
        col = int(square[1])

        self._board[row][col] = piece



    def _move_piece(self, origin, dest):

        """
        Moves a piece from one square to another. Validates that the path is clear and that the move is either horizontal or vertical.

        @param origin: a string representing the square the piece is moving from.
        @param dest: a string representing the square the piece is moving to.
        @param piece: a string representing the piece being moved. If None, the piece at the origin square is moved.
        """
        
        piece = self.get_square_occupant(origin)

        # if self.get_active_player() != self.get_square_occupant(origin):
        #     return False

        if origin == dest:
            print("You must move atleast one square.")
            return None
        
        if piece == '.': # if there is no piece to move
            print("No piece to move!")
            return None

        elif not self.validate_square(origin):
            Print("Square Not on Board")
            return None

        elif self.is_path_clear(self.get_path(origin, dest)):
        
            dest_row = self.space_map[dest[0]]
            
            dest_column = int(dest[1])

            origin_row = self.space_map[origin[0]]
            origin_column = int(origin[1])
            self._board[dest_row][dest_column] = piece
            self._board[origin_row][origin_column] = '.'



    def get_path(self, origin, dest):

        """
        Returns the path between two squares on the board. Validates that the move is either horizontal or vertical.

        @param origin: a string representing the square the piece is moving from.
        @param dest: a string representing the square the piece is moving to.
        @return: a list of the squares between the origin and destination squares.

        """
        
        if not (self.validate_square(origin) and self.validate_square(dest)):
                print("You're attempting to move off the board.")

        row1 = self.space_map[origin[0]]
        row2 = self.space_map[dest[0]]
        col1 = int(origin[1])
        col2 = int(dest[1])

        
        if self._is_horizontal(origin, dest):
            
            path = self._board[self.space_map[origin[0]]][col1 + 1:col2 + 1]

            return path
        
        elif self._is_vertical(origin, dest):
            path = [self._board[i][col1] for i in range(row1 + 1, row2 + 1)]
            return path
        
        else:
            print("your move is not horizontal or vertical")
            return None


    def is_path_clear(self, path):

        """
        Checks if the path between two squares is clear. 
        @param: Array of chars representing the path.
        @return: True if the path is clear, False otherwise.

        """

        if 'B' in path or 'R' in path:
            return False
        else:
            return True

    def check_captures(self, dest, direction):
        """
        Generalized method to check for captures in a specified direction.

        @param dest: The destination square where the move ends.
        @param direction: A tuple (row_offset, col_offset) representing the direction to check for captures.
        """
        capture_sequences = {
            'R': [['B', 'R'], ['B', 'B', 'R'], ['B', 'B', 'B', 'R'], ['B', 'B', 'B', 'B', 'R'], 
                    ['B', 'B', 'B', 'B', 'B', 'R'], ['B', 'B', 'B', 'B', 'B', 'B', 'R'], 
                    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'R']],
            'B': [['R', 'B'], ['R', 'R', 'B'], ['R', 'R', 'R', 'B'], ['R', 'R', 'R', 'R', 'B'], 
                    ['R', 'R', 'R', 'R', 'R', 'B'], ['R', 'R', 'R', 'R', 'R', 'R', 'B'], 
                    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']]
        }

        occupant = self.get_square_occupant(dest)
        if occupant not in ['R', 'B']:
            return  # No captures to check if no valid occupant

        capture_seq = capture_sequences[occupant]
        captured_count_increment = self.inc_red_captured if occupant == 'B' else self.inc_black_captured

        row, col = self.space_map[dest[0]], int(dest[1])
        captured_pieces = []
        seq = []

        # Traverse in the specified direction to check for capture sequences
        while True:
            row += direction[0]
            col += direction[1]
            if row < 1 or row > 9 or col < 1 or col > 9:
                break  # Stop if out of bounds
            current_piece = self._board[row][col]
            seq.append(current_piece)

            for capture_pattern in capture_seq:
                if seq == capture_pattern:
                    # Capture the pieces in this sequence
                    for i, piece in enumerate(capture_pattern):
                        capture_row = row - i * direction[0]
                        capture_col = col - i * direction[1]
                        if self._board[capture_row][capture_col] != occupant and self._board[capture_row][capture_col] != '.':
                            self._board[capture_row][capture_col] = '.'
                            captured_count_increment()

                    return  # Exit after capturing to avoid further redundant checks

    def check_corner_captures(self, dest):
        """
        Generalized method to check for captures at corners based on specific corner sequences.
        The corners checked are top-left, top-right, bottom-left, and bottom-right.
        
        @param dest: The destination square where the move ends.
        """
        occupant = self.get_square_occupant(dest)
        if occupant not in ['R', 'B']:
            return  # No captures to check if no valid occupant

        opponent = 'R' if occupant == 'B' else 'B'
        captured_count_increment = self.inc_red_captured if occupant == 'B' else self.inc_black_captured

        # Define corner positions and their relevant sequences
        corners = {
            'topright': [('a8', 'b9', 'a9')],
            'topleft': [('a2', 'b1', 'a1')],
            'bottomright': [('i8', 'h9', 'i9')],
            'bottomleft': [('h1', 'i2', 'i1')]
        }

        for corner, positions in corners.items():
            if dest in [positions[0][0], positions[0][1]]:
                # Check the corner sequence
                if (self.get_square_occupant(positions[0][0]) == occupant and
                    self.get_square_occupant(positions[0][1]) == occupant and
                    self.get_square_occupant(positions[0][2]) == opponent):
                    # Capture the opponent piece
                    self.set_square_occupant(positions[0][2])
                    captured_count_increment()


    def make_move(self, origin, dest):

        self._move_piece(origin, dest)

        # Check left capture
        self.check_captures(dest, direction=(0, -1))

        # Check right capture
        self.check_captures(dest, direction=(0, 1))

        # Check upward capture
        self.check_captures(dest, direction=(-1, 0))

        # Check downward capture
        self.check_captures(dest, direction=(1, 0))

        self.check_corner_captures(dest)

        if self.get_num_of_black_captured() >= 8:
            self.set_game_state("RED WINS:GAME OVER")
            print(self.get_game_state())
        
        elif self.get_num_of_red_captured() >= 8:
            self.set_game_state("BLACK WINS:GAME OVER")
            print(self.get_game_state())

        self.set_turn()
        self._active_player = self.get_active_player()

        

        return True




    def make_random_move(self):
            """
            Generates and makes a random move for the active player.
            """
            valid_moves = self.get_all_valid_moves(self._active_player)
            if valid_moves:
                origin, dest = random.choice(valid_moves)
                print(f"Random Player {self._active_player} moves from {origin} to {dest}")
                self.make_move(origin, dest)
            else:
                print(f"No valid moves available for {self._active_player}")

    def get_all_valid_moves(self, player):
        """
        Finds all valid horizontal and vertical moves for the current player.
        @param player: 'R' or 'B' representing the current active player.
        @return: A list of tuples (origin, destination) representing valid moves.
        """
        valid_moves = []
        
        for row_index in range(1, 10):  # Rows a-i (1 to 9 in indexing)
            for col_index in range(1, 10):  # Columns 1-9
                origin = chr(96 + row_index) + str(col_index)  # Convert to board notation
                if self.get_square_occupant(origin) == player:
                    
                    # Find valid horizontal moves (left and right)
                    for offset in [-1, 1]:  # -1 for left, +1 for right
                        current_col = col_index + offset
                        while 1 <= current_col <= 9:
                            dest = chr(96 + row_index) + str(current_col)
                            if self.get_square_occupant(dest) == '.':  # Empty square
                                if self.is_path_clear(self.get_path(origin, dest)):
                                    valid_moves.append((origin, dest))
                            else:
                                break  # Stop searching if path is blocked
                            current_col += offset

                    # Find valid vertical moves (up and down)
                    for offset in [-1, 1]:  # -1 for up, +1 for down
                        current_row = row_index + offset
                        while 1 <= current_row <= 9:
                            dest = chr(96 + current_row) + str(col_index)
                            if self.get_square_occupant(dest) == '.':  # Empty square
                                if self.is_path_clear(self.get_path(origin, dest)):
                                    valid_moves.append((origin, dest))
                            else:
                                break  # Stop searching if path is blocked
                            current_row += offset

        return valid_moves





    def minimax(self, game_copy, depth, is_maximizing_player):
        """
        Implements the Minimax algorithm on a copy of the game object to find the best move.
        
        @param game_copy: A copy of the ShogiGame object.
        @param depth: The depth to which the game tree is explored.
        @param is_maximizing_player: True if it's the maximizing player's (AI) turn, False if minimizing player's turn.
        @return: The best score for the current game state.
        """
        if depth == 0 or game_copy.get_game_state() != 'UNFINISHED':
            return game_copy.evaluate_board()

        if is_maximizing_player:
            max_eval = float('-inf')
            valid_moves = game_copy.get_all_valid_moves(game_copy._active_player)
            for move in valid_moves:
                origin, dest = move
                # Create a deep copy of the game object
                new_game_copy = copy.deepcopy(game_copy)
                # Make the move on the copied game object
                new_game_copy.make_move(origin, dest)
                eval = self.minimax(new_game_copy, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            opponent = 'R' if game_copy._active_player == 'B' else 'B'
            valid_moves = game_copy.get_all_valid_moves(opponent)
            for move in valid_moves:
                origin, dest = move
                # Create a deep copy of the game object
                new_game_copy = copy.deepcopy(game_copy)
                # Make the move on the copied game object
                new_game_copy.make_move(origin, dest)
                eval = self.minimax(new_game_copy, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, depth):
        """
        Finds the best move for the AI player using the Minimax algorithm with a copied game object.
        @param depth: The depth to which the game tree is explored.
        @return: The best move (origin, destination).
        """
        best_val = float('-inf')
        best_move = None
        valid_moves = self.get_all_valid_moves(self._active_player)
        for move in valid_moves:
            origin, dest = move
            # Create a deep copy of the game object
            game_copy = copy.deepcopy(self)
            # Make the move on the copied game object
            game_copy.make_move(origin, dest)
            move_val = self.minimax(game_copy, depth - 1, False)
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move


    def evaluate_board(self):
        """
        Evaluates the current board state to determine the score.
        @return: The score of the current board state.
        """
        return self.get_num_of_black_captured() - self.get_num_of_red_captured()
