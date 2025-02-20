import pygame
from player import Player
from platforms import Platform
from spikes import Spike
from key import Key
from door import Door
from load_level import load_level

class GameLogic:
    def __init__(self, display, clock, FPS):
        self.display = display
        self.clock = clock
        self.FPS = FPS
        self.white = (255, 255, 255)
        self.display_width = 800
        self.display_height = 600

        self.player = Player()
        self.platforms = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.current_level = 1
        self.key1, self.door1 = load_level(self.current_level, self.platforms, self.keys, self.doors, self.spikes, self.all_sprites, self.display_height / 24, self.display_width / 16, self.display_height, self.display_width, self.display_width / 32, self.display_height / 24)

    def check_collisions(self):
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        self.player.on_ground = False
        for hit in hits:
            if self.player.vel_y > 0 and self.player.rect.bottom <= hit.rect.bottom:
                self.player.rect.bottom = hit.rect.top
                self.player.vel_y = 0
                self.player.on_ground = True
            elif self.player.vel_x > 0 and self.player.rect.right > hit.rect.left and self.player.rect.left < hit.rect.left:
                self.player.rect.right = hit.rect.left
                self.player.vel_x = 0
            elif self.player.vel_x < 0 and self.player.rect.left < hit.rect.right and self.player.rect.right > hit.rect.right:
                self.player.rect.left = hit.rect.right
                self.player.vel_x = 0
            elif self.player.vel_y < 0 and self.player.rect.top < hit.rect.bottom and self.player.rect.bottom > hit.rect.bottom:
                self.player.rect.top = hit.rect.bottom
                self.player.vel_y = 0
        if pygame.sprite.spritecollideany(self.player, self.spikes):
            self.reset_level()

    def check_key_interaction(self):
        if pygame.sprite.spritecollideany(self.player, self.keys):
            if not self.key1.collected:
                self.key1.collected = True
                self.keys.remove(self.key1)

    def check_door_interaction(self):
        if pygame.sprite.spritecollideany(self.player, self.doors):
            if self.key1.collected:
                self.door1.open_door()
                self.key1.reset()
                print('door is open')
                self.load_next_level()

    def reset_level(self):
        self.player.rect.center = (10, self.display_height - 40)
        self.player.vel_x = 0
        self.player.vel_y = 0
        self.key1.reset()
        if self.key1 not in self.keys:
            self.keys.add(self.key1)

    def load_next_level(self):
        self.current_level += 1
        if self.current_level > 1:
            pygame.quit()
            sys.exit()
        else:
            self.key1, self.door1 = load_level(self.current_level, self.platforms, self.keys, self.doors, self.spikes, self.all_sprites, self.display_height / 24, self.display_width / 16, self.display_height, self.display_width, self.display_width / 32, self.display_height / 24)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True

            self.all_sprites.update()
            self.check_collisions()
            self.check_key_interaction()
            self.check_door_interaction()
            self.display.fill(self.white)
            self.keys.draw(self.display)
            self.doors.draw(self.display)
            self.all_sprites.draw(self.display)
            self.key1.draw_in_corner(self.display)
            pygame.display.flip()
            self.clock.tick(self.FPS)

        return False