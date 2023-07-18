import pygame
import Characters
import Enviroment


class Game:
    def __init__(self, py_game, screen, game_background):
        self.py_game = py_game
        self.screen = screen
        self.game_background = game_background



        # enviroment objects
        self.gravity = Enviroment.Gravity(1)
        self.obst1 = Enviroment.Obstacle(screen, 100, 100, 80, 80)
        self.ground = Enviroment.Obstacle(screen, 550, 50, 0, 550)

        # character obejcts
        self.fig = Characters.CommonCharacter('aaa', 100, 100, screen)
    def running(self):
        menu_state = 'Game'
        running = True

        # Load image to game scree background
        self.screen.blit(self.game_background, (0, 0))

        # draw character
        pressed = pygame.key.get_pressed()
        # keys_pressed = pygame.event.get()
        self.fig.gravity()

        self.obst1.active()
        self.ground.active()

        # user control logic
        self.user_control()

        # Exit condition to menu
        if pressed[pygame.K_ESCAPE]:
            menu_state = 'Menu'
        elif pressed[pygame.QUIT]:
            running = False

        self.fig.draw()

        # return game status
        return [menu_state, running]


    def user_control(self):
        pressed = pygame.key.get_pressed()
        keys_pressed = pygame.event.get()


        for event in keys_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.fig.jump()
                    print(self.fig.pos_y)
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
            self.fig.move_left()
            print(self.fig.pos_x)
        elif pressed[pygame.K_RIGHT]:
            self.fig.move_right()
            print(self.fig.pos_x)

    def object_colisions(self):
        pass
