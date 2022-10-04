from textwrap import indent
from Geometric_Shapes import Rectangle
from Geometric_Shapes import Circle
import pygame
from random import randint





if __name__ == "__main__":
    circle1 = Circle(100, 100, 14)
    circle2 = Circle(10, 15, 10)
    rectangle1 = Rectangle(10, 15, 2, 10)
    rectangle2 = Rectangle(10, 15, 2, 10)

    print(f"circle1 area: {circle1.Area}")
    print(f"circle1 Circumference: {circle1.Circumference}\n")
    
    print(f"circle2 area: {circle2.Area}")
    print(f"circle2 Circumference: {circle2.Circumference}")
    
    print(circle1 > circle2)
    print(circle1 < circle2)
    
    print(circle1)
    
    print(circle1.Area)
    
    Particles = []
    Particles2 = []
    
    #Particle = Circle(randint(1, 1200), 800, randint(1, 30))
    #Particle.AccelerationY = 30
    
    circle1.IsInside(90, 90)
    
    
    
    pygame.init()

    win = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Yea, i've got no idea what this is...")

    run = True

    ticks = 0
    ticks2 = 0

    while run:
        pygame.time.delay(10)
        
        pygame.draw.circle(win, (255, 0, 0), [
                           100, 100], 14, 0)
        
        pygame.draw.circle(win, (255, 0, 0), [
            90, 90], 1, 0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        if ticks >= 80:
            Particles.append(Circle(randint(1, 1200), 800, randint(3, 6)))
            Particles[-1].AccelerationY = randint(20, 40)
            
            ticks = 0

        if ticks2 >= 2:
            win.fill((0, 0, 0))
            for Index, Particle in enumerate(Particles):
                Particle.SimulateForces()
                Particle.Draw(win)
            
                if Particle.AccelerationY <= 0 and Particle.Radius >= 3:
                    Particles.pop(Index)
                    
                    for _ in range(30):
                        Particles.append(
                            Circle(Particle.X, Particle.Y, 2))
                        Particles[-1].AccelerationX = randint(-5, 5)
                        Particles[-1].AccelerationY = randint(0, 10)
                        #Particles[-1].Gravity = randint(1, 3)
                    
                if Particle.Y > 850:
                    Particles.pop(Index)
            
            ticks2 = 0
    
        
        # Cleanup
        
        ticks += 1
        ticks2 += 1
        
        pygame.display.update()

    pygame.quit()



# todo:
# en metod som checkar om en viss punkt befinner sig innanför i objektet
# felhantering
# UML