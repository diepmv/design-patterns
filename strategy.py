"""
Problem: Need for dynamically changing the behavior of an object

Scenario: Abstract Strategy class with a default set of behaviors
Concrete Strategy classes with new behaviors

Solution: The types module in python

"""
import types

class Strategy:
  """The strategy pattern class"""

  def __init__(self, function=None):
    self.name = "Default strategy"

    #if a reference to a function is provided, replace the execute() method with the function
    if function:
      self.execute = types.MethodType(function, self)

  def execute(self): #this get replaced by another version if another strategy is provided
    """The default method that prints the name of the strategy being used"""
    print("{} is used".format(self.name))

#Replace method 1
def strategy_one(self):
  print("{} is used to execute method 1".format(self.name))

#Replacement method 2
def strategy_two(self):
  print("{} is used to execute method 2".format(self.name))

s0 = Strategy()
s0.execute()


s1 = Strategy(function=strategy_one)
s1.name = 'Strategy one'
s1.execute()

s2 = Strategy(function=strategy_two)
s2.name = "Strategy two"
s2.execute()
