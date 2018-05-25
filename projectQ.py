#Filename: projectQ.py
#Written by Lance
#Written on 05/24/2018
#Description: This is the main project file

import pygame

pygame.init()

#constants
#display
display_width = 800
display_height = 600

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project-Q')
clock = pygame.time.Clock()

headImg = pygame.image.load('head.png')

def head(x,y):
	gameDisplay.blit(headImg,(x,y))

#starting position
x = (display_width * 0.45)
y = (display_height * .80)

#movement
x_change = 0

#game over variable
gameOver = False

#game loop
while not gameOver:
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True
		
		#when key is pushed down
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change =-5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
				
		#when key is released
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0
				
	#set new x position
	x += x_change
	#fill background color
	gameDisplay.fill(white)
	#add head
	head(x,y)
	#update display
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
