import os.path
import random

import pygame


class Cell:
    def __init__(self):
        self.clicked = False
        self.type = RIGHT
        self.checked = False
        self.clickable = True


WIDTH, HEIGHT = 400, 440
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
FILL = (111, 111, 111)
FPS = 60
ONE = pygame.image.load(os.path.join('Assets', '1.png'))
TWO = pygame.image.load(os.path.join('Assets', '2.png'))
THREE = pygame.image.load(os.path.join('Assets', '3.png'))
FOUR = pygame.image.load(os.path.join('Assets', '4.png'))
FIVE = pygame.image.load(os.path.join('Assets', '5.png'))
SIX = pygame.image.load(os.path.join('Assets', '6.png'))
SEVEN = pygame.image.load(os.path.join('Assets', '7.png'))
EIGHT = pygame.image.load(os.path.join('Assets', '8.png'))
START = pygame.image.load(os.path.join('Assets', 'open.png'))
BOMB = pygame.image.load(os.path.join('Assets', 'red.png'))
MAYBE = pygame.image.load(os.path.join('Assets', 'int.png'))
RIGHT = pygame.image.load(os.path.join('Assets', 'grey.png'))
WRONG = pygame.image.load(os.path.join('Assets', 'bomb.png'))
GENERIC = pygame.image.load(os.path.join('Assets', 'click_timer.png'))
RESTART = pygame.image.load(os.path.join('Assets', 'restart.png'))
grid_size = 20
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]
global winner
global clicked
global clicks
global gamerunning
global response


def game_restart():
    for iy, rows in enumerate(board):
        for ix, cell in enumerate(rows):
            cell.type = RIGHT
            cell.clicked = False
            cell.checked = False
    gen_field()
    global clicked
    global clicks
    global gamerunning
    global response
    gamerunning = True
    clicks = 0
    clicked = False
    response = True


def find_near(iy, ix, tipo, call):
    near = 0
    try:
        if (board[iy + 1][ix].type is tipo) and ((iy + 1) <= 19):
            near += 1
            if call == 2 and board[iy + 1][ix].clicked is False:
                board[iy + 1][ix].clicked = True
                find_near(iy + 1, ix, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy + 1][ix + 1].type is tipo) and (((ix + 1) <= 19) and (iy + 1) <= 19):
            near += 1
            if call == 2 and board[iy + 1][ix + 1].clicked is False:
                board[iy + 1][ix + 1].clicked = True
                find_near(iy + 1, ix + 1, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy][ix + 1].type is tipo) and ((ix + 1) <= 19):
            near += 1
            if call == 2 and board[iy][ix + 1].clicked is False:
                board[iy][ix + 1].clicked = True
                find_near(iy, ix + 1, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy - 1][ix].type is tipo) and ((iy - 1) >= 0):
            near += 1
            if call == 2 and board[iy - 1][ix].clicked is False:
                board[iy - 1][ix].clicked = True
                find_near(iy - 1, ix, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy - 1][ix - 1].type is tipo) and (((ix - 1) >= 0) and (iy - 1) >= 0):
            near += 1
            if call == 2 and board[iy - 1][ix - 1].clicked is False:
                board[iy - 1][ix - 1].clicked = True
                find_near(iy - 1, ix - 1, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy][ix - 1].type is tipo) and ((ix - 1) >= 0):
            near += 1
            if call == 2 and board[iy][ix - 1].clicked is False:
                board[iy][ix - 1].clicked = True
                find_near(iy, ix - 1, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy + 1][ix - 1].type is tipo) and (((iy + 1) <= 19) and (ix - 1) >= 0):
            near += 1
            if call == 2 and board[iy + 1][ix - 1].clicked is False:
                board[iy + 1][ix - 1].clicked = True
                find_near(iy + 1, ix - 1, tipo, call)
    except IndexError:
        pass
    try:
        if (board[iy - 1][ix + 1].type is tipo) and (((ix + 1) <= 19) and (iy - 1) >= 0):
            near += 1
            if call == 2 and board[iy - 1][ix + 1].clicked is False:
                board[iy - 1][ix + 1].clicked = True
                find_near(iy - 1, ix + 1, tipo, call)
    except IndexError:
        pass
    if near > 0 and call == 2:
        try:
            if iy + 1 <= 19:
                board[iy + 1][ix].clicked = True
        except IndexError:
            pass
        try:
            if iy - 1 >= 0:
                board[iy - 1][ix].clicked = True
        except IndexError:
            pass
        try:
            if ix + 1 <= 19:
                board[iy][ix + 1].clicked = True
        except IndexError:
            pass
        try:
            if ix - 1 >= 0:
                board[iy][ix - 1].clicked = True
        except IndexError:
            pass

    return near


def find_bombs():
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.type is not WRONG:
                near = find_near(iy, ix, WRONG, 1)
                match near:
                    case 1:
                        cell.type = ONE
                    case 2:
                        cell.type = TWO
                    case 3:
                        cell.type = THREE
                    case 4:
                        cell.type = FOUR
                    case 5:
                        cell.type = FIVE
                    case 6:
                        cell.type = SIX
                    case 7:
                        cell.type = SEVEN
                    case 8:
                        cell.type = EIGHT
                    case _:
                        cell.type = RIGHT


def gen_field():
    def gen_field_loop():
        rand_row = random.randrange(0, 20)
        rand_col = random.randrange(0, 20)
        if board[rand_row][rand_col].type == WRONG:
            gen_field_loop()
        else:
            board[rand_row][rand_col].type = WRONG

    for v in range(45):
        gen_field_loop()

    find_bombs()


def click_action(event):
    row = event.pos[1] // 20
    col = event.pos[0] // 20
    checkedbombs = []
    global gamerunning
    if row >= 20:
        if 440 > event.pos[1] > 400 and 280 > event.pos[0] > 120:
            game_restart()
            return True
    else:
        if event.button == 1:
            board[row][col].clicked = True
            if board[row][col].type is RIGHT:
                find_near(row, col, RIGHT, 2)
            elif board[row][col].type is WRONG:
                board[row][col].type = BOMB
                for iy, rowOfCells in enumerate(board):
                    for ix, cell in enumerate(rowOfCells):
                        if cell.type is WRONG:
                            cell.clicked = True
                return False

        elif event.button == 3:
            if board[row][col].checked:
                board[row][col].checked = False
            else:
                board[row][col].checked = True
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if not cell.clicked:
                checkedbombs.append(cell)

    if all(cell.type == WRONG for cell in checkedbombs):
        return False

    return True


def display(output):
    WIN.fill(FILL)
    WIN.blit(RESTART, (120, 400))
    WIN.blit(GENERIC, (-1, 400, 11, 3))
    WIN.blit(GENERIC, (281, 400, 118, 38))
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.clicked:
                WIN.blit(cell.type, (ix * 20 + 1, iy * 20 + 1, 18, 18))
            elif cell.checked:
                WIN.blit(MAYBE, (ix * 20 + 1, iy * 20 + 1, 18, 18))
            else:
                WIN.blit(START, (ix * 20 + 1, iy * 20 + 1, 18, 18))
    font_game = pygame.font.SysFont("Arial", 25)
    font = pygame.font.Font.render(font_game, output, False, pygame.Color((255, 0, 0)))
    label = pygame.font.Font.render(font_game, str(clicks), False, (255, 0, 0))
    restart = pygame.font.Font.render(font_game, 'RESTART', False, (255, 0, 0))
    WIN.blit(restart, (145, 407))
    WIN.blit(label, (330, 407))
    WIN.blit(font, (3, 407))

    pygame.display.update()


def main():
    global response
    response = True
    global gamerunning
    gamerunning = True
    start_tick = pygame.time.get_ticks()
    pygame.init()
    pygame.font.init()
    global clicked
    clicked = False
    clock = pygame.time.Clock()
    run = True
    gen_field()
    clock.tick(FPS)
    global clicks
    clicks = 0
    global winner
    winner = 0
    while run:
        if not clicked:
            start_tick = pygame.time.get_ticks()

        ticks = pygame.time.get_ticks()
        millis = (ticks - start_tick) % 1000
        seconds = int((ticks - start_tick) / 1000 % 60)
        minutes = int((ticks - start_tick) / 60000 % 24)
        output = '{minutes:02d}:{seconds:02d}:{millis:02d}'.format(minutes=minutes, seconds=seconds, millis=millis)
        if gamerunning:
            display(output)
            gamerunning = response

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                if event.pos[1] // 20 >= 20:
                    click_action(event)
                else:
                    clicks += 1
                    response = click_action(event)
                    clicked = True
            elif event.type == pygame.MOUSEBUTTONDOWN and clicked:
                if event.pos[1] // 20 >= 20:
                    gamerunning = click_action(event)
                else:
                    clicks += 1
                    response = click_action(event)


    pygame.quit()


if __name__ == "__main__":
    main()
