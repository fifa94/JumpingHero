import pygame

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
icon = pygame.image.load('shield.png')
pygame.display.set_icon(icon)

# Main game cycle
running = True

while running:
    for event in pygame.event.get():
        print(event)
        # close window
        if event.type == pygame.QUIT:
            running = False

# Close of pygame window
pygame.quit()
