"""
Problem:
+Creating many identical objects individually: expensive
+Cloning: an alternative

Scenerio: Mass production
+Create a prototypical instance first
+Simply clone it whenever you need replica

Related pattern: Abstract factory
"""
import copy

class Prototype():

  def __init__(self):
    self._objects = {}

  def register_object(self, name, obj):
    self._objects[name] = obj

  def unregister_object(self, name):
    """Unregister an object"""
    try:
      del self._objects[name]
    except KeyError:
      pass

  def clone(self, name, **attr):
    """Clone a register object and update its attributes"""
    obj = copy.deepcopy(self._objects.get(name))
    obj.__dict__.update(attr)
    return obj


class Car():

  def __init__(self):
    self.name = "Skylark"
    self.color = "Red"
    self.options = "Ex"

  def __str__(self):
    return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

c1 = prototype.clone("skylark")

print(c1)
