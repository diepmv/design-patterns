"""
Problem: Only one instance
Global variable in an object-oriented way

Scenerio: An information cache
Share by multiple objects

Solution:
Module: Shared by multiple objects
The Borg design pattern
"""

class Borg(object):
  """Make class attribute global"""
  _share_state = {} #Attribute dictionary

  def __init__(self):
    self.__dict__ = self._share_state #make it an attribute dictionary


class Singleton(Borg): #inherits from Borg
  """this class now shares all its attributes among its various instances"""
  #This essentially makes the singleton objects an object oriented global variable

  def __init__(self, **kwargs):
    Borg.__init__(self)
    #update the attribute dictionary by inserting a new key-value pair
    self._share_state.update(kwargs)

  def __str__(self):
    #return the attribute dictionary fro printing
    return str(self._share_state)

x = Singleton(HTTP="Hyper Text Transfer Protocol")

print(x)

y = Singleton(SNMP="Simple Network Management Protocol")

print(y)


assert x is y
