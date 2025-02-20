import pygame
from menu import Menu
from game_logic import GameLogic
import sys  # Для выхода из программы

pygame.init()
display_width = 800
display_height = 600
my_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('HORROR')
FPS = 60
clock = pygame.time.Clock()

# Передача параметров в классы Menu и GameLogic
menu = Menu(my_display, clock, FPS, display_width, display_height)
game_logic = GameLogic(my_display, clock, FPS)

running = True
in_menu = True
restart_game = False  # Флаг для перезапуска игры

while running:
    if in_menu:
        result = menu.run()  # Запускаем меню
        if result == "start_game":  # Если пользователь выбрал новую игру
            in_menu = False
            restart_game = True  # Устанавливаем флаг перезапуска
        elif result == "quit":  # Если пользователь выбрал выход
            running = False
    else:
        if restart_game:
            game_logic = GameLogic(my_display, clock, FPS)  # Пересоздаем игровую логику
            restart_game = False  # Сбрасываем флаг перезапуска
        in_menu = game_logic.run()  # Запускаем игровой цикл

pygame.quit()
sys.exit()