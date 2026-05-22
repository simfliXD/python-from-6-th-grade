import sys

import numpy as np
import pygame

# Initiera pygame
pygame.init()

# Skärmens bredd och höjd
WIDTH = 600
HEIGHT = 600

# Linjernas bredd
LINE_WIDTH = 15

# Antal rader och kolumner i på brädan
bräda_rows = 3
bräda_colums = 3

# Färger
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LINE_COLOR = (0, 20, 10)

# Skapa skärmen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Sätt fönstrets titel
pygame.display.set_caption("TIC TAC TOE")
# Fyll skärmen med grön färg
screen.fill(GREEN)

# Skapa ett bräde med nollor
bräda = np.zeros((bräda_rows, bräda_colums))

# Spelarens tur
player = 1

# Spelstatus
game_over = False


def rita_linjer():
    # Rita den första horisontella linjen
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # Rita den andra horisontella linjen
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # Rita den första vertikala linjen
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # Rita den andra vertikala linjen
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def markera_ruta(row, col, player):
    # Markera en ruta på brädans med spelarens nummer
    bräda[row][col] = player


def tillgänglit_ruta(row, col):
    # Kontrollera om en ruta är tillgänglig
    if bräda[row][col] == 0:
        return True
    return False


def är_rutan_full():
    # Kontrollera om brädet är fullt
    for row in range(bräda_rows):
        for col in range(bräda_colums):
            if bräda[row][col] == 0:
                return False
    return True


def kontrollera_vinnare():
    # Kontrollera rader
    for row in range(bräda_rows):
        if bräda[row][0] == bräda[row][1] == bräda[row][2] != 0:
            return bräda[row][0]

    # Kontrollera kolumner
    for col in range(bräda_colums):
        if bräda[0][col] == bräda[1][col] == bräda[2][col] != 0:
            return bräda[0][col]

    # Kontrollera diagonaler
    if bräda[0][0] == bräda[1][1] == bräda[2][2] != 0:
        return bräda[0][0]
    if bräda[0][2] == bräda[1][1] == bräda[2][0] != 0:
        return bräda[0][2]

    # Ingen vinnare
    return 0


def rita_symboler():
    # Rita X och O på brädet
    for row in range(bräda_rows):
        for col in range(bräda_colums):
            if bräda[row][col] == 1:
                pygame.draw.line(
                    screen,
                    BLACK,
                    (col * 200 + 50, row * 200 + 50),
                    (col * 200 + 150, row * 200 + 150),
                    15,
                )
                pygame.draw.line(
                    screen,
                    BLACK,
                    (col * 200 + 150, row * 200 + 50),
                    (col * 200 + 50, row * 200 + 150),
                    15,
                )
            elif bräda[row][col] == 2:
                pygame.draw.circle(
                    screen, BLACK, (col * 200 + 100, row * 200 + 100), 60, 15
                )


def visa_vinnare(vinnare):
    # Visa vinnaren
    font = pygame.font.SysFont(None, 75)
    if vinnare == 1:
        text = font.render("Spelare 1 vinner!", True, BLACK)
    elif vinnare == 2:
        text = font.render("Spelare 2 vinner!", True, BLACK)
    else:
        text = font.render("Oavgjort!", True, BLACK)
    screen.blit(
        text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2)
    )
    pygame.display.update()
    pygame.time.wait(3000)


rita_linjer()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # X-koordinat
            mouseY = event.pos[1]  # Y-koordinat

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if tillgänglit_ruta(clicked_row, clicked_col):
                markera_ruta(clicked_row, clicked_col, player)
                if kontrollera_vinnare() != 0:
                    game_over = True
                elif är_rutan_full():
                    game_over = True
                else:
                    player = 3 - player  # Växla spelare

                rita_symboler()

    if game_over:
        vinnare = kontrollera_vinnare()
        screen.fill(GREEN)
        visa_vinnare(vinnare)

    pygame.display.update()
