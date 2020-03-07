import pygame
import random

pygame.init()
disWidth = 1000
disHeight = 1000
gameDisplay = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

grey = (128,128,128)

foodImg = pygame.image.load('food.png') #Size is (220,200) 
snakeImg = pygame.image.load('head.png') #Size is (256,256)

'''
Found way to resize photos using windows, skip.
pygame.transform.scale(foodImg, (100,100))
pygame.transform.scale(snakeImg, (10,10))
'''
snake_Width = 100
snake_Height = 100

def snake(xs,ys):

	gameDisplay.blit(snakeImg,(xs,ys)) 
	
		 


def food(xf,yf):

	gameDisplay.blit(foodImg, (xf,yf))

def game():

	xs = (disWidth * .5)
	ys = (disHeight * .4)
	score = 0
	xsDelta = 0
	ysDelta = 0
	xf = random.randrange(0, disWidth , 100)
	yf = random.randrange(0, disHeight, 100)
	
	direction = None # 0 East, 1 North, 2 West, 3 South  


	eaten = False

	exitGame = False
	while not exitGame:
		if  xf == xs and yf == ys:
			eaten = True
		if eaten == True: 
			score += 1 
			print(score)
			eaten = False

			gameDisplay.fill(grey)
			xf = random.randrange(0, disWidth, 100)
			yf = random.randrange(0, disHeight, 100)
			food(xf,yf)
			snake(xs,ys)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exitGame = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					xsDelta = -100 
					ysDelta	= 0
					direction = 2
				elif event.key == pygame.K_d:
					xsDelta = 100
					ysDelta = 0
					direction = 0
				elif event.key == pygame.K_w:
					ysDelta = -100
					xsDelta = 0
					direction = 1
				elif event.key == pygame.K_s:
					ysDelta= 100
					xsDelta = 0
					direction = 3
		 


		xs += xsDelta
		ys += ysDelta
		gameDisplay.fill(grey)
		food(xf,yf)
		snake(xs,ys)

		if xs > disWidth - snake_Width or xs < 0:
			exitGame = True

		elif ys > disWidth - snake_Width or ys < 0:
			exitGame = True


		pygame.display.update()
		clock.tick(3)

game()