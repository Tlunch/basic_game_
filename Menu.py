import pygame
import pygame_menu

pygame.init()

screen_width_ = 1500
screen_height_ = 600
surface = pygame.display.set_mode((screen_width_, screen_height_))
# initializing pygame


def start_game():
    global menu
    import Bullet_Runner_
    menu.disable()
    pass


menu = pygame_menu.Menu('Welcome', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Start', start_game())

menu.mainloop(surface)
