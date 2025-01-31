import pygame


key_color =(255,239,0)

class Key(pygame.sprite.Sprite):
    def __init__(self,x,y,key_width= 25,key_height=15):
        super().__init__()
        self.image = pygame.Surface((key_width,key_height),pygame.SRCALPHA)
        pygame.draw.rect(self.image,key_color,(0,0,key_width,key_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        self.collected = False
    
    def draw_in_corner(self,screen):
        if self.collected:
            screen.blit(self.image,(10,10))
    
    def reset(self):
        self.collected = False
        self.rect.x = self.start_x
        self.rect.y = self.start_y