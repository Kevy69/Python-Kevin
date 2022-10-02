from math import pi

class Shape():
    def __init__(self, X: int, Y: int) -> None:
        self.X = X
        self.Y = Y
        self._Area = None
        self._Circumference = None
        
    @property
    def X(self) -> None:
        return self._X

    @X.setter
    def X(self, value) -> int:
        self._X = value
    
    
    @property
    def Y(self) -> None:
        return self._Y

    @Y.setter
    def Y(self, value) -> int:
        self._Y = value
    
        
    @property
    def Area(self) -> None:
        print("getter ran")
        return self._Area

    @property
    def Circumference(self) -> None:
        print("getter ran")
        return self._Circumference


    def __eq__(self, OtherObj):
        if (self._Area == OtherObj._Area): return True
        else: return False
    
    # Overloading the <, <=, >, and >= operators.
    # Check if the first object's _Area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, OtherObj):
        if self._Area < OtherObj._Area: return True
        else: return False
        
    def __le__(self, OtherObj):
        if self._Area <= OtherObj._Area: return True
        else: return False

    def __gt__(self, OtherObj):
        if self._Area > OtherObj._Area: return True
        else: return False
        
    def __ge__(self, OtherObj):
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
        self.SideX = Width
        self.SideY = Height
        # Calculate Area & Circumference
        self._Area = (Width * Height)
        self._Circumference = 2 * (Width + Height)



class Circle(Shape):
    def __init__(self, X: int, Y: int, Radius) -> None:
        super().__init__(X, Y)
        self.Radius = Radius
        
        # Calculate Area & Circumference.
        # No paranthesis needed due to PEMDAS/BEDMAS's order of operation
        self._Area = pi * Radius ** 2
        self._Circumference = 2 * pi * Radius
    
    
