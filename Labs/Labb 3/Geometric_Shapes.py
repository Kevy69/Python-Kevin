import pygame
from math import pi
from random import randint
from abc import abstractmethod, ABC

class Shape(ABC):
    """
        A class which the other (more specific) shapes inherits from

        Args:
            x -> int
            y -> int

        Returns:
            None

        Raises:
            TypeError
    """
    
    def __init__(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("only int's are allowed!")
        
        # Readonly properties
        self._x = x
        self._y = y
        self._area = None
        self._circumference = None
        
        # Read/write properties
        self.acceleration_x = 0
        self.acceleration_y = 0
        
        self._gravity = 1
        
        self.color = (randint(0, 255),  # R
                      randint(0, 255),  # G
                      randint(0, 255))  # B
    
    # Readonly property definitions
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
        
    @property
    def area(self) -> int:
        return self._area

    @property
    def circumference(self) -> int:
        return self._circumference
    
    @property
    def gravity(self) -> int:
        return self._gravity
    
    # Read/write property definitions
    @property
    def acceleration_x(self) -> int:
        return self._acceleration_x

    @acceleration_x.setter
    def acceleration_x(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._acceleration_x = value
        
    @property
    def acceleration_y(self) -> int:
        return self._acceleration_y

    @acceleration_y.setter
    def acceleration_y(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._acceleration_y = value
    
    @property
    def color(self) -> tuple:
        return self._color

    @color.setter
    def color(self, value) -> None:
        if not isinstance(value, tuple):
            raise TypeError("only tuples's are allowed!")
        self._color = value
    
    # Overloading <, <=, >, and >=.
    # Check if the first object's _area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, other_obj) -> bool:
        if self.area < other_obj.area: return True
        else: return False
        
    def __le__(self, other_obj) -> bool:
        if self.area <= other_obj.area: return True
        else: return False

    def __gt__(self, other_obj) -> bool:
        if self.area > other_obj.area: return True
        else: return False
        
    def __ge__(self, other_obj) -> bool:
        if self.area >= other_obj.area: return True
        else: return False
    
    
    # Return a dictionary containing the properties of the given class instance.
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    # Enforce implementation of these functions across all instances
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def is_inside(self):
        pass
    
    # Translate, e.g set new values for x/y
    def translate(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("only int's are allowed!")
        self._x = x
        self._y = y
    
    # Simulate acceleration and gravitational force.
    def simulate_forces(self) -> None:
        self._x -= self.acceleration_x
        self._y -= self.acceleration_y
        self.acceleration_y -= self.gravity
    

class Rectangle(Shape):
    """
        A class that can be used to spawn, manipulate and keep track of rectangles

        Args:
            x -> int
            y -> int
            side_x -> int
            side_y -> int

        Returns:
            None

        Raises:
            TypeError
    """
    
    def __init__(self, x: int, y: int, side_x: int, side_y: int) -> None:
        # To propely inherit from Shape class
        super().__init__(x, y)
        
        if not isinstance(side_x, int) or not isinstance(side_y, int):
            raise TypeError("only int's are allowed!")
            
        # Readonly properties
        self._side_x = side_x
        self._side_y = side_y
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._area = side_x * side_y
        self._circumference = 2 * (side_x + side_y)
    
    # Readonly property definitions
    @property
    def side_x(self) -> int:
        return self._side_x

    @property
    def side_y(self) -> int:
        return self._side_y
    
    def __eq__(self, other_obj) -> bool:
        if isinstance(other_obj, Rectangle): return True
        return False
    
    # Check if a given point is inside the circle instance
    def is_inside(self, point_x: int, point_y: int) -> bool:
        if not isinstance(point_x, int) or not isinstance(point_y, int):
            raise TypeError("only int's are allowed!")
        
        # Calculate x/y points on the perimeter of the rectangle
        x1 = self.x - (self.side_x / 2)
        x2 = self.x + (self.side_x / 2)
        
        y1 = self.y - (self.side_y / 2)
        y2 = self.y + (self.side_y / 2)
        
        # Check if the given point is greather than or less than the perimeter point values.
        if point_x > x1 and point_x < x2 and point_y > y1 and point_y < y2:
            return True
        else: return False
    
    # Check if shape is a square
    def is_square(self) -> bool:
        if self.side_x == self.side_y:
            return True
        return False
    
    # Draw the rectangle
    def draw(self, window: pygame.Surface) -> None:
        if not isinstance(window, pygame.Surface):
            raise TypeError("only 'pygame.Surface' allowed!")
        
        pygame.draw.rect(window, self.color, pygame.Rect(
            self.x, self.y, self.side_x, self.side_y))


class Circle(Shape):
    """
        A class that can be used to spawn, manipulate and keep track of circles

        Args:
            x -> int
            y -> int
            radius -> int

        Returns:
            None

        Raises:
            TypeError
    """
    
    def __init__(self, x: int, y: int, radius) -> None:
        # To propely inherit from Shape class
        super().__init__(x, y)
        
        if not isinstance(radius, int):
            raise TypeError("only int's are allowed!")

        # Readonly properies
        self._radius = radius
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._area = pi * radius ** 2
        self._circumference = 2 * pi * radius
        
    # Readonly property definitions
    @property
    def radius(self) -> int:
        return self._radius
    
    def __eq__(self, other_obj) -> bool:
        if isinstance(other_obj, Circle): return True
        return False
    
    # Check if circle is at Origo, with a radius of 1
    def is_unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1: return True
        return False
    
    # Check if a given point is inside the circle instance
    def is_inside(self, point_x: int, point_y: int) -> bool:
        if not isinstance(point_x, int) or not isinstance(point_y, int):
            raise TypeError("only int's are allowed!")
        
        # Source: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
        # Caution! PEMDAS/BEDMAS's order of operation
        return (point_x - self.x)**2 + (point_y - self.y)**2 < self.radius**2
    
    # Draw circle
    def draw(self, window: pygame.Surface) -> None:
        if not isinstance(window, pygame.Surface):
            raise TypeError("only 'pygame.Surface' allowed!")
        
        pygame.draw.circle(window, self.color, [self.x, self.y], self.radius, 0)
        

