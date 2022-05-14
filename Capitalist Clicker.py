#!/usr/bin/env python
#! coding: utf-8
#! python3
# Capitalist Clicker 2022

import random
import pygame
import pygame.freetype

# Draw text
def draw_text( coords=(0,0), text="None", color=(255,0,255) ) :
	textCanvas = font.render( str( text ), True, color )
	screen.blit( textCanvas, coords )


# Draw a task
def draw_task( color=(255,0,255), y=30, value=0, advancement=0 ) :
	# Icon
	icon = pygame.draw.circle( screen, color, (30,y), 20,5 )
	draw_text( (16, y-10), str( value ), c_white )
	
	# Bar
	pygame.draw.rect( screen, color, (70,y-15, 200,30) )
	pc = (advancement/100.0)
	pygame.draw.rect( screen, (0,0,0), (75+(190*pc),y-10, 190*(1-pc),20) )
	
	return icon


# Draw a button
def draw_button( coords=(0,0), text="None", color=(255,0,255), size=(50,30) ) :
	button = pygame.draw.rect( screen, color, (coords, size) )
	draw_text( coords, str( text ), c_white )
	return button


# Update a task
def update_task( value=0, working=False, advancement=0, speed=0 ):
	global money
	
	if working :
		advancement += speed
	
	if advancement >= 100 :
		advancement = 0
		working = False
		money += value
	
	return working, advancement

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
money = 0


# Game variables
tasks = {}
tasks["green"] = {"color":c_lgreen, "y":60, "value":1, "working":False, "speed":5, "advancement":0, "icon":None}
tasks["red"] = {"color":c_red, "y":120, "value":2, "working":False, "speed":4, "advancement":0, "icon":None}
tasks["orange"] = {"color":c_orange, "y":180, "value":3, "working":False, "speed":3, "advancement":0, "icon":None}
tasks["white"] = {"color":c_gray, "y":240, "value":4, "working":False, "speed":2, "advancement":0, "icon":None}
tasks["purple"] = {"color":c_purple, "y":300, "value":5, "working":False, "speed":1, "advancement":0, "icon":None}

managers = {}
managers["green"] = {"owned":False, "cost":100, "buyButton":None}
managers["red"] = {"owned":False, "cost":200, "buyButton":None}
managers["orange"] = {"owned":False, "cost":300, "buyButton":None}
managers["white"] = {"owned":False, "cost":400, "buyButton":None}
managers["purple"] = {"owned":False, "cost":500, "buyButton":None}

# Main

# Set the game
backgroundColor = c_black
running = True

while running :
	
	# Events
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN :
			# Buy buttons
			for task in tasks :
				if tasks[task]["icon"] != None :
					if tasks[task]["icon"].collidepoint( event.pos ) :
						tasks[task]["working"] = True
			# Managers buttons
			for manager in managers :
				if managers[manager]["buyButton"] != None :
					if managers[manager]["buyButton"].collidepoint( event.pos ) :
						if money >= managers[manager]["cost"] :
							managers[manager]["owned"] = True
			
	
	# Drawing
	screen.fill( backgroundColor )
	
	# Tasks
	for task in tasks :
		t = tasks[task]
		t["working"], t["advancement"] = update_task( t["value"], t["working"], t["advancement"], t["speed"] )
		t["icon"] = draw_task( t["color"], t["y"], t["value"], t["advancement"] )
		
		if managers[task]["owned"] :
			t["working"] = True
	
	# Money
	draw_text( (10, 10), "Money "+str( money ), c_white )
	
	# Managers buttons
	x = 5
	draw_text( (10,320), "Buy more", c_white )
	draw_text( (10,385), "Buy managers", c_white )
	for manager in managers :
		m = managers[manager]
		
		draw_button( (x, 345), m["cost"], color=tasks[manager]["color"] )
		
		if not m["owned"] :
			if money >= m["cost"] :
				color = tasks[manager]["color"]
			else :
				color = c_dgray
			
			m["buyButton"] = draw_button( (x, 410), m["cost"], color )
		
		x += 55
	
	# Update display
	pygame.display.flip()
	
	# Householding
	timer.tick( framerate )

pygame.quit()

