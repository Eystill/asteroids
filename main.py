# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shots import *

def main():
	pygame.init()
	# Splash screen showing that pygame module runs and the screen resolution set in constants
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# groups to bundle methods to prevent clutter. updateable bundles all player updates and drawable bundles all drawing methods.
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	asteroidfield = pygame.sprite.Group()
	shot = pygame.sprite.Group()

	# Create containers to hold the groups
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (asteroidfield, updateable)
	Shot.containers = shot

	# Create a FPS controller object to use for frames per seconds calculations
	fps_controller = pygame.time.Clock()
	dt = 0

	# Initialize game area with the resolution specified in constants
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# Initialize a player with properties from the Player class in player.py and the height and width form constants
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	# Set the asteroid field to a variable to use for later
	asteroid_spawner = AsteroidField()

	# creating an infinite loop
	while True:
		# If the player closes the window then terminate the program
		for event in pygame.event.get():
			# pause the loop for 1/60th of a second before restarting
			fps_controller.tick(60)
			# The .tick() function returns the time it took in seconds from the last time it ran. Divide with 1000 to get this in miliseconds.
			dt = fps_controller.tick(60) / 1000
			if event.type == pygame.QUIT:
				return

		# Draw a black square inside the game area and redraw it as long as the program runs
		# Draw the player after drawing the black square, but before refreshing the whole image
		# draw the show when spacebar is pressed (See player.py where the call is made)
		# Update all updateables except the shot via the updateable group.
		# update the shot
		screen.fill((0,0,0))
		for drawing in drawable:
			drawing.draw(screen)
		shot.draw(screen)
		updateable.update(dt)
		shot.update(dt)

		# For every asteroid in asteroids, check for collision with the player. If true then exit the application
		for asteroid in asteroids:
			if player.collision(asteroid) == True:
				print("Game over!")
				import sys
				sys.exit()
		pygame.display.flip()
		
if __name__ == "__main__":
	main()