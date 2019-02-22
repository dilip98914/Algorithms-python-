import pygame
import sys
import time
import random


class Node(object):
	def __init__(self,i,j):
		self.i=i
		self.j=j
		self.size=10
		self.color=(0,0,0)
		self.x=self.i*self.size
		self.y=self.j*self.size


	def show(self,display):
		pygame.draw.rect(display,self.color,pygame.Rect(self.x,self.y,self.size,self.size))


first_ndoe=Node(2,2)


def main():
	pygame.init()
	width=500
	height=500
	screen=pygame.display.set_mode((width,height))
	pygame.display.set_caption('ASTAR')
	while 1:
		for e in pygame.event.get():
			if e.type==pygame.QUIT:
				pygame.quit()
				sys.exit()


		screen.fill((255,255,255))
		first_ndoe.show(screen)
		pygame.display.update()




if __name__=='__main__':
	main()