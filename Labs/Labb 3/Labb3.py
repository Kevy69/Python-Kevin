import pygame
from random import randint
from Geometric_Shapes import Circle
from Geometric_Shapes import Rectangle
import Geometric_Shapes





if __name__ == "__main__":
    
    Geometric_Shapes.Shape
    
    cirkel1 = Circle(x=0, y=0, radius=5)  # enhetscirkel
    cirkel2 = Circle(x=1, y=1, radius=5)
    rektangel = Rectangle(x=0, y=0, side_x=1, side_y=1)
    
    print(cirkel1 == cirkel2)  # True
    print(cirkel2 == rektangel)  # False
    print(cirkel1.is_inside(2, 2))  # True
    cirkel1.translate(5, 5)
    print(cirkel1.is_inside(10, 10))  # False
    
    # Throws error, used for demo
    #cirkel1.Translate("TRE", 5)  # ge ValueError med lämplig kommentar



    # Fireworks section
    
    particles = []

    pygame.init()

    win = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Yea, i've got no idea what this is...")

    run = True

    ticks = 300
    TimeBetweenFireworks = randint(30, 100)

    while run:
        # (Attempt) to run loop every 10 ms (100 times/sec)
        pygame.time.delay(10)
        
        # Make sure user cant quit via window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Wait for ticks to increment up to n number, where n is randomly defined
        if ticks >= TimeBetweenFireworks:
            # Spawn some particles!
            particles.append(Circle(randint(1, 1200), 800, 3))
            particles[-1].color = (255, 255, 255)
            
            # Give acceleration so they shoot up from the bottom of the screen like rockets
            particles[-1].acceleration_y = randint(20, 38)
            
            # Reset tick based timers
            TimeBetweenFireworks = randint(20, 120)
            ticks = 0
        
        # Simulate forces
        # using mod (%) operator to only run this section every other loop iteration
        # in order to slow down physics simulation to a more desirable speed.
        if ticks % 2 == 0:
            # Clear the screen
            win.fill((0, 0, 0))
            
            # Draw and simulate physics for each particle instance
            for Index, Particle in enumerate(particles):
                Particle.simulate_forces()
                Particle.draw(win)
                
                # Check if particle has reached apogee (highest point in its ascent).
                # Also check particle radius in order to make sure we dont cleanup the
                # negatively accelerating particles that represent the actual firework "cloud"
                if Particle.acceleration_y <= 0 and Particle.radius >= 3:
                    # Delete the particle
                    particles.pop(Index)
                    
                    # Spawn a bunch of new particles that will shoot in all different directions,
                    # simulating fireworks!
                    for _ in range(randint(20, 40)):
                        
                        # Spawn them at the prior location of the "parent" particle with a
                        # random size and acceleration
                        particles.append(
                            Circle(Particle.x, Particle.y, randint(1, 2)))
                        particles[-1].acceleration_x = randint(-6, 6)
                        particles[-1].acceleration_y = randint(0, 10)
                
                # Check if particle has gone out of bounds (e.g off the screen/window),
                # if so, delete. This is crucial in order to prevent the program from killing itself by
                # creating a bunch of class instances.
                if Particle.y > 850:
                    particles.pop(Index)


        ticks += 1
        pygame.display.update()
        
    pygame.quit()