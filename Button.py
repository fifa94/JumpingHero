import pygame
from pygame.locals import *

class Button:
    # Define colors
    text_color = 255, 255, 255
    hover_color = 255, 255, 255
    WIDTH = 140
    LENGTH = 50
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self, screen):
        action = False
        click = False
        position = pygame.mouse.get_pos()
        # create pygame rect object
        button_rect = Rect(self.x, self.y, self.WIDTH, self.LENGTH)

        if button_rect.collidepoint(position) == 1:
            if pygame.mouse.get_pressed()[0] == 1:
                    click = True
                    pygame.draw.rect(screen, self.hover_color, button_rect)
                    action = True
            elif:
            else:
