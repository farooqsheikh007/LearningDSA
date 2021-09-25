class Person():
  def __init__(self,name,type):
    self.name = name
    self.type = type
  def introduce(self):
    print(f'Hi my name is {self.name} and i am a {self.type}')

class Wizard(Person):
  def __init__(self,name,type,power):
    Person.__init__(self,name,type)
    self.power = power
  def unleash(self):
      print(f"i am {self.type} and i can do {self.power}")

wizard1 = Wizard("scorpio", "hell fire", "Portal")

wizard1.introduce()
wizard1.unleash()