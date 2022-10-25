import os.path
import random

import pygame


class Cell:
    def __init__(self):
        self.clicked = True
        self.type = START


pygame.init()
WIDTH, HEIGHT = 400, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
GREY = (111, 111, 111)
FPS = 60
ONE = pygame.image.load(os.path.join('Assets', '1.png'))
TWO = pygame.image.load(os.path.join('Assets', '2.png'))
THREE = pygame.image.load(os.path.join('Assets', '3.png'))
FOUR = pygame.image.load(os.path.join('Assets', '4.png'))
FIVE = pygame.image.load(os.path.join('Assets', '5.png'))
SIX = pygame.image.load(os.path.join('Assets', '6.png'))
SEVEN = pygame.image.load(os.path.join('Assets', '7.png'))
EIGHT = pygame.image.load(os.path.join('Assets', '8.png'))
RIGHT = pygame.image.load(os.path.join('Assets', 'open.png'))
WRONG = pygame.image.load(os.path.join('Assets', 'red.png'))
MAYBE = pygame.image.load(os.path.join('Assets', 'int.png'))
START = pygame.image.load(os.path.join('Assets', 'grey.png'))
grid_size = 20
board = [[Cell() for _ in range(grid_size)] for _ in range(grid_size)]


def find_bombs():
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.type is not WRONG:
                near = 0
                try:
                    if (board[iy + 1][ix].type is WRONG) and ((iy + 1) <= 19):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy + 1][ix + 1].type is WRONG) and (((ix + 1) <= 19) and (iy + 1) <= 19):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy][ix + 1].type is WRONG) and ((ix + 1) <= 19):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy - 1][ix].type is WRONG) and ((iy - 1) >= 0):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy - 1][ix - 1].type is WRONG) and (((ix - 1) >= 0) and (iy - 1) >= 0):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy][ix - 1].type is WRONG) and ((ix - 1) >= 0):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy + 1][ix - 1].type is WRONG) and (((iy + 1) <= 19) and (ix - 1) >= 0):
                        near += 1
                except IndexError:
                    pass
                try:
                    if (board[iy - 1][ix + 1].type is WRONG) and (((ix + 1) <= 19) and (iy - 1) >= 0):
                        near += 1
                except IndexError:
                    pass

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

def gen_field():
    def gen_field_loop():
        rand_row = random.randrange(0, 20)
        rand_col = random.randrange(0, 20)
        if board[rand_row][rand_col].type == WRONG:
            gen_field_loop()
        else:
            board[rand_row][rand_col].type = WRONG

    for v in range(42):
        gen_field_loop()

    find_bombs()


def click_action(event):
    row = event.pos[1] // 20
    col = event.pos[0] // 20
    if row >= 20:
        pass
    else:
        if event.button == 1:
            board[row][col].clicked = True
        elif event.button == 3:
            if board[row][col].type is START:
                board[row][col].type = MAYBE
            elif board[row][col].type is MAYBE:
                board[row][col].type = START


def display():
    WIN.fill(GREY)
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.clicked:
                WIN.blit(cell.type, (ix*20+1, iy*20+1, 18, 18))
            else:
                WIN.blit(RIGHT, (ix * 20 + 1, iy * 20 + 1, 18, 18))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    gen_field()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_action(event)
        display()

    pygame.quit()


if __name__ == "__main__":
    main()