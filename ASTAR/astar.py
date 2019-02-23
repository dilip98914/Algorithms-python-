import pygame
import sys
import time
import random
import math
import threading

class Astar(object):
	def __init__(self,grid,start,end):
		self.cols=len(grid[0])
		self.rows=len(grid)
		self.start=grid [ start[0] ] [ start[1] ]
		self.end=grid [ end[0] ] [ end[1] ]

		""" nodes that already evaluated """ 
		self.closedSet=[]
		"""needs to be evaluated ,intially will contain only start node"""
		self.openSet=[]

		self.start.g_score=0
		self.start.h_score=self.start.calculate_heuiristic(self.end)
		self.start.f_score=self.start.h_score+self.start.g_score
		self.openSet.append(self.start)


	def do_perform(self):
		if len(self.openSet)>0:
			
			# calulate lowest f_score
			current=self.openSet[0]
			for elt in self.openSet:
				if elt.f_score<current.f_score:
					current=elt
			# check if it reached to the end
			if current==self.end:
				return
			# means finished being evaluated
			self.openSet.remove(current)
			self.closedSet.append(current)
			# now check for neighbours
			for nb in current.neighbours:
				if nb in self.closedSet:
					continue

				# distance from start to a neighbour
				gg_score=current.g_score+1

				if nb not in self.openSet:
					self.openSet.append(nb)
				elif gg_score>=nb.g_score:
					continue
				# this path is best unitl now record it
				nb.g_score=gg_score
				nb.f_score=nb.g_score+nb.h_score




class Node(object):
	def __init__(self,i,j,size):
		self.i=i
		self.j=j
		self.size=size
		# self.color=(0,0,0)
		self.x=self.i*self.size
		self.y=self.j*self.size
		# cost of getting from start node to this node
		self.g_score=0
		self.h_score=0
		self.f_score=0
		self.neighbours=[]


	""" call this method after whole grid is intilaized"""
	def add_neighbours(self,grid):
		i=self.i
		j=self.j
		grid_col=len(grid[0])
		grid_row=len(grid)

		if i>=1:
			n1=grid[j][i-1]
			self.neighbours.append(n1)
		else:
			pass
			# print('no neighbour to the left')
		if i<=grid_col-2:
			n2=grid[j][i+1]
			self.neighbours.append(n2)
		else:
			pass
			# print('no neighbour to the right')
		if j>=1:
			n4=grid[j-1][i]
			self.neighbours.append(n4)
		else:
			pass
			# print('no neighbour to the top')
		if j<=grid_row-2:
			n3=grid[j+1][i]
			self.neighbours.append(n3)
		else:
			pass
			# print('no neighbour to the bottom')



	def calculate_heuiristic(self,end):
		di=end.i-self.i
		dj=end.j-self.j
		return math.sqrt(di**2+dj**2)		

	def show(self,display,color=(255,255,255),border_flag=0):
		if border_flag==0:
			pygame.draw.rect(display,color,pygame.Rect(self.x,self.y,self.size,self.size))
		else:
			pygame.draw.rect(display,color,pygame.Rect(self.x,self.y,self.size,self.size),2)


class Main(object):
	def __init__(self):
		pygame.init()
		self.width=500
		self.height=500
		self.size=20
		self.screen=pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('ASTAR')
		self.cols=self.width//self.size
		self.rows=self.height//self.size
		# grid space to experiment
		self.grid=self.get_grid()
		self.add_all_neighbours()
		self.algo=Astar(self.grid,(0,0),(self.cols-1,self.rows-1))
		self.usr_logs()


	def change_end(self):
		self.pos=pygame.mouse.get_pos()
		x=self.pos[0]//self.size
		y=self.pos[1]//self.size
		pos=(x,y)
		print(pos)
		if pygame.mouse.get_pressed()[0]:
			# print('closked')
			self.algo=Astar(self.grid,(0,0),(y,x))

		# print(pos)

	def usr_logs(self):
		print("###### Welcome To Astar Algorithm#######")
		print('openSet:-Red')
		print('starting and ending:-White')
		print('closedSet:-kinda_blue')
		print('total nodes to evaluate:%d' %(len(self.grid)*len(self.grid[0])))


	def get_grid(self):
		return [ [Node(x,y,self.size) for x in range(self.cols)] for y in range(self.rows) ]

	def add_all_neighbours(self):
		for y in range(len(self.grid)):
			for x in range(len(self.grid[0])):
				self.grid[y][x].add_neighbours(self.grid)

	def draw_grid(self,display):
		for y in range(self.rows):
			for x in range(self.cols):
				spot=self.grid[y][x]
				if spot in self.algo.closedSet:
					spot.show(display,color=(12,122,155))
				if spot in self.algo.openSet:
					spot.show(display,color=(255,0,0))
				if spot==self.algo.start or  spot==self.algo.end:
					spot.show(display,color=(255,255,255))
		for y in range(self.rows):
			for x in range(self.cols):
				self.grid[y][x].show(display,color=(0,0,0),border_flag=1)

	
	def loop(self):
		while 1:
			for e in pygame.event.get():
				if e.type==pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.algo.do_perform()
			self.change_end()
			self.screen.fill((0,0,0))
			th=threading.Thread(target=self.draw_grid(self.screen))
			th.start()
			# self.draw_grid(self.screen)
			pygame.display.update()




if __name__=='__main__':
	main=Main()
	main.loop()