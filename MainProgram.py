#from tkinter import Menu

import pygame
import ButtonGeneral

# Initialization of pygame
pygame.init()

width = 600
height = 600
name = 'Jumping Hero'

# Create window
screen = pygame.display.set_mode((width, height))

# Set window caption
pygame.display.set_caption(name)

# Load window icon
icon = pygame.image.load('Pictures/shield.png')
pygame.display.set_icon(icon)

again_btn = ButtonGeneral.Button(75, 200, 'Second menu')
quit_btn = ButtonGeneral.Button(75, 300, 'Quit')
second_btn = ButtonGeneral.Button(75, 200, 'Main menu')
# Main game cycle
running = True

back_ground = 215, 25, 25

menu_state = 'Menu'

while running:

    if menu_state == 'Menu':

        screen.fill((123, 13, 123))

        if again_btn.draw_button(screen):
            menu_state = 'SecondMenu'

        if quit_btn.draw_button(screen):
            running = False

    if menu_state == 'SecondMenu':

        screen.fill((123, 16, 13))

        if second_btn.draw_button(screen):
            menu_state = 'Menu'

        if quit_btn.draw_button(screen):
            running = False

    for event in pygame.event.get():
        print(event)
        # close window
        if event.type == pygame.QUIT:
            running = False

    # Screen update
    pygame.display.update()

# Close of pygame window
pygame.quit()
