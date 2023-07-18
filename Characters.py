import pygame
import Enviroment

class CommonCharacter:
    def __init__(self, name, pos_x, pos_y, screen):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.perk = 'none'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0
        self.vel_y = 0
        self.screen = screen
        self.player = pygame.image.load('Pictures/hero_01.png')
        self.frame = Enviroment.Borders(self.screen, 540)
        self.draw()

        self.rotation_flag = True

    def __str__(self):
        new_line = '\n'
        separator = '====================================================' + new_line
        text_name = 'character name: ' + str(self.get_name()) + new_line
        text_hp = 'hit points: ' + str(self.get_hp()) + new_line
        text_stamina = 'stamina: ' + str(self.get_stamina()) + new_line
        output_text = separator + text_name + text_hp + text_stamina + separator
        return output_text

    def draw(self):

        self.screen.blit(self.player, (self.pos_x, self.pos_y))



    def jump(self):
        self.dynamics(-15)
        # k = self.frame.heaven(self.pos_y, self.vel_y)
        # k = self.frame.border_frame(self.pos_y, self.vel_y)
        # self.pos_y = k[0]
        # self.vel_y = k[1]
        print('jump')
        self.draw()



    def dynamics(self,acceleration):
        time_step = 1
        last_vel = self.vel_y
        self.vel_y = self.vel_y + (acceleration * time_step)
        self.pos_y = self.pos_y + ((self.vel_y + last_vel) * 0.5 * time_step)

    def frame_borders(self, act_pos, act_vel):
        l = self.frame.ground(act_pos)
        k = self.frame.heaven(act_pos)
        return [k[0], k[1]]

    def vertical_dynamics(self, acceleration):
        time_step = 1
        last_vel = self.vel_y
        self.vel_y = self.vel_y + (acceleration * time_step)
        self.pos_y = self.pos_y + ((self.vel_y + last_vel) * 0.5 * time_step)

    def horizontal_dynamics(self, step):
        self.pos_x += step

    def set_x_position(self, x_new): self.pos_x = x_new

    def set_y_position(self, y_new): self.pos_y = y_new

    def set_x_velocity(self, x_vel_new): self.vel_x = x_vel_new

    def set_y_velocity(self, y_vel_new): self.vel_y = y_vel_new

    def increase_hitpoint(self):
        pass

    def decrease_hitpoint(self):
        pass

    def increase_stamina(self):
        pass

    def decrease_stamina(self):
        pass

    def get_hp(self): return self.hp

    def get_stamina(self): return self.stamina

    def get_name(self): return self.name

    def get_actual_position(self): return [self.pos_x + 20, self.pos_y]

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# a = commonCharacter('Franta')
# print(a)
