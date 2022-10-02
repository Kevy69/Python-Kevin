from math import pi

class Shape():
    def __init__(self, X: int, Y: int) -> None:
        # Readonly properties
        self._X = X
        self._Y = Y
        self._Area = None
        self._Circumference = None
        
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
    
    # only way of setting x/y
    def Translate(self, x: int, y: int) -> None:
        self._X = x
        self._Y = y


    def __eq__(self, OtherObj) -> bool:
        if (self._Area == OtherObj._Area): return True
        else: return False
    
    # Overloading the <, <=, >, and >= operators.
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
    
    # Return a dictionary containing the properties of the given instance.
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)



class Rectangle(Shape):
    def __init__(self, X: int, Y: int, Width: int, Height: int) -> None:
        super().__init__(X, Y)
        self._Width = Width
        self._Height = Height
        # Calculate Area & Circumference
        self._Area = (Width * Height)
        self._Circumference = 2 * (Width + Height)
        
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
        super().__init__(X, Y)
        self._Radius = Radius
        
        # Calculate Area & Circumference.
        # No paranthesis needed due to PEMDAS/BEDMAS's order of operation
        self._Area = pi * Radius ** 2
        self._Circumference = 2 * pi * Radius
        
    @property
    def Radius(self) -> None:
        return self._Radius
    
    def IsUnitCircle(self) -> bool:
        if self._X == 0 and self._Y == 0 and self._Radius == 1:
            return True
        return False
    
    def IsInside(self) -> bool:
        pass
