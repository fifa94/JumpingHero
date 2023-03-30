import pygame
import Characters
import ButtonGeneral

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

fig = Characters.CommonCharacter('aaa', 100, 100, screen)
rocketImg = pygame.image.load('Pictures/rocket.png')

play_btn = ButtonGeneral.Button(75, 200, 'Play')
quit_btn = ButtonGeneral.Button(75, 300, 'Quit')
second_btn = ButtonGeneral.Button(75, 200, 'Main menu')

# Main game cycle
running = True

back_ground = 215, 25, 25

menu_state = 'Menu'

while running:

    if menu_state == 'Menu':

        screen.fill((123, 13, 123))

        if play_btn.draw_button(screen):
            menu_state = 'Game'

        if quit_btn.draw_button(screen):
            running = False

    if menu_state == 'Game':

        # draw character
        pressed = pygame.key.get_pressed()
        fig.gravity()

        print(fig.pos_y)
        print(fig.vel_y)


        if pressed[pygame.K_SPACE]:
            # pass
            fig.move_up()
            print(fig.pos_y)
        # elif pressed[pygame.K_DOWN]:
        #     fig.move_down()
        #     print(fig.pos_y)
        # elif pressed[pygame.K_LEFT]:
        #     fig.move_left()
        #     print(fig.pos_x)
        # elif pressed[pygame.K_RIGHT]:
        #     fig.move_right()
        #     print(fig.pos_x)
        # Exit condition to menu
        elif pressed[pygame.K_ESCAPE]:
            menu_state = 'Menu'
        screen.fill((0, 0, 0))
        fig.draw()

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
