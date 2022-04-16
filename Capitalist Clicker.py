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


# Draw a task
def draw_task( color=(255,0,255), y=30 ) :
	pygame.draw.circle( screen, color, (30,y), 20,5 )
	pygame.draw.rect( screen, color, (70,y-15, 200,30) )
	pygame.draw.rect( screen, (0,0,0), (75,y-10, 190,20) )
	


# Config window
pygame.init()
screen = pygame.display.set_mode( [300,450] )
pygame.display.set_caption( "Capitalist Clicker" )
framerate = 60
timer = pygame.time.Clock()
font = pygame.font.Font( "freesansbold.ttf", 16 )

# Main
def main() :
	
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
		
		draw_task( c_lgreen, 50 )
		draw_task( c_red, 110 )
		draw_task( c_orange, 170 )
		draw_task( c_gray, 230 )
		draw_task( c_purple, 290 )
		
		pygame.display.flip()
		
		# Householding
		timer.tick( framerate )
	
	pygame.quit()
	

# run the main function only if this module is executed as the main script
# Close to useless here, as the game will probably never be called as a submodule
if __name__=="__main__":
	main()
