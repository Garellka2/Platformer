import pygame
import sys  # Для выхода из программы

class Menu:
    def __init__(self, display, clock, FPS, display_width, display_height):
        self.display = display
        self.clock = clock
        self.FPS = FPS
        self.display_width = display_width
        self.display_height = display_height
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)
        self.white = (255, 255, 255)

    def run(self):
        while True:  # Бесконечный цикл для работы меню
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"  # Завершаем программу при закрытии окна
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "resume_game"  # Возвращаемся в игру
                    if event.key == pygame.K_q:
                        return "quit"  # Завершаем программу при нажатии Q
                    if event.key == pygame.K_n:
                        return "start_game"  # Переход к новой игре

            # Очистка экрана
            self.display.fill((0, 0, 0))

            # Отображение заголовка
            text = self.font.render('HORROR', True, self.white)
            self.display.blit(text, (self.display_width // 2 - 100, self.display_height // 4))

            # Отображение инструкций
            text = self.small_font.render('N - Новая игра', True, self.white)
            self.display.blit(text, (self.display_width // 2 - 120, self.display_height // 2))
            text = self.small_font.render('ESC - Вернуться в игру', True, self.white)
            self.display.blit(text, (self.display_width // 2 - 180, self.display_height // 2 + 50))
            text = self.small_font.render('Q - Выйти', True, self.white)
            self.display.blit(text, (self.display_width // 2 - 80, self.display_height // 2 + 100))

            # Обновление экрана
            pygame.display.flip()
            self.clock.tick(self.FPS)