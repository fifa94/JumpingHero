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

    def border_frame(self, act_pos, act_vel):
        if self.ground(act_pos):
            return [self.ground_pos, 0]
        if self.heaven(act_pos):
            print('heaven active')
            return [0, 0]
        return [act_pos, act_vel]
