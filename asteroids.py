import pygame
from circleshape import CircleShape

# Create an Asteroid class that inherits from CircleShape class.
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
    
    # The draw method takes the screen as input. The screen object is provided in the main file when the method is called.
    def draw(self, screen):
        # The circle draw function draws on the screen in white colour. The self.position is a Vector2 value and comes from the CircleShape class
        # and it is converted to a tuple to meet the draw.circle requirements. Radius is added as well as the width of the "line" used to draw the circle
        # which must be an int value
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.position), self.radius, 2)

    # override the update method from CircleShape and update the position based on the velocity and deltatime (dt)
    # This ensures a smooth update as omitting (dt) would cause the object to update only on a full screen update
    def update(self, dt):
        self.position += self.velocity * dt