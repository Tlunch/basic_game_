import pygame
import random

from pygame.locals import (K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)


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


pygame.init()
# initialize so pygame works on any hardware
pygame.display.set_caption('Bullet_Runner_')

pygame.font.init()
my_font = pygame.font.SysFont('ocraextended', 60, bold= pygame.font.Font.bold)
text_surface = my_font.render('Bullet_Runner_', False, (50, 50, 50))

screen_width_ = 1500
screen_height_ = 600
screen = pygame.display.set_mode((screen_width_, screen_height_))
# set the scale of the display window

ADDENEMY = pygame.USEREVENT + 1
# custom event for adding a new enemy
pygame.time.set_timer(ADDENEMY, 150)

player = Player()
# initialize the player

enemies = pygame.sprite.Group()
# creating a sprite group for enemies to go into
all_sprites = pygame.sprite.Group()
# creating a sprite group for all sprites to be rendered to go in
all_sprites.add(player)

clock = pygame.time.Clock()
running = True
# set up before the gameloop

while running:
    # this is the main gameloop, this will run while the game runs

    for event in pygame.event.get():
        # handles the event queue

        if event.type == QUIT:
            running = False
        # this quits the game if the [x] is hit

        if event.type == KEYDOWN:
            # handles the key press events

            if event.key == K_ESCAPE:
                running = False
            # this quits the game if esc is hit

        if event.type == ADDENEMY:
            # when the add enemy event is called create a new enemy class object
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    keys_pressed_ = pygame.key.get_pressed()
    # return a dictionary of currently pressed keys

    player.update(keys_pressed_)
    # calls the update argument defined above. this updates player.surf.rect

    enemies.update()
    # update the position of all enemies in the sprite group enemies

    screen.fill((0, 0, 0))
    # colour the screen

    #    surf = pygame.Surface((50, 50))
    #    surf.fill((255, 0, 0))
    #    rect = surf.get_rect()
    # creates a surface, colours it red and stores the underlying rectangle object

    pygame.draw.circle(screen, (255, 100, 120), (250, screen_height_/2),110)
    screen.blit(text_surface, (250, screen_height_/2))
    # draw an object

    # screen.blit(player.surf, player.rect)
    # block transfer the surf surface to the screen surface

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    # looping through all entities and block transferring them on to the screen

    if pygame.sprite.spritecollideany(player, enemies):
        # checks if any sprite in the enemies group is colliding with the player sprite and ends the game
        player.kill()
        running = False
    pygame.display.flip()
    # update the changes to the screen

    clock.tick(250)

pygame.quit()
# cleanly closes the game
