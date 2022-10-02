from math import pi

# Shape class, which the other (more specific) shapes inherit from
class Shape():
    def __init__(self, X: int, Y: int) -> None:
        # Readonly properties
        
        self._X = X
        self._Y = Y
        self._Area = None
        self._Circumference = None
    
    # Readonly properies
    
    @property
    def X(self) -> None:
        return self._X
    
    @property
    def Y(self) -> None:
        return self._Y
        
    @property
    def Area(self) -> None:
        return self._Area

    @property
    def Circumference(self) -> None:
        return self._Circumference
        
    # Operator overloadings.
    
    # Compare dict output of both class instances, return false if there is a missmatch
    def __eq__(self, OtherObj) -> bool:
        if self.__dict__ == OtherObj.__dict__: return True
        return False
    
    # Overloading <, <=, >, and >=.
    # Check if the first object's _Area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, OtherObj) -> bool:
        if self._Area < OtherObj._Area: return True
        else: return False
        
    def __le__(self, OtherObj) -> bool:
        if self._Area <= OtherObj._Area: return True
        else: return False

    def __gt__(self, OtherObj) -> bool:
        if self._Area > OtherObj._Area: return True
        else: return False
        
    def __ge__(self, OtherObj) -> bool:
        if self._Area >= OtherObj._Area: return True
        else: return False
    
    
    # Return a dictionary containing the properties of the given class instance.
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    
    def Translate(self, x: int, y: int) -> None:
        self._X = x
        self._Y = y



class Rectangle(Shape):
    def __init__(self, X: int, Y: int, Width: int, Height: int) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)
        
        # Readonly properies
        
        self._Width = Width
        self._Height = Height
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = Width * Height
        self._Circumference = 2 * (Width + Height)
    
    # Readonly properies
    
    @property
    def Width(self) -> None:
        return self._Width

    @property
    def Height(self) -> None:
        return self._Height
    
    
    def IsSquare(self) -> bool:
        if self._Width == self._Height: return True
        return False
    
    def IsInside(self) -> bool:
        pass


class Circle(Shape):
    def __init__(self, X: int, Y: int, Radius) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)

        # Readonly properies
        
        self._Radius = Radius
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = pi * Radius ** 2
        self._Circumference = 2 * pi * Radius
        
    # Readonly property
    @property
    def Radius(self) -> None:
        return self._Radius
    
    # Check if circle is at Origo, with a radius of 1
    def IsUnitCircle(self) -> bool:
        if self._X == 0 and self._Y == 0 and self._Radius == 1: return True
        return False
    
    def IsInside(self) -> bool:
        pass
