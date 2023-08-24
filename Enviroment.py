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


class Obstacle:
    def __init__(self, screen, Xdim, Ydim, Xpos, Ypos):
        self.screen = screen
        self.Xdim = Xdim
        self.Ydim = Ydim
        self.Xpos = Xpos
        self.Ypos = Ypos

    def get_edges(self):
        X = [self.Xpos, self.Xpos + self.Xdim, self.Xpos + self.Xdim, self.Xpos]
        Y = [self.Ypos, self.Ypos, self.Ypos + self.Ydim, self.Ypos + self.Ydim]

        return [X,Y]

    def get_upper_border(self):
        return self.Ypos

    def get_lower_border(self):
        return self.Ypos + self.Ydim

    def get_left_border(self):
        return self.Xpos

    def get_right_border(self):
        return self.Xpos + self.Xdim

    def draw(self):
        # wall = pygame.image.load('Pictures/rocket.png')
        # wall = pygame.Rect(self.Xpos, self.Ypos, self.Xdim, self.Ydim)

        wall = pygame.Surface((self.Xdim, self.Ydim))
        wall.fill([92, 64, 51])
        self.screen.blit(wall, (self.Xpos, self.Ypos))

    def object_detection(self, obj_positions, obj_dimensions):
        if self.right_left_border_check(obj_positions[0], obj_dimensions[0]) and self.up_low_border_check(obj_positions[1], obj_dimensions[1]):
            print('obj_detected')
            return True
        return False

    def up_low_border_check(self, y_pos, y_size):
        if y_pos > self.get_upper_border() and y_pos - y_size < self.get_lower_border():
            return True
        return False

    def right_left_border_check(self, x_pos, x_size):
        if self.Xpos + self.Xdim > x_pos > self.Xpos:
            return True
        return False
    
    def active(self):
        self.draw()

class Gravity:
    def __init__(self, value):
        self.gravity_value = value

    def get_gravity(self):
        return self.gravity_value


class Background:
    def __init__(self):
        pass