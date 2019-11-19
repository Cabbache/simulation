import math

class Ball:
	
	def __init__(self,x=0,y=0,color=(255,255,255),size=10,vx=0,vy=0):
		self.x = x
		self.y = y
		self.color = color
		self.vx = vx
		self.vy = vy
		self.size = size
	
	def frame(self):
		self.x += self.vx
		self.y += self.vy
	
	def area(self):
		return math.pi*pow(self.size,2)

	def noRoot(self, ball):
		return pow(ball.x-self.x,2) + pow(ball.y-self.y,2)

	def distance(self, ball):
		return math.sqrt(self.noRoot(ball))

	def attract(self, body, G=1):
		M = body.area()
		m = self.area()
		A = G*M/self.noRoot(body)
		Ax = A/self.distance(body) * (body.x-self.x)
		Ay = A/self.distance(body) * (body.y-self.y)
		self.vx += Ax
		self.vy += Ay

	def getCoords(self):
		return [int(self.x), int(self.y)]
	
	def isOverlap(self, mass):
		return self.distance(mass) < self.size+mass.size
	
	def avg(self,x,y):
		return (x+y)/2.0

	def merge(self, ball):
		mass = ball.area()+self.area()
		newSize = math.sqrt(mass/math.pi)
		newX = self.x + ((ball.x-self.x) * ball.area()/mass)
		newY = self.y + ((ball.y-self.y) * ball.area()/mass)
		newVx = (ball.area()*ball.vx + self.area()*self.vx) / mass
		newVy = (ball.area()*ball.vy + self.area()*self.vy) / mass
		return Ball(newX, newY, size=newSize, vx=newVx, vy=newVy)
