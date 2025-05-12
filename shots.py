import pygame
from circleshape import CircleShape

# Create a Shot class that inherits from CircleShape class.
class Shot(CircleShape):
    containers = None
    def __init__(self, position, velocity, radius):
        CircleShape.__init__(self, position.x, position.y, radius)
        self.velocity = velocity
        # Initialize the Sprite object
        pygame.sprite.Sprite.__init__(self)
        # Add self to containers
        self.add(self.containers)
        # Create the surface to draw on (pygame.SRCALPHA allows for use of opacity)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        # Draw the circle onto the surface
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), self.radius, 2)
        # Set the center of the drawing - in this case a circle, despite the rect name. The method originally works with rectangles
        self.rect = self.image.get_rect(center=tuple(self.position))
        

    # override the update method from CircleShape and update the position based on the velocity and deltatime (dt)
    # This ensures a smooth update as omitting (dt) would cause the object to update only on a full screen update
    def update(self, dt):
        self.position += self.velocity * dt
        # Define the center of the rect object as a tuple of integers as the position is a tuple of floats.
        # This ensures smoother updating
        self.rect.center = (int(self.position.x), int(self.position.y))