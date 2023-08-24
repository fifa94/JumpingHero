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
        self.obst1 = Enviroment.Obstacle(screen, 150, 100, 0, 469)
        self.obst2 = Enviroment.Obstacle(screen, 150, 100, 400, 469)
        self.obst3 = Enviroment.Obstacle(screen, 100, 30, 300, 300)

        self.ground = Enviroment.Obstacle(screen, 1000, 300, -200, 570)

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
        self.obst3.active()
        self.ground.active()
        self.fig.draw()

        # return game status
        return [menu_state, running]


    def user_control(self):
        pressed = pygame.key.get_pressed()
        keys_pressed = pygame.event.get()

        p = self.fig.get_actual_position()
        d = self.fig.get_dimensions()

        enable_jump = True
        # enable_jump = self.ground.object_detection(p, d) or self.obst1.object_detection(p, d) or self.obst2.object_detection(p, d) \
        #               or self.obst3.object_detection(p, d)

        # print('enable jump ' + str(enable_jump))
        for event in keys_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and enable_jump:
                    self.fig.vertical_dynamics(-15)    # jump
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



        # self.detection_in_x(self.obst1)
        self.detection_in_Y(self.obst1)

        self.detection_in_Y(self.obst2)
        self.detection_in_Y(self.obst3)

        self.detection_in_Y(self.ground)

    def detection_in_Y(self, obstacle):
        fig_act_pos = self.fig.get_actual_position()
        fig_dim = self.fig.get_dimensions()

        if obstacle.object_detection(fig_act_pos, fig_dim):

            diff = [abs(obstacle.get_upper_border() - fig_act_pos[1]),
                    abs(obstacle.get_lower_border() - fig_act_pos[1]),
                    abs(obstacle.get_left_border() - fig_act_pos[0]),
                    abs(obstacle.get_right_border() - fig_act_pos[0])
                    ]
            # print(diff)
            match diff.index(min(diff)):
                case 0:
                    self.fig.set_y_position(obstacle.get_upper_border())
                case 1:
                    a = diff.copy()
                    a.pop(0)
                    a.pop(0)
                    if max(a) < 100:
                        if a[0] < a[1]:
                            self.fig.set_x_position(obstacle.get_left_border())
                        else:
                            self.fig.set_x_position(obstacle.get_right_border())
                    self.fig.set_y_position(obstacle.get_lower_border() + fig_dim[1])
                case 2:
                    self.fig.set_x_position(obstacle.get_left_border())
                case 3:
                    self.fig.set_x_position(obstacle.get_right_border())
            self.fig.set_y_velocity(0)

    def detection_in_x(self, obstacle):
        fig_act_pos = self.fig.get_actual_position()
        fig_dim = self.fig.get_dimensions()

        if obstacle.object_detection(fig_act_pos, fig_dim):

            diff = [abs(obstacle.get_left_border() - fig_act_pos[0]),
                    abs(obstacle.get_right_border() - fig_act_pos[0])]

            match diff.index(min(diff)):
                case 0:
                    self.fig.set_x_position(obstacle.get_left_border())
                case 1:
                    self.fig.set_x_position(obstacle.get_right_border() + fig_dim[1])
            self.fig.set_y_velocity(0)