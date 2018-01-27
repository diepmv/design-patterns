"""
Problem: The user expectation yields multiple, related objects
Scenario: Pet factory(Dog factory, Cat factory, both produce related products)
Solution: Abstract factory:
+pet factory
+concrete factory: dog factory and cat factory
+abstract product
+ concrete product: dog and dog food, cat and cat food
"""


class Dog():
  """One of objects to be returned"""
  def speak(self):
    return "woof!"

  def __str__(self):
    """Concrete Factory"""
    return "Dog"


class DogFactory():
  """Concrete factory"""
  def get_pet(self):
    """return dog object"""
    return Dog()
  def get_food(self):
    """return a dog food object"""
    return "dog food"

class PetStore():
  """Petstore houses our abstract factory"""
  def __init__(self, pet_factory=None):
    """pet_factory is our abstract factory"""
    self._pet_factory = pet_factory

  def show_pet(self):
    """utility method to display the details of the objects returned by the Dogfactory"""
    pet =  self._pet_factory.get_pet()
    pet_food = self._pet_factory.get_food()
    return 

#Create a concrete factory:
factory = DogFactory()

#create a pet store housing our abstract factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()















