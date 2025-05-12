from circleshape import CircleShape
from constants import *
from shots import *
import pygame

# We construct a new Player class that inherits from the CircleShape class
# PLAYER_RADIUS from constants is loaded into the method because we want to draw the player
# an instanced attribute "rotation" has been created
class Player(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

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
    
    # When the key a is pressed turn left calling the rotate method with (-dt) when the key d is pressed turn right calling the rotate method with (dt)
    # When the keys w and s are pressed respectively, the player moves backwards and forwards.
    # Start a shoot timer to allow for intervals in between shots even if the spacebar is held down
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()
                self.shoot_timer = PLAYER_SHOT_TIMER

                


    # Method to move the player forward or backwards
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    # Method to shoot. Velocity is defined as a Vector2 object that shoots in the direction the player is facing (self.rotation)
    # The value is multiplied with the PLAYER_SHOOT_SPEED from constants.py
    # The radius is defined in a similar way. A copy of the self.position is created, so as not to overwrite the players position.
    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        Shot(self.position.copy(), velocity, PLAYER_SHOT_RADIUS)