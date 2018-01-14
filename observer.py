"""
Problem: Subjects to be monitored
Observer need to be notified when there is changes in subject

Scenarior:
Core temperatures: Reactors at a power plant
Registered observers: notifications

Solution:
Subject: abstract class
Attach-Detach-Notify
Concrete subjects

"""

class Subject(object): #represents what is being observed

  def __init__(self):
    #THis where references to all the observers are being kept
    #NOte that this is one-to-many relationship: there will be one subject to be observed by multiple_observers
    self._observers = []

  def attach(self, observer):
    if observer not in self._observers: #if observer is not already in the observer list
      self._observers.append(observer)  #append observer to the list

  def detach(self, observer): #simple remove observer
    try:
      self._observers.remove(observer)
    except ValueError:
      pass

  def notify(self, modifier=None):
    #for all the observers in the list
    for observer in self._observers:
      if observer is not modifier:  #Dont notify the observer who is actually updating the temperature
        observer.update(self)    #alert the observer


class Core(Subject): #inherit from the Subject class

  def __init__(self, name=""):
    Subject.__init__(self)
    self._name = name
    self._temp = 0 #initialize the temp

  @property
  def temp(self):
    return self.temp

  @temp.setter
  def temp(self, temp):
    self._temp = temp
    self.notify()  #Notify observer when somebody change core temperature


class TempViewer:

  def update(self, subject): #alert method that is invoked when the notify() method in a concrete subject is invoked
    print("Temperature Viewer: {} has temparature{}".format(subject._name, subject._temp))


c1 = Core("Core 1")
c2 = Core("Core 2")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90
