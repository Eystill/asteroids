import pygame
import random
from constants import ASTEROID_MIN_RADIUS
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

    # New method to handle the split of asteroids when they are shot
    def split(self):
        # First we remove the asteroid
        self.kill()

        # If the radius of the new asteroid is less than or equal to the min radius defined in constants, then do nothing.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create a random angle between 20 and 50 degrees
        # Then rotate the asteroit and set a new velocity based on the random angle. With a +- variation it will look like the asteroid splits.
        # Set the new object radius to be smaller than the previous asteroid
        random_angle = random.uniform(20,50)
        new_asteroid_velocity_1 = self.velocity.rotate(random_angle)
        new_asteroid_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects based on the new coordinates and the new radius
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set the new velocity of the asteroids. (They speed up when they are shot)
        new_asteroid_1.velocity = new_asteroid_velocity_1 * 1.2
        new_asteroid_2.velocity = new_asteroid_velocity_2 * 1.2

        # Return the new asteroid objects
        return(new_asteroid_1, new_asteroid_2)