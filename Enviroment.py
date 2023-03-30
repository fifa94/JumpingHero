import pygame

class Ground:
    def __init__(self, ground_pos,screen):
        self.ground_pos = ground_pos

        self.screen = screen
        self.wall = pygame.image.load('Pictures/rocket.png')

        self.screen.blit(self.wall, (0, self.ground_pos))

        pass

    def border(self, act_pos, act_vel):
        if act_pos > self.ground_pos:
            return [self.ground_pos, 0]
        return [act_pos, act_vel]
