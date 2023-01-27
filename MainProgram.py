import pygame
import Characters

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

# Pygame clock - FPS
clock = pygame.time.Clock()
FPS = 30
x = 30
y = 30
# Main game cycle
running = True
fig = Characters.CommonCharacter('aaa', 100, 100, screen)
rocketImg = pygame.image.load('Pictures/rocket.png')
while running:

    for event in pygame.event.get():
        print(event)
        # close window
        if event.type == pygame.QUIT:
            running = False


    # draw character
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        # pass
        fig.move_up()
        print(fig.pos_y)
    elif pressed[pygame.K_DOWN]:
        fig.move_down()
        print(fig.pos_y)
    elif pressed[pygame.K_LEFT]:
        fig.move_left()
        print(fig.pos_x)
    elif pressed[pygame.K_RIGHT]:
        fig.move_right()
        print(fig.pos_x)

    screen.fill((0, 0, 0))
    fig.draw()

    pygame.display.flip()
    clock.tick(FPS)


# Close of pygame window
pygame.quit()
