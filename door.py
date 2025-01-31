import pygame


door_color =(151,60,7)
open_door_color = (57,156,255)

class Door(pygame.sprite.Sprite):
    def __init__(self,x,y,door_width= 50,door_height=100):
        super().__init__()
        self.image = pygame.Surface((door_width,door_height),pygame.SRCALPHA)
        pygame.draw.rect(self.image,door_color,(0,0,door_width,door_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_open = False
    
    def open_door(self):
        self.is_open = True
        self.image.fill(open_door_color)
        