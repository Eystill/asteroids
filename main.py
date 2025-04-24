# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init()
	# Splash screen showing that pygame module runs and the screen resolution set in constants
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Initialize game area with the resolution specified in constants
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# creating an infinite loop
	while True:
		# Draw a black square inside the game area
		pygame.Surface.fill(screen, (0,0,0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
