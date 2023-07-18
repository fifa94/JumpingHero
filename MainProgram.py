import pygame
import Characters
import ButtonGeneral
import GameEngine

# Initialization of pygame
pygame.init()

width = 600
height = 600
name = 'Jumping Hero'

# Create window
screen = pygame.display.set_mode((width, height))
surf = pygame.Surface((width, height))

# Set window caption
pygame.display.set_caption(name)

# Load window icon
icon = pygame.image.load('Pictures/shield.png')
pygame.display.set_icon(icon)

# Pygame clock-FPS
clock = pygame.time.Clock()
FPS = 30
x = 30
y = 30


menu_background = pygame.image.load('Pictures/meadow-game-background.jpg')
game_background = pygame.image.load('Pictures/meadow-game-background.jpg')


play_btn = ButtonGeneral.Button(225, 200, 'Play')
quit_btn = ButtonGeneral.Button(225, 300, 'Quit')
second_btn = ButtonGeneral.Button(225, 200, 'Main menu')

game_runtime = GameEngine.Game(pygame, screen, game_background)

# Main game cycle
running = True

back_ground = 215, 25, 25

menu_state = 'Menu'

while running:

    # main menu screen
    if menu_state == 'Menu':

        # Main menu with its background. Position x0, y0.
        screen.blit(menu_background, (0, 0))

        if play_btn.draw_button(screen):
            menu_state = 'Game'

        if quit_btn.draw_button(screen):
            running = False

    # running game screen
    if menu_state == 'Game':
        out = game_runtime.running()

        menu_state = out[0]
        running = out[1]

    # pygame process
    for event in pygame.event.get():
        print(event)
        # close window
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

    # Screen update
    pygame.display.update()

# Close of pygame window
pygame.quit()
