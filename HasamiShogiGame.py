
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
        if color == 'RED':
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
        
        """
        Assigns a space on the board to the given piece. Validates that the square is on the board.

        @param square: a string representing a square on the board. 
        @param piece: a string representing a game piece.

        """
        if piece is None:
            piece = '.'

        if not self.validate_square(square):
            return None
        
        row = self.space_map[square[0]]
        column = int(square[1])
        self._board[row][column] = piece

    def _move_piece(self, origin, dest):

        """
        Moves a piece from one square to another. Validates that the path is clear and that the move is either horizontal or vertical.

        @param origin: a string representing the square the piece is moving from.
        @param dest: a string representing the square the piece is moving to.
        @param piece: a string representing the piece being moved. If None, the piece at the origin square is moved.
        """
        
        piece = self.get_square_occupant(origin)
        
        if piece == '.': # if there is no piece to move
            print("No piece to move!")
            return None

        if self.is_path_clear(origin, dest):
            self.set_square_occupant(origin)
            self.set_square_occupant(dest, piece)

        else:
            print("Invalid Path!")


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


    def is_path_clear(self, origin, dest):

        """
        Checks if the path between two squares is clear. 
        @param origin: a string representing the square the piece is moving from.
        @param dest: a string representing the square the piece is moving to.
        @return: True if the path is clear, False otherwise.

        """
   
        
        if self.get_path(origin, dest) is None:
            return False
        
        path = self.get_path(origin, dest)

        if 'B' in path or 'R' in path:
            return False
        else:
            return True

    def _check_rhs_captures(self, dest):

        if self.get_square_occupant(dest) == 'BLACK':
            capture_seq = [['R', 'B'],
                           ['R', 'R', 'B'],
                           ['R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']
                           ]
        elif self.get_square_occupant(dest) == 'RED':
            capture_seq = [['B', 'R'],
                           ['B', 'B', 'R'],
                           ['B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'R']
                           ]

        for i in self._board:
            if i[0] == dest[0]:
                segment = i[int(dest[1]) + 1::]
                seq = []
                for k in segment:
                    seq.append(k)
                    for j in capture_seq:
                        if seq == j:
                            index = 0
                            for g in seq:

                                if self.get_square_occupant(dest) == 'BLACK':
                                    if g != 'B' and g != '.':
                                        index += 1
                                        i[int(dest[1]) + index] = '.'
                                        self.inc_red_captured()

                                elif self.get_square_occupant(dest) == 'RED':
                                    if g != 'R' and g != '.':
                                        index += 1
                                        i[int(dest[1]) + index] = '.'
                                        self.inc_black_captured()

    def _check_lhs_captures(self, dest, capture_seq=None):

        if self.get_square_occupant(dest) == 'BLACK':
            capture_seq = [['R', 'B'],
                           ['R', 'R', 'B'],
                           ['R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']
                           ]
        elif self.get_square_occupant(dest) == 'RED':
            capture_seq = [['B', 'R'],
                           ['B', 'B', 'R'],
                           ['B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'R']
                           ]

        for i in self._board:
            if i[0] == dest[0]:
                segment = i[:int(dest[1])]
                segment.reverse()
                segment.pop()
                seq = []
                for k in segment:
                    seq.append(k)
                    for j in capture_seq:
                        if seq == j:
                            index = 0
                            for g in seq:

                                if self.get_square_occupant(dest) == 'BLACK':
                                    if g != 'B' and g != '.':
                                        index += 1
                                        i[int(dest[1]) - index] = '.'
                                        self.inc_red_captured()

                                elif self.get_square_occupant(dest) == 'RED':
                                    if g != 'R' and g != '.':
                                        index += 1
                                        i[int(dest[1]) - index] = '.'
                                        self.inc_black_captured()

    def _check_up_captures(self, dest):
        if self.get_square_occupant(dest) == 'BLACK':
            capture_seq = [['R', 'B'],
                           ['R', 'R', 'B'],
                           ['R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']
                           ]
        elif self.get_square_occupant(dest) == 'RED':
            capture_seq = [['B', 'R'],
                           ['B', 'B', 'R'],
                           ['B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'R']
                           ]
        for i in self._board:
            if i[0] == dest[0]:
                segment = [i[int(dest[1])] for i in self._board if i[0] < dest[0]]
                segment.reverse()
                segment.pop()
                seq = []
                for k in segment:
                    seq.append(k)
                    for j in capture_seq:
                        if seq == j:
                            row = chr(ord(dest[0]) - 1)
                            index = dest[1]
                            sqr = row + index

                            for g in seq:

                                if self.get_square_occupant(dest) == 'BLACK':

                                    if g != 'B' and g != '.':
                                        self.set_square_occupant(sqr)
                                        self.inc_red_captured()
                                        row = chr(ord(row) - 1)
                                        sqr = row + index

                                elif self.get_square_occupant(dest) == 'RED':

                                    if g != 'R' and g != '.':
                                        self.set_square_occupant(sqr)
                                        self.inc_black_captured()
                                        row = chr(ord(row) - 1)
                                        sqr = row + index

    def _check_down_captures(self, dest):
        if self.get_square_occupant(dest) == 'BLACK':
            capture_seq = [['R', 'B'],
                           ['R', 'R', 'B'],
                           ['R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'B'],
                           ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']
                           ]
        elif self.get_square_occupant(dest) == 'RED':
            capture_seq = [['B', 'R'],
                           ['B', 'B', 'R'],
                           ['B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'R'],
                           ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'R']
                           ]
        for i in self._board:
            if i[0] == dest[0]:
                segment = [i[int(dest[1])] for i in self._board if i[0] > dest[0]]
                seq = []
                for k in segment:
                    seq.append(k)
                    for j in capture_seq:
                        if seq == j:
                            row = chr(ord(dest[0]) + 1)
                            index = dest[1]
                            sqr = row + index
                            for g in seq:

                                if self.get_square_occupant(dest) == 'BLACK':
                                    if g != 'B' and g != '.':
                                        self.set_square_occupant(sqr)
                                        self.inc_red_captured()
                                        row = chr(ord(row) + 1)
                                        sqr = row + index

                                elif self.get_square_occupant(dest) == 'RED':
                                    if g != 'R' and g != '.':
                                        self.set_square_occupant(sqr)
                                        self.inc_black_captured()
                                        row = chr(ord(row) + 1)
                                        sqr = row + index

    def _check_topright(self, dest):
        if self.get_square_occupant(dest) == 'RED':
            if dest == 'a8' or dest == 'b9':
                if self.get_square_occupant('a8') == 'RED' and self.get_square_occupant('b9') == 'RED':
                    if self.get_square_occupant('a9') == 'BLACK':
                        self.set_square_occupant('a9')
                        self.inc_black_captured()
        elif self.get_square_occupant(dest) == 'BLACK':
            if dest == 'a8' or dest == 'b9':
                if self.get_square_occupant('a8') == 'BLACK' and self.get_square_occupant('b9') == 'BLACK':
                    if self.get_square_occupant('a9') == 'RED':
                        self.set_square_occupant('a9')
                        self.inc_red_captured()

    def _check_topleft(self, dest):
        if self.get_square_occupant(dest) == 'RED':
            if dest == 'b1' or dest == 'a2':
                if self.get_square_occupant('b1') == 'RED' and self.get_square_occupant('a2') == 'RED':
                    if self.get_square_occupant('a1') == 'BLACK':
                        self.set_square_occupant('a1')
                        self.inc_black_captured()
        elif self.get_square_occupant(dest) == 'BLACK':
            if dest == 'b1' or dest == 'a2':
                if self.get_square_occupant('a2') == 'BLACK' and self.get_square_occupant('b1') == 'BLACK':
                    if self.get_square_occupant('a1') == 'RED':
                        self.set_square_occupant('a1')
                        self.inc_red_captured()

    def _check_bottomleft(self, dest):
        if self.get_square_occupant(dest) == 'RED':
            if dest == 'h1' or dest == 'i2':
                if self.get_square_occupant('h1') == 'RED' and self.get_square_occupant('i2') == 'RED':
                    if self.get_square_occupant('i1') == 'BLACK':
                        self.set_square_occupant('i1')
                        self.inc_black_captured()
        elif self.get_square_occupant(dest) == 'BLACK':
            if dest == 'h1' or dest == 'i2':
                if self.get_square_occupant('h1') == 'BLACK' and self.get_square_occupant('i2') == 'BLACK':
                    if self.get_square_occupant('i1') == 'RED':
                        self.set_square_occupant('i1')
                        self.inc_red_captured()

    def _check_bottomright(self, dest):
        if self.get_square_occupant(dest) == 'RED':
            if dest == 'i8' or dest == 'h9':
                if self.get_square_occupant('i8') == 'RED' and self.get_square_occupant('h9') == 'RED':
                    if self.get_square_occupant('i9') == 'BLACK':
                        self.set_square_occupant('i9')
                        self.inc_black_captured()
        elif self.get_square_occupant(dest) == 'BLACK':
            if dest == 'i8' or dest == 'h9':
                if self.get_square_occupant('i8') == 'BLACK' and self.get_square_occupant('h9') == 'BLACK':
                    if self.get_square_occupant('i9') == 'RED':
                        self.set_square_occupant('i9')
                        self.inc_red_captured()


    def make_move(self, origin, dest):

        if origin == dest:
            return False

        if self.get_game_state() == 'BLACK_WON' or self.get_game_state() == 'RED_WON':
            return False

        if self.get_active_player() != self.get_square_occupant(origin):
            return False

        if self.get_square_occupant(origin) == '.':
            return False

        if not (self._is_vertical(origin, dest) or self._is_horizontal(origin, dest)):
            return False

        if self.is_path_clear(origin, dest):
            self._move_piece(origin, dest)
            self._check_lhs_captures(dest)
            self._check_rhs_captures(dest)
            self._check_up_captures(dest)
            self._check_down_captures(dest)
            self._check_topright(dest)
            if dest in ['a2', 'b1', 'a8', 'b9', 'h9', 'i8', 'h1', 'i2']:
                self._check_topright(dest)
                self._check_topleft(dest)
                self._check_bottomleft(dest)
                self._check_bottomright(dest)
            if self.get_num_of_red_captured() >= 8:
                self.set_game_state('BLACK_WON')
            if self.get_num_of_black_captured() >= 8:
                self.set_game_state('RED_WON')

            self.set_turn()

            return True
