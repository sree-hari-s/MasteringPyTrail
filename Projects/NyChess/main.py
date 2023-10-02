import pygame as p
import ChessEngine
import ChessBrain
import sys
import os
from multiprocessing import Queue, Process


p.init()
WIDTH = 800
HEIGHT = 800
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def load_images():

    pieces = ["bR", "bN", "bB", "bQ", "bK",
              "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]

    for piece in pieces:

        IMAGES[piece] = p.image.load(resource_path(f'{piece}.png')).convert_alpha()
        IMAGES[piece] = p.transform.scale(IMAGES[piece], (SQ_SIZE, SQ_SIZE))


def main():

    global flipped

    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("NyChess")
    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    valid_moves = gs.get_valid_moves()
    move_made = False
    animate = False

    move_sound = p.mixer.Sound(resource_path('move.wav'))
    capture_sound = p.mixer.Sound(resource_path('capture.wav'))

    load_images()
    running = True
    sq_selected = ()
    player_clicks = []
    game_over = True
    game_start = False
    move_undone = False

    white_human = True
    black_human = True
    human_turn = True

    ai_thinking = False
    move_finder_process = None

    flipped = 0

    while running:

        if not game_start:
            screen.fill(p.Color("Black"))
            font = p.font.SysFont("Helvetica", 72, True, False)
            text_object = font.render("NyChess", True, p.Color("White"))
            text_location = p.Rect(0, 0, WIDTH, HEIGHT).move(
                WIDTH / 2 - text_object.get_width() / 2, HEIGHT / 2 - text_object.get_height() / 2 - 200)
            screen.blit(text_object, text_location)

            menu_mouse_pos = p.mouse.get_pos()

            white_vs_ai_button = Button(pos=(WIDTH / 2, (HEIGHT / 2) * 1.2), text_input="White v/s AI", font=p.font.SysFont(
                "Helvetica", 48, True, False), base_color=p.Color("White"), hovering_color=p.Color("Grey"))

            white_vs_ai_button.changeColor(menu_mouse_pos)
            white_vs_ai_button.update(screen)

            black_vs_ai_button = Button(pos=(WIDTH / 2, (HEIGHT / 2) * 1.4), text_input="Black v/s AI", font=p.font.SysFont(
                "Helvetica", 48, True, False), base_color=p.Color("White"), hovering_color=p.Color("Grey"))

            black_vs_ai_button.changeColor(menu_mouse_pos)
            black_vs_ai_button.update(screen)

            play_friend = Button(pos=(WIDTH / 2, (HEIGHT / 2) * 1), text_input="P v/s P", font=p.font.SysFont(
                "Helvetica", 48, True, False), base_color=p.Color("White"), hovering_color=p.Color("Grey"))

            play_friend.changeColor(menu_mouse_pos)
            play_friend.update(screen)

        human_turn = (gs.white_to_move and white_human) or (not gs.white_to_move and black_human)

        for e in p.event.get():

            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:

                if not game_start:
                    if white_vs_ai_button.checkForInput(menu_mouse_pos):
                        white_human = True
                        black_human = False
                        flipped = 0
                        game_over = False
                        game_start = True

                    elif black_vs_ai_button.checkForInput(menu_mouse_pos):
                        white_human = False
                        black_human = True
                        flipped = 7
                        game_over = False
                        game_start = True
                        human_turn = False

                    elif play_friend.checkForInput(menu_mouse_pos):
                        white_human = True
                        black_human = True
                        flipped = 0
                        game_over = False
                        game_start = True

                if not game_over:

                    location = p.mouse.get_pos()
                    col = (location[0]) // SQ_SIZE
                    row = location[1] // SQ_SIZE

                    if 0 <= row and row <= 7 and 0 <= col and col <= 7:
                        sq_selected = (abs(row - flipped), abs(col - flipped))
                        player_clicks.append(sq_selected)
                    else:
                        sq_selected = ()
                        player_clicks = []

                    if len(player_clicks) == 2 and human_turn:
                        move = ChessEngine.Move(
                            player_clicks[0], player_clicks[1], gs.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                if white_human and black_human:
                                    flipped = 7 if flipped == 0 else 0
                                gs.make_move(valid_moves[i])
                                move_made = True
                                sq_selected = ()
                                player_clicks = []
                                animate = True

                        if not move_made:
                            player_clicks = [sq_selected]

            elif e.type == p.KEYDOWN:

                if e.key == p.K_m and game_start:
                    flipped = 0
                    game_start = False
                    gs = ChessEngine.GameState()
                    valid_moves = gs.get_valid_moves()
                    player_clicks = []
                    sq_selected = ()
                    move_made = False
                    animate = False
                    game_over = True
                    if ai_thinking:
                        move_finder_process.terminate()
                        ai_thinking = False
                    move_undone = False

                if e.key == p.K_s:
                    game_start = True

                if e.key == p.K_f:
                    if flipped == 0:
                        flipped = 7
                    else:
                        flipped = 0

                if e.key == p.K_z:
                    if (not white_human and black_human) or (white_human and not black_human):
                        if white_human and gs.white_to_move:
                            gs.undo_move()
                            gs.undo_move()
                        elif white_human and not gs.white_to_move:
                            gs.undo_move()
                        elif black_human and not gs.white_to_move:
                            gs.undo_move()
                            gs.undo_move()
                        else:
                            gs.undo_move()
                    else:
                        if len(gs.movelog) > 0:
                            flipped = 7 if flipped == 0 else 0
                        gs.undo_move()
                    animate = False
                    move_made = True
                    game_over = False
                    if ai_thinking:
                        move_finder_process.terminate()
                        ai_thinking = False
                    move_undone = True

                if e.key == p.K_r:
                    gs = ChessEngine.GameState()
                    valid_moves = gs.get_valid_moves()
                    player_clicks = []
                    sq_selected = ()
                    move_made = False
                    animate = False
                    game_over = False
                    if ai_thinking:
                        move_finder_process.terminate()
                        ai_thinking = False
                    move_undone = False
                    if (not white_human and black_human):
                        flipped = 7
                    else:
                        flipped = 0

        if not game_over and not human_turn and not move_undone:

            if not ai_thinking:
                ai_thinking = True
                returnQueue = Queue() 
                move_finder_process = Process(target=ChessBrain.find_best_move, args=(gs, valid_moves, returnQueue))
                move_finder_process.start()
            
            if not move_finder_process.is_alive():
                ai_move = returnQueue.get()
                if ai_move is None:
                    ai_move = ChessBrain.find_random_move(valid_moves)
                gs.make_move(ai_move)
                move_made = True
                animate = True
                ai_thinking = False
                sq_selected = ()
                player_clicks = []

        if move_made:

            if len(gs.movelog) > 0:
                if gs.is_capture:
                    move_sound.play()
                else:
                    capture_sound.play()

            if animate:
                animate_move(gs.movelog[-1], screen, gs.board, clock)
            valid_moves = gs.get_valid_moves()
            move_made = False
            animate = False
            move_undone = False

        if game_start:
            draw_gamestate(screen, gs, valid_moves, sq_selected)

        if gs.is_stalemate:

            game_over = True
            s = p.Surface((WIDTH, HEIGHT))
            s.set_alpha(200)
            s.fill(p.Color("Black"))
            screen.blit(s, (0, 0))
            draw_text(screen, "Draw", p.Color("White"))

        elif gs.is_checkmate:

            game_over = True
            s = p.Surface((WIDTH, HEIGHT))
            s.set_alpha(200)
            s.fill(p.Color("Black"))
            screen.blit(s, (0, 0))
            if not gs.white_to_move:
                draw_text(screen, "White Wins", p.Color("White"))
            else:
                draw_text(screen, "Black Wins", p.Color("White"))

        clock.tick(MAX_FPS)
        p.display.flip()


def highlight_squares(screen, gs, valid_moves, sq_selected):

    s = p.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(200)
    s.fill(p.Color("yellow"))
    if len(gs.movelog) != 0:
        screen.blit(s, ((abs(gs.movelog[-1].start_col - flipped) * SQ_SIZE), abs(
            gs.movelog[-1].start_row - flipped) * SQ_SIZE))
        screen.blit(s, ((abs(gs.movelog[-1].end_col - flipped) * SQ_SIZE), abs(
            gs.movelog[-1].end_row - flipped) * SQ_SIZE))

        if gs.in_check:
            s.fill(p.Color("red"))
            if gs.white_to_move:
                    screen.blit(s, ((abs(gs.white_king_location[1] - flipped) * SQ_SIZE), abs(
                        gs.white_king_location[0] - flipped) * SQ_SIZE))
            else:
                    screen.blit(s, ((abs(gs.black_king_location[1] - flipped) * SQ_SIZE), abs(
                        gs.black_king_location[0] - flipped) * SQ_SIZE))

    if sq_selected != ():
        r, c = sq_selected
        if gs.board[r][c][0] == ("w" if gs.white_to_move else "b"):
            s.fill(p.Color("#4b739a"))
            screen.blit(s, ((abs(c - flipped) * SQ_SIZE),
                        abs(r - flipped) * SQ_SIZE))
            s.fill(p.Color("Light Blue"))
            for move in valid_moves:
                if move.start_row == r and move.start_col == c:
                    screen.blit(s, ((abs(move.end_col - flipped) * SQ_SIZE),
                                abs(move.end_row - flipped) * SQ_SIZE))


def draw_gamestate(screen, gs, valid_moves, sq_selected):

    draw_board(screen)
    highlight_squares(screen, gs, valid_moves, sq_selected)
    draw_pieces(screen, gs.board)


def draw_board(screen):

    global colors
    colors = [p.Color("#EBECD0"), p.Color("#779556")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(
                (c * SQ_SIZE), r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):

    for r in range(DIMENSION):
        for c in range(DIMENSION):

            piece = board[abs(r - flipped)][abs(c - flipped)]

            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(
                    (c * SQ_SIZE), r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def animate_move(move, screen, board, clock):

    global colors
    dR = move.end_row - move.start_row
    dC = move.end_col - move.start_col
    frames_per_square = 5
    frame_count = (abs(dR) + abs(dC)) * frames_per_square
    for frame in range(frame_count + 1):
        r, c = (move.start_row + dR*frame/frame_count,
                move.start_col + dC*frame/frame_count)
        draw_board(screen)
        draw_pieces(screen, board)

        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect((abs(move.end_col - flipped) * SQ_SIZE),
                            abs(move.end_row - flipped) * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, end_square)

        if move.piece_captured != "--":

            if move.is_enpassant:

                enpassant_row = move.end_row + \
                    1 if move.piece_captured[0] == "b" else move.end_row - 1
                end_square = p.Rect((abs(move.end_col - flipped) * SQ_SIZE),
                                    abs(enpassant_row - flipped) * SQ_SIZE, SQ_SIZE, SQ_SIZE)

            screen.blit(IMAGES[move.piece_captured], end_square)

        screen.blit(IMAGES[move.piece_moved], p.Rect(
            (abs(c - flipped) * SQ_SIZE), abs(r - flipped) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)


def draw_text(screen, text, color):

    font = p.font.SysFont("Helvetica", 48, True, False)
    text_object = font.render(text, 1, color)
    text_location = p.Rect(0, 0, WIDTH, HEIGHT).move(
        WIDTH / 2 - text_object.get_width() / 2, HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)


class Button():
    def __init__(self, pos, text_input, font, base_color, hovering_color, image=None):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        if self.image is None:
            self.rect = self.text_rect
        else:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)


if __name__ == "__main__":

    main()
