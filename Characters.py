class commonCharacter:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.stamina = 100
    self.perk = 'none'

  def __str__(self):
    new_line = '\n'
    separator = '====================================================' + new_line
    text_name = 'character name: ' + str(self.getName()) + new_line
    text_hp = 'hit points: ' + str(self.getHP()) + new_line
    text_stamina = 'stamina: ' + str(self.getStamina()) + new_line
    output_text = separator + text_name + text_hp + text_stamina + separator
    return output_text

  def move_right(self):
    pass

  def move_left(self):
    pass

  def jump(self):
    pass

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

a = commonCharacter('Franta')
print(a)