class GameState():

    def __init__(self):

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        board_id = ""

        for i in range(len(self.board)):
            row_id = ""
            for j in range(len(self.board[i])):
                square = self.board[i][j]
                row_id += square

                if square == "wK":
                    self.white_king_location = [i, j]
                if square == "bK":
                    self.black_king_location = [i, j]

            board_id += row_id

        self.board_id = board_id

        self.white_to_move = True
        self.movelog = []

        self.is_capture = False

        self.in_check = False
        self.pins = []
        self.checks = []

        self.is_checkmate = False
        self.is_stalemate = False

        self.enpassant_possible = ()
        self.enpassant_possible_log = [self.enpassant_possible]

        self.current_castling_rights = CastlingRights(True, True, True, True)
        self.castling_rights_log = [CastlingRights(
            self.current_castling_rights.wks, self.current_castling_rights.wqs, self.current_castling_rights.bks, self.current_castling_rights.bqs)]
        self.has_castled = False

    def make_move(self, move):

        board_id = ""

        for row in self.board:
            row_id = ""
            for square in row:
                row_id += square
            board_id += row_id

        self.board_id = board_id

        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.movelog.append(move)
        self.white_to_move = not self.white_to_move

        if move.piece_moved == "wK":
            self.white_king_location = [move.end_row, move.end_col]
        elif move.piece_moved == "bK":
            self.black_king_location = [move.end_row, move.end_col]

        if move.is_promotion:
            self.board[move.end_row][move.end_col] = move.piece_moved[0] + "Q"

        if move.is_enpassant:
            self.board[move.start_row][move.end_col] = "--"

        if move.piece_moved[1] == "p" and abs(move.start_row - move.end_row) == 2:
            self.enpassant_possible = (
                ((move.start_row + move.end_row) // 2), move.start_col)
        else:
            self.enpassant_possible = ()

        if move.is_castle_move:
            if move.end_col - move.start_col == 2:
                self.board[move.end_row][move.end_col -
                                         1] = self.board[move.end_row][move.end_col + 1]
                self.board[move.end_row][move.end_col + 1] = "--"
            else:
                self.board[move.end_row][move.end_col +
                                         1] = self.board[move.end_row][move.end_col - 2]
                self.board[move.end_row][move.end_col - 2] = "--"

        self.enpassant_possible_log.append(self.enpassant_possible)

        self.update_castling_rights(move)
        self.castling_rights_log.append(CastlingRights(
            self.current_castling_rights.wks, self.current_castling_rights.wqs, self.current_castling_rights.bks, self.current_castling_rights.bqs))

        self.is_capture = (move.piece_captured == "--")

        if len(self.movelog) >= 9:
            i = len(self.movelog) - 1
            if self.movelog[i] == self.movelog[i - 4] and self.movelog[i] == self.movelog[i - 8] and self.movelog[i - 1] == self.movelog[i - 5] and self.movelog[i - 2] == self.movelog[i - 6] and self.movelog[i - 3] == self.movelog[i - 7]:
                self.is_stalemate = True

    def undo_move(self):

        board_id = ""

        for row in self.board:
            row_id = ""
            for square in row:
                row_id += square
            board_id += row_id

        self.board_id = board_id

        self.is_checkmate = False
        self.is_stalemate = False

        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

            if move.piece_moved == "wK":
                self.white_king_location = [move.start_row, move.start_col]
            elif move.piece_moved == "bK":
                self.black_king_location = [move.start_row, move.start_col]

            if move.is_enpassant:
                self.board[move.end_row][move.end_col] = "--"
                self.board[move.start_row][move.end_col] = move.piece_captured

            self.enpassant_possible_log.pop()
            self.enpassant_possible = self.enpassant_possible_log[-1]

            self.castling_rights_log.pop()
            new_rights = self.castling_rights_log[-1]
            self.current_castling_rights = CastlingRights(
                new_rights.wks, new_rights.wqs, new_rights.bks, new_rights.bqs)

            if move.is_castle_move:
                if move.end_col - move.start_col == 2:
                    self.board[move.end_row][move.end_col +
                                             1] = self.board[move.end_row][move.end_col-1]
                    self.board[move.end_row][move.end_col-1] = "--"
                else:
                    self.board[move.end_row][move.end_col -
                                             2] = self.board[move.end_row][move.end_col+1]
                    self.board[move.end_row][move.end_col+1] = "--"

    def update_castling_rights(self, move):

        if move.piece_moved == 'wK':
            self.current_castling_rights.wks = False
            self.current_castling_rights.wqs = False
        elif move.piece_moved == 'bK':
            self.current_castling_rights.bks = False
            self.current_castling_rights.bqs = False
        elif move.piece_moved == 'wR':
            if move.start_row == 7:
                if move.start_col == 0:
                    self.current_castling_rights.wqs = False
                elif move.start_col == 7:
                    self.current_castling_rights.wks = False
        elif move.piece_moved == 'bR':
            if move.start_row == 0:
                if move.start_col == 0:
                    self.current_castling_rights.bqs = False
                elif move.start_col == 7:
                    self.current_castling_rights.bks = False

        if move.piece_captured == 'wR':
            if move.end_row == 7:
                if move.end_col == 0:
                    self.current_castling_rights.wqs = False
                elif move.end_col == 7:
                    self.current_castling_rights.wks = False
        elif move.piece_captured == 'bR':
            if move.end_row == 0:
                if move.end_col == 0:
                    self.current_castling_rights.bqs = False
                elif move.end_col == 7:
                    self.current_castling_rights.bks = False

    def get_valid_moves(self):

        temp_enpassant_possible = self.enpassant_possible
        temp_castle_rights = CastlingRights(self.current_castling_rights.wks, self.current_castling_rights.wqs,
                                            self.current_castling_rights.bks, self.current_castling_rights.bqs)

        moves = []

        self.in_check, self.pins, self.checks = self.check_for_pins_and_checks()

        if self.white_to_move:

            king_row = self.white_king_location[0]
            king_col = self.white_king_location[1]

        else:

            king_row = self.black_king_location[0]
            king_col = self.black_king_location[1]

        if self.in_check:

            if len(self.checks) == 1:

                moves = self.get_possible_moves()

                check = self.checks[0]
                check_row = check[0]
                check_col = check[1]
                piece_checking = self.board[check_row][check_col]
                valid_squares = []

                if piece_checking[1] == "N":
                    valid_squares = [(check_row, check_col)]

                else:

                    for i in range(1, 8):

                        valid_square = (
                            king_row + check[2] * i, king_col + check[3] * i)
                        valid_squares.append(valid_square)

                        if valid_square[0] == check_row and valid_square[1] == check_col:
                            break

                for i in range(len(moves) - 1, -1, -1):

                    if moves[i].piece_moved[1] != "K":

                        if not (moves[i].end_row, moves[i].end_col) in valid_squares:
                            moves.remove(moves[i])

            else:
                self.get_king_moves(king_row, king_col, moves)

        else:
            moves = self.get_possible_moves()

        self.get_castle_moves(king_row, king_col, moves)

        self.enpassant_possible = temp_enpassant_possible
        self.current_castling_rights = temp_castle_rights

        if len(moves) == 0:
            if self.in_check:
                self.is_checkmate = True
            else:
                self.is_stalemate = True

        return moves

    def check_for_pins_and_checks(self):

        pins = []
        checks = []

        in_check = False

        if self.white_to_move:

            enemy_color = "b"
            ally_color = "w"

            king_start_row = self.white_king_location[0]
            king_start_col = self.white_king_location[1]

        else:

            enemy_color = "w"
            ally_color = "b"

            king_start_row = self.black_king_location[0]
            king_start_col = self.black_king_location[1]

        directions = ((-1, 0), (0, -1), (1, 0), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1))

        for j in range(len(directions)):

            d = directions[j]
            possible_pin = ()

            for i in range(1, 8):

                end_row = king_start_row + d[0] * i
                end_col = king_start_col + d[1] * i

                if 0 <= end_row < 8 and 0 <= end_col < 8:

                    end_piece = self.board[end_row][end_col]

                    if end_piece[0] == ally_color and end_piece[1] != "K":

                        if possible_pin == ():
                            possible_pin = (end_row, end_col, d[0], d[1])
                        else:
                            break

                    elif end_piece[0] == enemy_color:

                        type = end_piece[1]

                        if (0 <= j <= 3 and type == "R") or \
                                (4 <= j <= 7 and type == "B") or \
                                (i == 1 and type == "p" and ((enemy_color == "w" and 6 <= j <= 7) or (enemy_color == "b" and 4 <= j <= 5))) or \
                                (type == "Q") or (i == 1 and type == "K"):

                            if possible_pin == ():

                                in_check = True
                                checks.append((end_row, end_col, d[0], d[1]))
                                break
                            else:

                                pins.append((possible_pin))
                                break

                        else:

                            break

                else:

                    break

        knight_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1))

        for m in knight_moves:

            end_row = king_start_row + m[0]
            end_col = king_start_col + m[1]

            if 0 <= end_row < 8 and 0 <= end_col < 8:

                end_piece = self.board[end_row][end_col]

                if end_piece[0] == enemy_color and end_piece[1] == "N":

                    in_check = True
                    checks.append((end_row, end_col, m[0], m[1]))

        return in_check, pins, checks

    def square_under_attack(self, r, c):
        self.white_to_move = not self.white_to_move
        opp_moves = self.get_possible_moves()
        self.white_to_move = not self.white_to_move

        for move in opp_moves:
            if move.end_row == r and move.end_col == c:
                return True
        return False

    def get_possible_moves(self):

        moves = []

        queen_done = False
        rook_done = False
        bishop_done = False
        knight_done = False
        pawn_done = False

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if not queen_done:
                        if piece == "Q":
                            self.get_queen_moves(r, c, moves)
        queen_done = True

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if not rook_done:
                        if piece == "R":
                            self.get_rook_moves(r, c, moves)
        rook_done = True

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if not bishop_done:
                        if piece == "B":
                            self.get_bishop_moves(r, c, moves)
        bishop_done = True

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if not knight_done:
                        if piece == "N":
                            self.get_knight_moves(r, c, moves)
        knight_done = True

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if not pawn_done:
                        if piece == "p":
                            self.get_pawn_moves(r, c, moves)
        pawn_done = True

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == "K":
                        self.get_king_moves(r, c, moves)

        capture_moves = []
        good_capture_moves = []
        bad_capture_moves = []
        non_capture_moves = []

        for move in moves:
            if move.piece_captured == "--":
                non_capture_moves.append(move)
            else:
                capture_moves.append(move)

        piece_score = {"K": 0, "Q": 9, "R": 5,
                       "B": 3.001, "N": 3, "p": 1, "-": 0}

        for move in moves:
            if piece_score[move.piece_captured[1]] >= piece_score[move.piece_moved[1]]:
                good_capture_moves.append(move)
            else:
                bad_capture_moves.append(move)

        moves = good_capture_moves + bad_capture_moves

        return moves

    def get_pawn_moves(self, r, c, moves):

        piece_pinned = False
        pin_direction = ()

        for i in range(len(self.pins) - 1, -1, -1):

            if self.pins[i][0] == r and self.pins[i][1] == c:

                piece_pinned = True
                pin_direction = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])

                break

        if self.white_to_move:
            if self.board[r - 1][c] == "--":
                if not piece_pinned or pin_direction == (-1, 0):

                    moves.append(Move((r, c), (r - 1, c), self.board))

                    if r == 6 and self.board[r - 2][c] == "--":
                        moves.append(Move((r, c), (r - 2, c), self.board))

            if c - 1 >= 0:
                if self.board[r - 1][c - 1][0] == "b":
                    if not piece_pinned or pin_direction == (-1, -1):
                        moves.append(Move((r, c), (r - 1, c - 1), self.board))

                elif (r - 1, c - 1) == self.enpassant_possible:
                    if not piece_pinned or pin_direction == (-1, -1):
                        moves.append(Move((r, c), (r - 1, c - 1),
                                     self.board, is_enpassant_move=True))

            if c + 1 <= 7:
                if self.board[r - 1][c + 1][0] == "b":
                    if not piece_pinned or pin_direction == (-1, 1):
                        moves.append(Move((r, c), (r - 1, c + 1), self.board))

                elif (r - 1, c + 1) == self.enpassant_possible:
                    if not piece_pinned or pin_direction == (-1, 1):
                        moves.append(Move((r, c), (r - 1, c + 1),
                                     self.board, is_enpassant_move=True))
        else:
            if self.board[r + 1][c] == "--":
                if not piece_pinned or pin_direction == (1, 0):

                    moves.append(Move((r, c), (r + 1, c), self.board))

                    if r == 1 and self.board[r + 2][c] == "--":
                        moves.append(Move((r, c), (r + 2, c), self.board))

            if c - 1 >= 0:
                if self.board[r + 1][c - 1][0] == "w":
                    if not piece_pinned or pin_direction == (1, -1):
                        moves.append(Move((r, c), (r + 1, c - 1), self.board))

                elif (r + 1, c - 1) == self.enpassant_possible:
                    if not piece_pinned or pin_direction == (1, -1):
                        moves.append(Move((r, c), (r + 1, c - 1),
                                     self.board, is_enpassant_move=True))

            if c + 1 <= 7:
                if self.board[r + 1][c + 1][0] == "w":
                    if not piece_pinned or pin_direction == (1, 1):
                        moves.append(Move((r, c), (r + 1, c + 1), self.board))

                elif (r + 1, c + 1) == self.enpassant_possible:
                    if not piece_pinned or pin_direction == (1, 1):
                        moves.append(Move((r, c), (r + 1, c + 1),
                                     self.board, is_enpassant_move=True))

    def get_king_moves(self, r, c, moves):

        row_moves = (-1, -1, -1, 0, 0, 1, 1, 1)
        col_moves = (-1, 0, 1, -1, 1, -1, 0, 1)

        ally_color = "w" if self.white_to_move else "b"

        for i in range(8):

            end_row = r + row_moves[i]
            end_col = c + col_moves[i]

            if 0 <= end_row < 8 and 0 <= end_col < 8:

                end_piece = self.board[end_row][end_col]

                if end_piece[0] != ally_color:

                    if ally_color == "w":
                        self.white_king_location = [end_row, end_col]

                    else:
                        self.black_king_location = [end_row, end_col]

                    in_check, pins, checks = self.check_for_pins_and_checks()

                    if not in_check:
                        moves.append(
                            Move((r, c), (end_row, end_col), self.board))

                    if ally_color == "w":
                        self.white_king_location = [r, c]

                    else:
                        self.black_king_location = [r, c]

    def get_castle_moves(self, r, c, moves):

        if self.in_check:
            return
        if (self.white_to_move and self.current_castling_rights.wks) or (not self.white_to_move and self.current_castling_rights.bks):
            self.get_king_side_castle_moves(r, c, moves)
        if (self.white_to_move and self.current_castling_rights.wqs) or (not self.white_to_move and self.current_castling_rights.bqs):
            self.get_queen_side_castle_moves(r, c, moves)

    def get_king_side_castle_moves(self, r, c, moves):

        if c + 2 <= 7:
            if self.board[r][c+1] == "--" and self.board[r][c+2] == "--":
                if not self.square_under_attack(r, c+1) and not self.square_under_attack(r, c+2):
                    moves.append(
                        Move((r, c), (r, c+2), self.board, is_castle_move=True))

    def get_queen_side_castle_moves(self, r, c, moves):

        if c - 2 >= 0:
            if self.board[r][c-1] == "--" and self.board[r][c-2] == "--" and self.board[r][c-3] == "--":
                if not self.square_under_attack(r, c-1) and not self.square_under_attack(r, c-2):
                    moves.append(
                        Move((r, c), (r, c-2), self.board, is_castle_move=True))

    def get_knight_moves(self, r, c, moves):

        piece_pinned = False

        for i in range(len(self.pins) - 1, -1, -1):

            if self.pins[i][0] == r and self.pins[i][1] == c:

                piece_pinned = True
                self.pins.remove(self.pins[i])

                break

        knight_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1))
        ally_color = "w" if self.white_to_move else "b"

        for m in knight_moves:

            end_row = r + m[0]
            end_col = c + m[1]

            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if not piece_pinned:

                    end_piece = self.board[end_row][end_col]

                    if end_piece[0] != ally_color:
                        moves.append(
                            Move((r, c), (end_row, end_col), self.board))

    def get_rook_moves(self, r, c, moves):

        piece_pinned = False
        pin_direction = ()

        for i in range(len(self.pins) - 1, -1, -1):

            if self.pins[i][0] == r and self.pins[i][1] == c:

                piece_pinned = True
                pin_direction = (self.pins[i][2], self.pins[i][3])

                if self.board[r][c][1] != "Q":
                    self.pins.remove(self.pins[i])
                break

        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        enemy_color = "b" if self.white_to_move else "w"

        for d in directions:
            for i in range(1, 8):

                end_row = r + d[0] * i
                end_col = c + d[1] * i

                if 0 <= end_row < 8 and 0 <= end_col < 8:

                    if not piece_pinned or pin_direction == d or pin_direction == (-d[0], -d[1]):

                        end_piece = self.board[end_row][end_col]

                        if end_piece == "--":
                            moves.append(
                                Move((r, c), (end_row, end_col), self.board))

                        elif end_piece[0] == enemy_color and end_piece[1] != "K":
                            moves.append(
                                Move((r, c), (end_row, end_col), self.board))
                            break
                        else:
                            break

                else:
                    break

    def get_bishop_moves(self, r, c, moves):

        piece_pinned = False
        pin_direction = ()

        for i in range(len(self.pins) - 1, -1, -1):
            if self.pins[i][0] == r and self.pins[i][1] == c:

                piece_pinned = True
                pin_direction = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])

                break

        directions = ((1, 1), (-1, 1), (-1, -1), (1, -1))
        enemy_color = "b" if self.white_to_move else "w"

        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i

                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if not piece_pinned or pin_direction == d or pin_direction == (-d[0], -d[1]):
                        end_piece = self.board[end_row][end_col]
                        if end_piece == "--":
                            moves.append(
                                Move((r, c), (end_row, end_col), self.board))
                        elif end_piece[0] == enemy_color and end_piece[1] != "K":
                            moves.append(
                                Move((r, c), (end_row, end_col), self.board))
                            break
                        else:
                            break
                else:
                    break

    def get_queen_moves(self, r, c, moves):

        self.get_rook_moves(r, c, moves)
        self.get_bishop_moves(r, c, moves)


class CastlingRights():

    def __init__(self, wks, wqs, bks, bqs):
        self.wks = wks
        self.wqs = wqs
        self.bks = bks
        self.bqs = bqs


class Move():

    ranks_to_rows = {"1": 7, "2": 6, "3": 5,
                     "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2,
                     "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board, is_enpassant_move=False, is_castle_move=False):

        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]

        if 0 <= self.end_row < 8 and 0 <= self.end_col < 8:
            self.piece_moved = board[self.start_row][self.start_col]
            self.piece_captured = board[self.end_row][self.end_col]

        self.is_promotion = (self.piece_moved == "wp" and self.end_row == 0) or (
            self.piece_moved == "bp" and self.end_row == 7)

        self.is_enpassant = is_enpassant_move

        if self.is_enpassant:
            self.piece_captured = "bp" if self.piece_moved == "wp" else "wp"

        self.is_castle_move = is_castle_move

        self.move_id = self.start_row * 1000 + self.start_col * \
            100 + self.end_row * 10 + self.end_col

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
