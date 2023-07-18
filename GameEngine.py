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
        self.obst1 = Enviroment.Obstacle(screen, 150, 35, 200, 200)
        self.obst2 = Enviroment.Obstacle(screen, 150, 35, 400, 400)
        self.ground = Enviroment.Obstacle(screen, 600, 30, 0, 550)

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
        # self.fig.gravity()
        self.fig.vertical_dynamics(self.gravity.get_gravity())


        self.object_colisions()

        fig_act_pos = self.fig.get_actual_position()
        # print(str(self.ground.object_detection(fig_act_pos[0], fig_act_pos[1])) + ' x = ' + str(fig_act_pos[0]) + ' y = ' + str(fig_act_pos[1]))



        # user control logic
        self.user_control()


        # Exit condition to menu
        if pressed[pygame.K_ESCAPE]:
            menu_state = 'Menu'
        elif pressed[pygame.QUIT]:
            running = False

        self.obst1.active()
        self.obst2.active()
        self.ground.active()
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

        if pressed[pygame.K_LEFT]:
            self.fig.horizontal_dynamics(-5)
            # self.fig.move_left()
            print(self.fig.pos_x)
        elif pressed[pygame.K_RIGHT]:
            self.fig.horizontal_dynamics(5)
            # self.fig.move_right()
            print(self.fig.pos_x)

    def object_colisions(self):
        fig_act_pos = self.fig.get_actual_position()

        if self.ground.object_detection(fig_act_pos[0], fig_act_pos[1]):
            self.fig.set_y_position(self.ground.get_upper_border())
            self.fig.set_y_velocity(0)

        if self.obst1.object_detection(fig_act_pos[0], fig_act_pos[1]):
            a1 = abs(self.obst1.get_upper_border() - fig_act_pos[1])
            a2 = abs(self.obst1.get_lower_border() - fig_act_pos[1])
            print(self.obst1.get_upper_border())
            print(self.obst1.get_lower_border())
            A = [a1, a2]
            index = A.index(min(A))
            print(A)
            print(index)

            if index == 0:
                self.fig.set_y_position(self.obst1.get_upper_border())
            elif index == 1:
                self.fig.set_y_position(self.obst1.get_lower_border())
            self.fig.set_y_velocity(0)

        if self.obst2.object_detection(fig_act_pos[0], fig_act_pos[1]):
            self.fig.set_y_position(self.obst2.get_upper_border())
            self.fig.set_y_velocity(0)

