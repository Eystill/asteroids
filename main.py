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
		# If the player closes the window then terminate the program
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Draw a black square inside the game area and redraw it as long as the program runs
		screen.fill((0,0,0))
		pygame.display.flip()
		
if __name__ == "__main__":
	main()