from math import pi
import pygame
from random import randint

class Shape():
    """Shape class, which the other (more specific) shapes inherit from"""
    def __init__(self, X: int, Y: int) -> None:
        # Readonly properties
        self._X = X
        self._Y = Y
        self._Area = None
        self._Circumference = None
        
        # Read/write properties
        self.AccelerationX = 0
        self.AccelerationY = 0
        
        self._Gravity = 1
        
        self.Color = (randint(0, 255),  # R
                      randint(0, 255),  # G
                      randint(0, 255)) # B
    
    # Readonly property definitions
    @property
    def X(self) -> int:
        return self._X
    
    @property
    def Y(self) -> int:
        return self._Y
        
    @property
    def Area(self) -> int:
        return self._Area

    @property
    def Circumference(self) -> int:
        return self._Circumference
    
    # Read/write property definitions
    @property
    def AccelerationX(self) -> int:
        return self._AccelerationX

    @AccelerationX.setter
    def AccelerationX(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._AccelerationX = value
        
    @property
    def AccelerationY(self) -> int:
        return self._AccelerationY

    @AccelerationY.setter
    def AccelerationY(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._AccelerationY = value
    
    @property
    def Gravity(self) -> int:
        return self._Gravity
    
    @property
    def Color(self) -> tuple:
        return self._Color

    @Color.setter
    def Color(self, value) -> None:
        if not isinstance(value, tuple):
            raise TypeError("only tuples's are allowed!")
        self._Color = value
    
    # Overloading <, <=, >, and >=.
    # Check if the first object's _Area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, OtherObj) -> bool:
        if self.Area < OtherObj.Area: return True
        else: return False
        
    def __le__(self, OtherObj) -> bool:
        if self.Area <= OtherObj.Area: return True
        else: return False

    def __gt__(self, OtherObj) -> bool:
        if self.Area > OtherObj.Area: return True
        else: return False
        
    def __ge__(self, OtherObj) -> bool:
        if self.Area >= OtherObj.Area: return True
        else: return False
    
    
    # Return a dictionary containing the properties of the given class instance.
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    # Translate, e.g set new values for x/y
    def Translate(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("only int's are allowed!")
        self._X = x
        self._Y = y
    
    # Simulate acceleration and gravitational force.
    def SimulateForces(self) -> None:
        self._X -= self.AccelerationX
        self._Y -= self.AccelerationY
        self.AccelerationY -= self.Gravity



class Rectangle(Shape):
    """Rectangle class. A class that can be used to spawn, manipulate and keep track of rectangles"""
    def __init__(self, X: int, Y: int, side1: int, side2: int) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)
        
        if not isinstance(side1, int) or not isinstance(side2, int):
            raise TypeError("only int's are allowed!")
            
        
        # Readonly properties
        self._side1 = side1
        self._side2 = side2
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = side1 * side2
        self._Circumference = 2 * (side1 + side2)
    
    # Readonly property definitions
    @property
    def side1(self) -> None:
        return self._side1

    @property
    def side2(self) -> None:
        return self._side2
    
    def __eq__(self, OtherObj) -> bool:
        if isinstance(OtherObj, Rectangle):
            return True
        return False
    
    # Check if shape is a square
    def IsSquare(self) -> bool:
        if self._side1 == self._side2:
            return True
        return False
    
    # Draw the rectangle
    def Draw(self, window) -> None:
        pygame.draw.rect(window, self.Color, pygame.Rect(
            self._X, self._Y, self._side1, self._side2))


class Circle(Shape):
    """Circle class. A class that can be used to spawn, manipulate and keep track of rectangles"""
    def __init__(self, X: int, Y: int, Radius) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)
        
        if not isinstance(Radius, int):
            raise TypeError("only int's are allowed!")

        # Readonly properies
        self._Radius = Radius
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = pi * Radius ** 2
        self._Circumference = 2 * pi * Radius
        
    # Readonly property definitions
    @property
    def Radius(self) -> None:
        return self._Radius
    
    def __eq__(self, OtherObj) -> bool:
        if isinstance(OtherObj, Circle):
            return True
        return False
    
    # Check if circle is at Origo, with a radius of 1
    def IsUnitCircle(self) -> bool:
        if self.X == 0 and self.Y == 0 and self.Radius == 1: return True
        return False
    
    # Check if a given point is inside the circle instance
    def IsInside(self, PointX: int, PointY: int) -> bool:
        if not isinstance(PointX, int) or not isinstance(PointY, int):
            raise TypeError("only int's are allowed!")
        
        # Source: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
        # Caution! PEMDAS/BEDMAS's order of operation
        return (PointX - self.X)**2 + (PointY - self.Y)**2 < self.Radius**2
    
    # Draw circle
    def Draw(self, window) -> None:
        pygame.draw.circle(window, self.Color, [self.X, self.Y], self.Radius, 0)
        

