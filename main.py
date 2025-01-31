import pygame
import sys
from player import Player
from platforms import Platform
from spikes import Spike
from key import Key
from door import Door
from levels import load_level
pygame.init()

display_width = 800
display_height= 600

spike_width = display_width / 32
spike_height = display_height / 24
platform_height = display_height / 24
platform_width = display_width / 16


my_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('HORROR')

white = (255,255,255)

FPS = 60
clock = pygame.time.Clock()

player = Player()
platforms = pygame.sprite.Group()
spikes = pygame.sprite.Group()
keys = pygame.sprite.Group()
doors = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

current_level = 1
key1, door1 = load_level(current_level,platforms,keys,doors,spikes,all_sprites,platform_height,platform_width,display_height,display_width,spike_width,spike_height)

def check_collisions():
    hits=pygame.sprite.spritecollide(player,platforms,False)
    player.on_ground = False
    for hit in hits:
        if player.vel_y > 0 and player.rect.bottom <= hit.rect.bottom:
            player.rect.bottom=hit.rect.top
            player.vel_y=0
            player.on_ground=True
        elif player.vel_x > 0 and player.rect.right > hit.rect.left and player.rect.left < hit.rect.left:
            player.rect.right = hit.rect.left
            player.vel_x = 0
        elif player.vel_x < 0 and player.rect.left < hit.rect.right and player.rect.right > hit.rect.right:
            player.rect.left = hit.rect.right
            player.vel_x = 0
        elif player.vel_y < 0 and player.rect.top < hit.rect.bottom and player.rect.bottom>hit.rect.bottom:
            player.rect.top=hit.rect.bottom
            player.vel_y=0
    if pygame.sprite.spritecollideany(player,spikes):
        reset_level()

def check_key_interaction():
    if pygame.sprite.spritecollideany(player,keys):
        if not key1.collected:
            key1.collected = True
            keys.remove(key1)

def check_door_interaction():
    if pygame.sprite.spritecollideany(player,doors):
        if key1.collected:
            door1.open_door()
            key1.reset()
            print('door is open')
            load_next_level()

def reset_level():
    global door1, key1
    player.rect.center =(10,display_height-40)
    player.vel_x = 0
    player.vel_y = 0
    key1.reset()
    if key1 not in keys:
        keys.add(key1)

def load_next_level():
    global current_level, door1, key1
    current_level += 1
    if current_level > 1:
        pygame.quit()
        sys.exit()
    else:
        key1,door1 = load_level(current_level,platforms,keys,doors,spikes,all_sprites,platform_height,platform_width,display_height,display_width,spike_width,spike_height)

running= True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    check_collisions()
    check_key_interaction()
    check_door_interaction()
    my_display.fill(white)
    keys.draw(my_display)
    doors.draw(my_display)
    all_sprites.draw(my_display)
    key1.draw_in_corner(my_display)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()