from math import pi

class Shape():
    def __init__(self, X: int, Y: int) -> None:
        self.X = X
        self.Y = Y
        self.Area = None
        self.Circumference = None
    
    def __eq__(self, OtherObj):
        if (self.Area == OtherObj.Area): return True
        else: return False
    
    # Overloading the <, <=, >, and >= operators.
    # Check if the first object's area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, OtherObj):
        if self.Area < OtherObj.Area: return True
        else: return False
        
    def __le__(self, OtherObj):
        if self.Area <= OtherObj.Area: return True
        else: return False

    def __gt__(self, OtherObj):
        if self.Area > OtherObj.Area: return True
        else: return False
        
    def __ge__(self, OtherObj):
        if self.Area >= OtherObj.Area: return True
        else: return False



class Rectangle(Shape):
    def __init__(self, X: int, Y: int, Width: int, Height: int) -> None:
        super().__init__(X, Y)
        self.SideX = Width
        self.SideY = Height
        # Calculate area & circumference
        self.Area = (Width * Height)
        self.Circumference = 2 * (Width + Height)



class Circle(Shape):
    def __init__(self, X: int, Y: int, Radius) -> None:
        super().__init__(X, Y)
        self.Radius = Radius
        # Calculate area & circumference.
        # No paranthesis needed due to PEMDAS/BEDMAS's order of operation
        self.Area = pi * Radius ** 2
        self.Circumference = 2 * pi * Radius
