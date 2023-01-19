class commonCharacter:
  def __init__(self, name):
    self.name = name
    self.hp = 100
    self.stamina = 100

  def __str__(self):
    return self.name




a = commonCharacter('Franta')

print(a)