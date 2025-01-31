import pygame

platform_color = (96,96,96)

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,platform_width,platform_height):
        super().__init__()
        self.image = pygame.Surface((platform_width,platform_height))
        self.image.fill(platform_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y