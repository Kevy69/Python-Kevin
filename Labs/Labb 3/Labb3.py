from Geometric_Shapes import Rectangle as rect
from Geometric_Shapes import Circle





if __name__ == "__main__":
    circle1 = Circle(10, 15, 5)
    circle2 = Circle(10, 15, 10)
    rectangle1 = rect(10, 15, 2, 10)
    rectangle2 = rect(10, 15, 5, 10)

    print(f"circle1 area: {circle1.Area}")
    print(f"circle1 Circumference: {circle1.Circumference}\n")
    
    print(f"circle2 area: {circle2.Area}")
    print(f"circle2 Circumference: {circle2.Circumference}")
    
    print(circle1 > circle2)
    print(circle1 < circle2)
    
    print(circle1)
    
    print(circle1.Area)
    
    print(f"jew: {rectangle1.IsSquare()}")
    


# todo:
# display shapes
# en metod som checkar om en viss punkt befinner sig innanför i objektet
# felhantering
# comment code
