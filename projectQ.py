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

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project-Q')
clock = pygame.time.Clock()

headImg = pygame.image.load('head.png')

def head(x,y):
	gameDisplay.blit(headImg,(x,y))

x = (display_width * 0.45)
y = (display_height * .80)

#game over variable
gameOver = False

while not gameOver:
	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True
			
	#fill background color
	gameDisplay.fill(white)
	#add head
	head(x,y)
	#update display
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
