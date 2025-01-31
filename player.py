import pygame

player_width = 50
player_height = 50
player_color = (51,255,255)

display_width = 800
display_height= 600
gravity = 1
jump_strength = 15
player_speed = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_width,player_height))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.center = (0,display_height-player_height)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
    
    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel_x = -player_speed
        elif keys[pygame.K_d]:
            self.vel_x = player_speed
        else:
            self.vel_x = 0
        
        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = - jump_strength
            self.on_ground = False

        self.vel_y+=gravity
        if self.vel_y > 20 :
            self.vel_y = 20

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


        if self.rect.right > display_width:
            self.rect.right = display_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >=display_height:
            self.rect.bottom = display_height
            self.vel_y = 0
            self.on_ground = True

        
        
        


