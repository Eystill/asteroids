import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Collision method uses asteroids as input for use to check for collision between player and asteroid.
    # Using self.position sets player position as point of origin and uses the built in distance.to() method from pygame.Vector2
    # If the distance from the player to the asteroids position is less than the sum of player radius and asteroids radius, then we have a collision
    def collision(self, asteroids):
        if self.position.distance_to(asteroids.position) < (self.radius + asteroids.radius):
            return(True)
        else:
            return(False)