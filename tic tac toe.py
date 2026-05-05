import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
bräd_row = 3
bräd_col = 3

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LINE_COLOR = (0, 20, 10)

screen = pygame.display.set_mode ( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( GREEN )

bräda = np.zeros( (bräd_row, bräd_col) )

def rita_linjer():
    # första liggande linje
    pygame.draw.line( screen, LINE_COLOR, (0,200), (600, 200), LINE_WIDTH )
    # andra liggande linje
    pygame.draw.line( screen, LINE_COLOR, (0,400), (600, 400), LINE_WIDTH )
    # första stående linje
    pygame.draw.line( screen, LINE_COLOR, (200,0), (200, 600), LINE_WIDTH )
    # andra stäende linje
    pygame.draw.line( screen, LINE_COLOR, (400,0), (400, 600), LINE_WIDTH )

def markera_ruta(row, col, player):
    bräda[row][col] = player

def tillgänglit_ruta(row, col):
    if bräda[row][col] == 0


def är_rutan_full():
    for row in range(bräd_row):
        for col in range(bräd_col):
            if board[row][col] == 0:
                return False
    return True

rita_linjer()

for row in range(bräd_row):
        for col in range(bräd_col):
            markera_ruta( row, col, 1 )
print(är_rutan_full

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
