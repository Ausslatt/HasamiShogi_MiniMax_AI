
class ShogiGame:

    def __init__(self):
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

    def show_board(self):
        for i in self._board:
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
            return 'BLACK'

        elif self._turn % 2 != 0:
            return 'RED'

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

    def get_square_occupant(self, square):
        for i in self._board:
            if i[0] == square[0]:
                if i[int(square[1])] == 'R':
                    return "RED"

                elif i[int(square[1])] == 'B':
                    return "BLACK"
                else:
                    return '.'

    def set_square_occupant(self, square, piece=None):
        if piece is None:
            piece = '.'

        for i in self._board:
            if i[0] == square[0]:
                i[int(square[1])] = piece

    def _move_piece(self, origin, dest, piece=None):
        if self.get_square_occupant(origin) == 'RED':
            piece = 'R'

        if self.get_square_occupant(origin) == 'BLACK':
            piece = 'B'

        for i in self._board:

            if i[0] == dest[0]:
                i[int(dest[1])] = piece

            if i[0] == origin[0]:
                i[int(origin[1])] = '.'

    def _is_horizontal(self, origin, dest):
        if origin[0] == dest[0]:
            return True

    def _is_vertical(self, origin, dest):
        if origin[1] == dest[1]:
            return True

    def get_horizontal_path(self, origin, dest):
        if origin[0] == dest[0]:
            for i in self._board:
                if i[0] == origin[0] == dest[0]:

                    if int(origin[1]) < int(dest[1]):
                        path = []
                        for k in range(int(origin[1]) + 1, int(dest[1]) + 1):
                            path.append(i[k])
                        return path

                    elif int(origin[1]) > int(dest[1]):
                        path = []
                        for k in range(int(dest[1]), int(origin[1])):
                            path.append(i[k])
                        return path
        else:
            return 'not horizontal'

    def get_vertical_path(self, origin, dest):
        if origin[1] == dest[1]:
            path = []
            for i in self._board:

                if origin[0] < dest[0]:
                    if origin[0] < i[0] <= dest[0]:
                        path.append(i[int(origin[1])])

                if origin[0] > dest[0]:
                    if dest[0] <= i[0] < origin[0]:
                        path.append(i[int(origin[1])])
            return path
        else:
            return 'not vertical'

    def is_path_clear(self, origin, dest):
        for i in self.get_vertical_path(origin, dest):
            if i == 'B' or i == 'R':
                return False
        for i in self.get_horizontal_path(origin, dest):
            if i == 'B' or i == 'R':
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
