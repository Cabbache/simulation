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

gameDisplay = pygame.display.set_mode((1220,700))
gameDisplay.fill(black)
pixAr = pygame.PixelArray(gameDisplay)
w,h = pygame.display.get_surface().get_size()

balls = []

def solarSystem():
	sun = 100
	const = G*pow(sun,2)*math.pi
	balls.append(Ball(600,400,red,size=sun))
	balls.append(Ball(800,400,yellow,vy=-math.sqrt(const/200.0),size=15))
	balls.append(Ball(400,400,yellow,vy=math.sqrt(const/200.0),size=15))

def random(times):
	for x in xrange(times):
		xc = randint(0,w)
		yc = randint(0,h)
		si = randint(5,15)
		#vx = randint(-10,10)/10.0
		#vy = randint(-10,10)/10.0
		#print(str(xc)+","+str(yc)+","+str(si)+","+str(vx)+","+str(vy))
		balls.append(Ball(xc, yc, (randint(10,255), randint(10,255), randint(10,255)), si))

def load(filename):
	lines = []
	with open(filename, 'r') as f:
		lines = f.readlines()
	for line in lines:
		sp = line.split(",")
		balls.append(Ball(float(sp[0]), float(sp[1]), white, float(sp[2]), float(sp[3]), float(sp[4])))

solarSystem()
#random(200)
#random(90)
#load("random.txt")

#imagenum = 1
while True:
	pygame.display.update()
	gameDisplay.fill(black)

	pygame.event.get()
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]:
		point = pygame.mouse.get_pos()
		balls.append(Ball(point[0], point[1], white, size=15))

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
		#ball.attract(Ball(point[0], point[1], size=10), G)
		pygame.draw.circle(gameDisplay, ball.color, ball.getCoords(), int(ball.size))
	#pygame.image.save(gameDisplay, "simulation/"+str(imagenum)+".jpeg")
	#imagenum += 1
