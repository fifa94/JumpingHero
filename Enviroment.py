import pygame


class Borders:
    def __init__(self, screen, ground_pos):
        self.ground_pos = ground_pos
        self.screen = screen
        self.wall = pygame.image.load('Pictures/rocket.png')

        self.screen.blit(self.wall, (0, self.ground_pos))
        pass

    def ground(self, act_pos):
        if act_pos > self.ground_pos:
            return True
        return False

    def heaven(self, act_pos):
        if act_pos < 0:
            print('heaven active')
            return True
        return False

    def left_border(self, act_pos_x):
        if act_pos_x <= 0:
            print('Left border activated')
            return True
        return False

    def right_border(self, act_pos_x):
        if act_pos_x >= (pygame.display.get_surface().get_width() - self.wall.get_width()):
            print('Right border activated')
            return True
        return False

    def border_frame(self, act_pos, act_vel, act_pos_x):
        if self.ground(act_pos):
            return [self.ground_pos, 0, act_pos_x]
        if self.heaven(act_pos):
            print('heaven active1')
            return [0, 0, 0]
        if self.left_border(act_pos_x):
            return [act_pos, act_vel, 0]
        if self.right_border(act_pos_x):
            return [act_pos, act_vel, pygame.display.get_surface().get_width() - self.wall.get_width()]
        return [act_pos, act_vel, act_pos_x]
