from circleshape import CircleShape
from constants import *
import pygame

# We construct a new Player class that inherits from the CircleShape class
# PLAYER_RADIUS from constants is loaded into the method because we want to draw the player
# an instanced attribute "rotation" has been created
class Player(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Define the triangle method in the player class
    # Use the dimensions from the constants file
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # This method overrides the draw method from the circleshape module
    # the colour white is achieved via RGB values
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    # Method to rotate the player which uses the PLAYER_TURN_SPEED set in constants
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # When the key a is pressed turn left (-dt) when the key d is pressed turn right (dt)
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)