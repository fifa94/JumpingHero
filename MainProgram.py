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
rocketImg = pygame.image.load('Pictures/hero_01.png')
menu_background = pygame.image.load('Pictures/meadow-game-background.jpg')

play_btn = ButtonGeneral.Button(225, 200, 'Play')
quit_btn = ButtonGeneral.Button(225, 300, 'Quit')
second_btn = ButtonGeneral.Button(225, 200, 'Main menu')

# Main game cycle
running = True

back_ground = 215, 25, 25

menu_state = 'Menu'

while running:

    if menu_state == 'Menu':

        # Main menu with its background. Position x0, y0.
        screen.blit(menu_background, (0, 0))

        if play_btn.draw_button(screen):
            menu_state = 'Game'

        if quit_btn.draw_button(screen):
            running = False

    if menu_state == 'Game':

        # draw character
        pressed = pygame.key.get_pressed()
        keys_pressed = pygame.event.get()
        fig.gravity()

        # print(fig.pos_y)
        # print(fig.vel_y)

        for event in keys_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fig.jump()
                    print(fig.pos_y)
            # closing of the window in game
            if event.type == pygame.QUIT:
                running = False

        if pressed[pygame.K_SPACE]:
            pass
            # k_space_edge = True
            # fig.move_up()
            # print(fig.pos_y)
        # elif pressed[pygame.K_DOWN]:
        #     fig.move_down()
        #     print(fig.pos_y)
        elif pressed[pygame.K_LEFT]:
            fig.move_left()
            print(fig.pos_x)
        elif pressed[pygame.K_RIGHT]:
            fig.move_right()
            print(fig.pos_x)
        # Exit condition to menu
        elif pressed[pygame.K_ESCAPE]:
            menu_state = 'Menu'
        elif pressed[pygame.QUIT]:
            running = False

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
