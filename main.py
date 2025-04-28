# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	# Splash screen showing that pygame module runs and the screen resolution set in constants
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Create a FPS controller object to use for frames per seconds calculations
	fps_controller = pygame.time.Clock()
	dt = 0

	# Initialize game area with the resolution specified in constants
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# Initialize a player with properties from the Player class in player.py and the height and width form constants
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
		screen.fill((0,0,0))
		player.draw(screen)
		pygame.display.flip()
		
if __name__ == "__main__":
	main()