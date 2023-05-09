import pygame
import Classes
import pygame_menu

from pygame.locals import (K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)


pygame.init()
# initialize so pygame works on any hardware
pygame.display.set_caption('Bullet_Runner_')

pygame.font.init()
my_font = pygame.font.SysFont('ocraextended', 60, bold= pygame.font.Font.bold)
text_surface = my_font.render('Bullet_Runner_', False, (50, 50, 50))

screen_width_ = 1500  # these are also in classes!!! I could link em but cba
screen_height_ = 600
screen = pygame.display.set_mode((screen_width_, screen_height_))
# set the scale of the display window

ADDENEMY = pygame.USEREVENT + 1
# custom event for adding a new enemy
pygame.time.set_timer(ADDENEMY, 150)

player = Classes.Player()
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
            new_enemy = Classes.Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    if menu.is_enabled():
        menu.mainloop(screen)

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
