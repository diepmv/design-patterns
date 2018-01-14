"""
+Problem
New features to an existing object
Dynamic changes
Not using subclassing

+Scenario:
Display "hello world" => "<blink>Hello world<blink>"

+ Solution:
FUnctions: objects in python
BUilt-in decorator feature

"""
from functools import wraps

def make_blink(function):
  """Define decorator"""

  @wraps(function)

  #This make the decorator transparent in term of its name and docstring
  def decorator():
    """Decorator function"""
    #Grab the return value of the function being decorated
    ret = function()
    #Add new functionality the the function being decorated
    return "<blink>" + ret + "</blink>"
  return decorator


#apply blink
@make_blink
def hello_world():
  """Original decorator"""
  return "hello world"


print(hello_world())

print(hello_world.__name__)

print(hello_world.__doc__)
