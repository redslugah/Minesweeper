import os.path
import pygame


class Cell:
    def __init__(self):
        self.clicked = False
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


def click_action(event):
    row = event.pos[1] // 20
    col = event.pos[0] // 20
    if row >= 20:
        pass
    else:
        if event.button == 1:
            board[row][col].type = RIGHT
        elif event.button == 3:
            board[row][col].type = MAYBE


def display():
    WIN.fill(GREY)
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            color = (64, 64, 64) if cell.clicked else (164, 164, 164)
            #pygame.draw.rect(WIN, color, (ix*20+1, iy*20+1, 18, 18))
            status = cell.type
            #status = WRONG if cell.clicked else START
            WIN.blit(status, (ix*20+1, iy*20+1, 18, 18))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
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