import pygame
import random

from pygame.locals import (K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)

screen_width_ = 1500
screen_height_ = 600


class Player(pygame.sprite.Sprite):
    # defining an object to be the player, inheriting from the pygame.sprite.Sprite object
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, keys_pressed):
        if keys_pressed[K_w]:
            self.rect.move_ip((0, -6))
        if keys_pressed[K_s]:
            self.rect.move_ip((0, 6))
        if keys_pressed[K_a]:
            self.rect.move_ip((-6, 0))
        if keys_pressed[K_d]:
            self.rect.move_ip((6, 0))

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width_:
            self.rect.right = screen_width_
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height_:
            self.rect.bottom = screen_height_


class Enemy(pygame.sprite.Sprite):
    # defining an object to be enemies, inheriting from the pygame.sprite.Sprite object
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(  # initializing new enemies with a random position off the right of the screen
            center=(
                random.randint(screen_width_ + 20, screen_width_ + 100),
                random.randint(0, screen_height_)
            )
        )
        self.speed = random.randint(1, 5)

    def update(self):
        # making enemies self moving
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


