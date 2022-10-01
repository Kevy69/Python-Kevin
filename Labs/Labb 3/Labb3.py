from Geometric_Shapes import *



if __name__ == "__main__":
    circle1 = Circle(10, 15, 5)
    circle2 = Circle(10, 15, 10)
    rectangle1 = Rectangle(10, 15, 2, 10)
    rectangle2 = Rectangle(10, 15, 5, 10)

    print(f"circle1 area: {circle1.Area}")
    print(f"circle1 Circumference: {circle1.Circumference}\n")
    
    print(f"circle2 area: {circle2.Area}")
    print(f"circle2 Circumference: {circle2.Circumference}")
    
    print(circle1 > circle2)
    print(circle1 < circle2)


#en operator overload av komparatoroperatorer < , > , <= , >= för jämförelser
#en override av __repr__()
#en override av __str__()
#x och y som representerar mittpositionen av objektet
#en translationsmetod som gör det möjligt att förflytta x och y
#en metod som checkar om en viss punkt befinner sig innanför i objektet
#felhantering
#en metod som checkar om cirkelinstansen är en enhetscirkel
#en metod som checkar om rektangelinstansen är en kvadrat
