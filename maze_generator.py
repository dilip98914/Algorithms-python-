import pygame
import random
import sys

def get_index(i,j):
	if i<0 or j<0 or i>cols-1 or j>rows-1:
		return -1
	return int(i+j*cols)


def remove_walls(a,b):
	x=a.i-b.i
	if x==1:
		a.walls[3]=False
		b.walls[1]=False
	elif x==-1:
		a.walls[1]=False
		b.walls[3]=False
	y=a.j-b.j
	if y==1:
		a.walls[0]=False
		b.walls[2]=False
	elif y==-1:
		a.walls[2]=False
		b.walls[0]=False


class Cell(object):
	def __init__(self,i,j,size):
		self.i=i
		self.j=j
		self.size=size
		self.x=self.i*self.size
		self.y=self.j*self.size
		self.color=(255,0,255)
		#			top  right bottom left
		self.walls=[True,True,True,True]
		self.visited=False

	# returns a random but not visited neighbour
	def check_neighbours(self):
		neighbours=[]
		i=self.i
		j=self.j
		# getting neighbours
		left=None
		right=None
		top=None
		bottom=None

		if get_index(i-1,j)!=-1:
			left=grid[get_index(i-1,j)]
		if get_index(i+1,j)!=-1:
			right=grid[get_index(i+1,j)]
		if get_index(i,j-1)!=-1:
			top=grid[get_index(i,j-1)]
		if get_index(i,j+1)!=-1:
			bottom=grid[get_index(i,j+1)]

		if left is not None:	
			if not left.visited:
				neighbours.append(left)
		if right is not None:	
			if not right.visited:
				neighbours.append(right)
		if top is not None:
			if not top.visited:
				neighbours.append(top)
		if bottom is not None:
			if not bottom.visited:
				neighbours.append(bottom)

		# print("neightbors: "+str(len(neighbours)))		
		if len(neighbours)>0:
			nei_index=random.randint(0,len(neighbours)-1)	
			# print('index:'+str(nei_index))
			return neighbours[nei_index]
		else:
			# print('neighbour is undefined!!')
			return None


	def highlight(self,display):
		x0=self.x
		x1=x0+self.size
		y0=self.y
		y1=y0+self.size

		pygame.draw.rect(display,(0,0,255),pygame.Rect(self.x,self.y,size,size))

	def show(self,display):
		x0=self.x
		x1=x0+self.size
		y0=self.y
		y1=y0+self.size

		if self.visited:
			pygame.draw.rect(display,(255,255,255),pygame.Rect(self.x,self.y,size,size))
		else:
			return

		if self.walls[0]:
			pygame.draw.line(display,self.color,(x0,y0),(x1,y0),2)
		if self.walls[1]:
			pygame.draw.line(display,self.color,(x1,y0),(x1,y1),2)
		if self.walls[2]:
			pygame.draw.line(display,self.color,(x1,y1),(x0,y1),2)
		if self.walls[3]:
			pygame.draw.line(display,self.color,(x0,y1),(x0,y0),2)



if __name__=="__main__":
	# clock=pygame.time.Clock()
	print('\n#######Hello from Maze-Generator#####\n')
	cols=int(input('enter number of cols:'))
	rows=int(input('enter number of rows:'))
	size=15
	width=cols*size
	height=rows*size
	grid=[]
	stack=[]
	current=None
	pygame.init()
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption('Maze-Generator')

	for y in range(rows):
		for x in range(cols):
			grid.append(Cell(x,y,size))

	current=grid[0]
	while 1:
		# clock.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()

		for x in range(len(grid)):
			grid[x].show(screen)
		#actual algorithm	
		current.visited=True
		current.highlight(screen)
		next=current.check_neighbours()
		if next is not None:
			next.visited=True
			stack.append(current)
			remove_walls(current,next)
			current=next

		elif len(stack)>0:
			current=stack.pop()

		pygame.display.update()
				
