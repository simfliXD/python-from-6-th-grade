from main_menu_funktions import Game
from spel_kod import *
g = Game()

while g.running:
    g.game_loop()
    g.curr_menu.display_menu()