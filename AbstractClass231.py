from abc import ABC, abstractmethod          #can write ABC or ABCMeta both works

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):  
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 8
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth

rec1 = Rectangle()
print(rec1.printarea())
