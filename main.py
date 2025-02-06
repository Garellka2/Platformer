import pygame
import sys
from menu import Menu
#from game_logic import GameLogic




pygame.init()

display_width = 800
display_height= 600


my_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('HORROR')


FPS = 60
clock = pygame.time.Clock()

menu = Menu(my_display,clock,FPS,display_width,display_height)
#game_logic = GameLogic(my_display,clock,FPS)

running = True
in_menu = True
restart_game = False

while running:
    if in_menu:
        result = menu.run()
        if result == 'start_game':
            in_menu = False
            restart_game = True
        elif result == 'quit':
            running = False
    else:
        if restart_game:
            #game_logic = GameLogic(my_display,clock,FPS)
            restart_game = False
        #in_menu = game_logic.run()
    

pygame.quit()
sys.exit()