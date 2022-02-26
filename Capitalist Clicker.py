#!/usr/bin/env python
#! coding: utf-8
#! python3
# Capitalist Clicker 2022

import random
import pygame
import pygame.freetype

# Pico8ish palette
c_white = (255,255,255)
c_gray = (191,191,191)
c_dgray = (127,127,127)
c_black = (0,0,0)
c_purple = (142,68,207)
c_magenta = (207,68,133)
c_red = (219,29,35)
c_orange = (255,168,17)
c_brown = (207,142,68)
c_beige = (255,214,144)
c_yellow = (245,231,0)
c_lgreen = (133,207,68)
c_green = (0,139,80)
c_dblue = (0,67,133)
c_blue = (68,133,207)
c_lblue = (125,187,255)

# Main
def main() :
	
	# Config window
	pygame.init()
	screen = pygame.display.set_mode( [300,450] )
	pygame.display.set_caption( "Capitalist Clicker" )
	framerate = 60
	timer = pygame.time.Clock()
	font = pygame.font.Font( "freesansbold.ttf", 16 )
	
	# Set the game
	backgroundColor = c_black
	running = True
	
	while running :
		
		# Events
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				running = False
		
		# Drawing
		screen.fill( backgroundColor )
		
		pygame.display.flip()
		
		# Householding
		timer.tick( framerate )
	
	pygame.quit()
	

# run the main function only if this module is executed as the main script
# Close to useless here, as the game will probably never be called as a submodule
if __name__=="__main__":
	main()
