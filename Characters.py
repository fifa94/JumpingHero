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
        self.player = pygame.image.load('Pictures/rocket.png')
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

    def move_right(self):
        print('move right')
        self.pos_x += 5
        if self.rotation_flag:
            self.player = pygame.transform.rotate(self.player, 45)
            self.rotation_flag = False

        self.draw()

    def move_left(self):
        print('move left')
        self.pos_x -= 5
        if self.rotation_flag:
            self.player = pygame.transform.rotate(self.player, 135)
            self.rotation_flag = False
        self.draw()

    def move_up(self):
        print('move up')
        self.pos_y -= 5
        self.rotation_flag = True
        self.draw()

    def move_down(self, velocity):
        print('move down')
        time_step = 1
        self.pos_y = self.pos_y + velocity * time_step
        self.draw()


    def jump(self):
        self.draw()

    def gravity(self):
        time_step = 1
        gravity = 1
        last_vel = self.vel_y
        self.vel_y = self.vel_y + (gravity * time_step)

        self.pos_y = self.pos_y + ((self.vel_y + last_vel) * 0.5 * time_step)

        print('gravity')

        g = Enviroment.Ground(450,self.screen)

        k = g.border(self.pos_y, self.vel_y)
        self.pos_y = k[0]
        self.vel_y = k[1]
        # time_step = 1
        # self.pos_y = self.pos_y + (v * time_step)
        self.draw()

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


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# a = commonCharacter('Franta')
# print(a)
