import pygame


class CommonCharacter:
    def __init__(self, name, pos_x, pos_y, screen):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.perk = 'none'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.player = pygame.Rect(self.pos_x, self.pos_y, 50, 50)
        self.draw()

    def __str__(self):
        new_line = '\n'
        separator = '====================================================' + new_line
        text_name = 'character name: ' + str(self.getName()) + new_line
        text_hp = 'hit points: ' + str(self.getHP()) + new_line
        text_stamina = 'stamina: ' + str(self.getStamina()) + new_line
        output_text = separator + text_name + text_hp + text_stamina + separator
        return output_text

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 255), self.player)



    def move_right(self):
      print('move right')
      self.player.move_ip(5, 0)
      self.draw()


    def move_left(self):
      print('move left')
      self.player.move_ip(-5, 0)
      self.draw()


    def jump(self):
      self.draw()


    def gravity(self):
      pass
    def increase_hitpoint(self):
      pass

    def decrease_hitpoint(self):
      pass

    def increase_stamina(self):
      pass

    def decrease_stamina(self):
      pass

    def getHP(self): return self.hp

    def getStamina(self): return self.stamina

    def getName(self): return self.name


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# a = commonCharacter('Franta')
# print(a)