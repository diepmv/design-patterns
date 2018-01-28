"""
Problem: Uncertainties in types of objects or
Decisions to be made at runtime ragarding what classes to use

Scenario: Pet shop
Only dogs originally
now cats too
"""


class Dog(object):

  def __init__(self, name):
    self._name = name

  def speak(self):
    return "Woof!"

class Cat(object):

  def __init__(self, name):
    self._name = name

  def speak(self):
    return "Moew"


def get_pet(pet="dog"):
  pets = dict(dog=Dog("DOG"), cat=Cat("CAT"))
  return pets[pet]


d = get_pet()
print(d.speak())

c = get_pet(pet="cat")
print(c.speak())



class ShapeInterface():
  def draw(self): pass

class Circle(ShapeInterface):
  def draw(self):
    print("circle.draw")


class Square(ShapeInterface):
  def __init__(self):
    print("square.draw")

class ShapeFactory():
  @staticmethod
  def getShape(type):
    if type=='circle':
      return Circle()
    if type=='square':
      return Square()
    assert 0, 'Could not find shape'
