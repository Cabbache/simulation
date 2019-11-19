import pygame
import math
from random import randint
from Ball import Ball

G = 0.01
pygame.init()

white = (255,255,255)
black = (0,0,0)

yellow = (255,128,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((1200,800))
gameDisplay.fill(black)
pixAr = pygame.PixelArray(gameDisplay)
w,h = pygame.display.get_surface().get_size()

balls = []

def solarSystem():
	sun = 100
	const = G*pow(sun,2)*math.pi
	balls.append(Ball(600,400,red,size=sun))
	balls.append(Ball(800,400,yellow,vy=math.sqrt(const/200.0)))
	balls.append(Ball(300,400,yellow,vy=-math.sqrt(const/300.0)))
	balls.append(Ball(1000,400,yellow,vy=-math.sqrt(const/400.0)))

def random(times):
	for x in xrange(times):
		balls.append(Ball(randint(0,w), randint(0,h), white, size=randint(5,10)))

#solarSystem()
random(200)

imagenum = 1
while True:
	pygame.display.update()
	pygame.event.get()
	gameDisplay.fill(black)
	for ball in balls:
		ball.frame()
		for other in balls:
			if ball == other:
				continue
			if not(ball.isOverlap(other)):
				other.attract(ball, G)
			else:
				balls.remove(ball)
				balls.remove(other)
				balls.append(ball.merge(other))
				break
		#point = pygame.mouse.get_pos()
		#ball.attract(Ball(point[0], point[1], size=500), G)
		pygame.draw.circle(gameDisplay, ball.color, ball.getCoords(), int(ball.size))
	pygame.image.save(gameDisplay, "simulation/"+imagenum+".jpeg")
	imagenum += 1
