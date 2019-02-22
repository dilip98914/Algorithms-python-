import pygame
import sys
import time
import random



class Astar(object):
	def __init__(self):
		# nodes that already evaluated
		self.closedSet=[]
		# need to be evaluated
		# intially will contain only start node
		self.openSet=[]




class Node(object):
	def __init__(self,i,j,size):
		self.i=i
		self.j=j
		self.size=size
		self.color=(0,0,0)
		self.x=self.i*self.size
		self.y=self.j*self.size


	def show(self,display):
		pygame.draw.rect(display,self.color,pygame.Rect(self.x,self.y,self.size,self.size),1)



# global space






class Main(object):
	def __init__(self):
		pygame.init()
		self.width=500
		self.height=500
		self.size=10
		self.screen=pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('ASTAR')
		self.cols=self.width//self.size
		self.rows=self.height//self.size
		# grid space to experiment
		self.grid=self.get_grid()

	def get_grid(self):
		return [ [Node(x,y,self.size) for x in range(self.cols)] for y in range(self.rows) ]

	def draw_grid(self,display):
		for y in range(self.rows):
			for x in range(self.cols):
				self.grid[y][x].show(display)
	
	def loop(self):
		while 1:
			for e in pygame.event.get():
				if e.type==pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill((255,255,255))
			self.draw_grid(self.screen)
			pygame.display.update()




if __name__=='__main__':
	main=Main()
	main.loop()