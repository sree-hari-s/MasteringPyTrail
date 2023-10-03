import random

piece_score = {"K": 0, "Q": 90, "R": 50, "B": 40, "N": 30, "p": 10}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

knight_score = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]


bishop_score = [[4, 3, 2, 1, 1, 2, 3, 4],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [4, 3, 2, 1, 1, 2, 3, 4]]

queen_score = [[1, 1, 1, 3, 1, 1, 1, 1],
               [1, 2, 3, 3, 3, 1, 1, 1],
               [1, 4, 3, 3, 3, 4, 2, 1],
               [1, 2, 3, 3, 3, 2, 2, 1],
               [1, 2, 3, 3, 3, 2, 2, 1],
               [1, 4, 3, 3, 3, 4, 2, 1],
               [1, 2, 3, 3, 3, 1, 1, 1],
               [1, 1, 1, 3, 1, 1, 1, 1]]

rook_score = [[4, 3, 4, 4, 4, 4, 3, 4],
              [4, 4, 4, 4, 4, 4, 4, 4],
              [1, 1, 2, 3, 3, 2, 1, 1],
              [1, 2, 3, 4, 4, 3, 2, 1],
              [1, 2, 3, 4, 4, 3, 2, 1],
              [1, 1, 2, 3, 3, 2, 1, 1],
              [4, 4, 4, 4, 4, 4, 4, 4],
              [4, 3, 4, 4, 4, 4, 3, 4]]

white_pawn_score = [[8, 8, 8, 8, 8, 8, 8, 8],
                    [8, 8, 8, 8, 8, 8, 8, 8],
                    [5, 6, 6, 7, 7, 6, 6, 5],
                    [2, 3, 3, 5, 5, 3, 3, 2],
                    [1, 2, 3, 4, 4, 3, 2, 1],
                    [1, 1, 1, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

black_pawn_score = [[0, 0, 0, 0, 0, 0, 0, 0],

                    [1, 1, 1, 0, 0, 1, 1, 1],
                    [1, 2, 3, 4, 4, 3, 2, 1],
                    [2, 3, 3, 5, 5, 3, 3, 2],
                    [5, 6, 6, 7, 7, 6, 6, 5],
                    [8, 8, 8, 8, 8, 8, 8, 8],
                    [8, 8, 8, 8, 8, 8, 8, 8]]


piece_position_scores = {"N": knight_score, "Q": queen_score, "R": rook_score,
                         "B": bishop_score, "bp": black_pawn_score, "wp": white_pawn_score}


def find_random_move(valid_moves):

    return random.choice(valid_moves)


def find_best_move(gs, valid_moves, returnQueue):

    global next_move, counter, current_score

    next_move = None
    counter = 0

    find_negamax_move_alpha_beta_pruning(gs, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.white_to_move else -1)

    print(f'No. of moves calculated: {counter}')

    if next_move is None:
        print("No move found :/")

    returnQueue.put(next_move)


def find_negamax_move_alpha_beta_pruning(gs, valid_moves, depth, alpha, beta, turn_multiplier):

    global next_move, counter, current_score

    current_score = 0

    if depth == 0:
        current_score = turn_multiplier * get_score_board(gs)
        return turn_multiplier * get_score_board(gs)

    max_score = -CHECKMATE

    for move in valid_moves:

        gs.make_move(move)

        next_moves = gs.get_valid_moves()

        score = 0

        dist_bw_kings = (((gs.white_king_location[0] - gs.black_king_location[0]) ** 2) + (
            (gs.white_king_location[1] - gs.black_king_location[1]) ** 2)) ** 0.5

        if len(gs.movelog) > 50:
            score -= turn_multiplier * len(gs.movelog) * 0.001 * dist_bw_kings * \
                (-0.01 if current_score < 0 else 0.01)

        score += turn_multiplier * (0.01 if gs.in_check else 0)

        score += turn_multiplier * (1 if move.is_castle_move else 0)

        counter += 1

        score += -find_negamax_move_alpha_beta_pruning(
            gs, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)

        if score > max_score:
            max_score = score

            if depth == DEPTH:
                next_move = move

        gs.undo_move()

        if max_score > alpha:
            alpha = max_score

        if alpha >= beta:
            break

    current_score = turn_multiplier * max_score

    return max_score


def get_score_board(gs):

    global current_score

    if gs.is_checkmate:

        if gs.white_to_move:
            return -CHECKMATE
        else:
            return CHECKMATE

    elif gs.is_stalemate:
        return CHECKMATE * (-1 if current_score < 0 else 1)

    score = 0

    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):

            square = gs.board[row][col]

            if square != "--":

                piece_position_score = 0

                if square[1] != "K":

                    if square[1] == "p":
                        piece_position_score = piece_position_scores[square][row][col]
                    else:
                        piece_position_score = piece_position_scores[square[1]][row][col]

                if square[0] == "w":
                    score += piece_score[square[1]] + \
                        piece_position_score * 0.05
                else:
                    score -= piece_score[square[1]] + \
                        piece_position_score * 0.05

    return score
