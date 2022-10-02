from Geometric_Shapes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches




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
    
    print(circle1)
    
    print(circle1.Area)


    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    rect1 = patches.Rectangle((-200, -100), 400, 200, color ='green')
    
    ax.add_patch(rect1)
    
    plt.xlim([-400, 400])
    plt.ylim([-400, 400])
    
    plt.show()

# todo:
# display shapes
# en translationsmetod som gör det möjligt att förflytta x och y
# en metod som checkar om en viss punkt befinner sig innanför i objektet
# felhantering
# en metod som checkar om cirkelinstansen är en enhetscirkel
# en metod som checkar om rektangelinstansen är en kvadrat
