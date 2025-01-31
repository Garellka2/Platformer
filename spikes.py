import pygame

spikes_color =(199,0,0)

class Spike(pygame.sprite.Sprite):
    def __init__(self,x,y,spike_width,spike_height):
        super().__init__()
        self.image = pygame.image.load('assets/spike.jpg')
        self.image = pygame.transform.scale(self.image,(spike_width,spike_height))
        #self.image = pygame.Surface((spike_width,spike_height),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        point1 = (0,spike_height)
        point2 = (spike_width/2,0)
        point3 = (spike_width,spike_height)
        #pygame.draw.polygon(self.image,spikes_color,[point1,point2,point3])