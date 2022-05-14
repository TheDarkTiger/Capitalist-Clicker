#!/usr/bin/env python
#! coding: utf-8
#! python3
# Capitalist Clicker 2022

import random
import pygame
import pygame.freetype


# Draw a task
def draw_task( color=(255,0,255), y=30, value=0 ) :
	pygame.draw.circle( screen, color, (30,y), 20,5 )
	pygame.draw.rect( screen, color, (70,y-15, 200,30) )
	pygame.draw.rect( screen, (0,0,0), (75,y-10, 190,20) )
	
	valueTextCanvas = font.render( str( value ), True, c_white )
	screen.blit( valueTextCanvas, (16, y-10) )
	

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


# Config window
pygame.init()
screen = pygame.display.set_mode( [300,450] )
pygame.display.set_caption( "Capitalist Clicker" )
framerate = 60
timer = pygame.time.Clock()
font = pygame.font.Font( "ka1.ttf", 16 )


# Game variables
tasks = {}
tasks["green"] = {"color":c_lgreen, "y":50, "value":1}
tasks["red"] = {"color":c_red, "y":110, "value":2}
tasks["orange"] = {"color":c_orange, "y":170, "value":3}
tasks["white"] = {"color":c_gray, "y":230, "value":4}
tasks["purple"] = {"color":c_purple, "y":290, "value":5}


# Main

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
	
	for task in tasks :
		draw_task( tasks[task]["color"], tasks[task]["y"], tasks[task]["value"] )
	
	pygame.display.flip()
	
	# Householding
	timer.tick( framerate )

pygame.quit()

