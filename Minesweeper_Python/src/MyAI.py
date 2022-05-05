# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action
import numpy as np
from random import randint


class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		
		self.row = rowDimension
		self.col = colDimension
		self.numOfMines = totalMines
		self.numOfFlag = 0 #should be one by the end 
		self.numUncoveredtiles = 1
		self.unTiles = []
		self.flag = []
		self.uncovered = []
		self.label = np.full((rowDimension, colDimension), -1)
		self.elabel = np.zeroes(rowDimension, colDimension)
		self.amove = Action(AI.Action.UNCOVER, startX, startY) #uncovers the first move tile 
		

		

		

		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int):
		
		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		
		#win condition= uncovered all except one tile 
		if (self.row * self.col) - self.numOfMines == self.numUncoveredtiles:
			return Action(AI.Action.LEAVE)

		#check which tiles are uncovered relative to the current position
		#uncovered = [] #tiles uncovered relative to start position
		
		if number != -1: # if uncover then update
			self.unTiles.append((self.amove.getX(), self.amove.getY())) # uncovered tiles
			self.label[self.amove.getX(), self.amove.getY()] = number # number of neighbors

			numFlagged, numNoFlagged = self.marked(self.amove.getX(), self.amove.getY())

			# EffectiveLabel(x) = Label(x) – NumMarkedNeighbors(x)

			self.elabel[self.amove.getX(), self.amove.getY()] = self.label[self.amove.getX(), self.amove.getY()] - numFlagged

			if self.elabel[self.amove.getX(), self.amove.getY()] == numNoFlagged:

				if self.elabel[self.amove.getX(), self.amove.getY()] == 0: # uncover all unmarked neighbors
					self.unCoverAll(self.amove.getX(), self.amove.getY())







		
		
		
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
	def unCoverAll(self, x, y):
		
		# left side
		## left
		if self.tileinBounds(x - 1, y) and (x - 1, y) not in self.flag and (x - 1, y) not in self.uncovered: # if coordinates is valid and it is not a flag and it is not uncovered
			self.uncovered.append((x - 1, y))
			self.amove = Action(AI.Action.UNCOVER, x - 1, y)

			return self.amove
	
		## top left
		if self.tileinBounds(x - 1, y + 1) and (x - 1, y + 1) not in self.flag and (x - 1, y + 1) not in self.uncovered: 

			self.uncovered.append((x - 1, y + 1))
			self.amove = Action(AI.Action.UNCOVER, x - 1, y + 1)

			return self.amove
		
		## bottom left
		if self.tileinBounds(x - 1, y - 1) and (x - 1, y - 1) not in self.flag  and (x - 1, y - 1) not in self.uncovered: 
			self.uncovered.append((x - 1, y - 1))
			self.amove = Action(AI.Action.UNCOVER, x - 1, y - 1)

			return self.amove
		

		# right side

		## right
		if self.tileinBounds(x + 1, y) and (x + 1, y) not in self.flag and (x + 1, y) not in self.uncovered: 
			self.uncovered.append((x + 1, y))
			self.amove = Action(AI.Action.UNCOVER, x + 1, y)

			return self.amove
		
		## top right
		if self.tileinBounds(x + 1, y + 1)  and (x + 1, y + 1) not in self.flag and (x + 1, y + 1) not in self.uncovered: 
			self.uncovered.append((x + 1, y + 1))
			self.amove = Action(AI.Action.UNCOVER,x + 1, y + 1)

			return self.amove
		
		## top right
		if self.tileinBounds(x + 1, y - 1) and (x + 1, y - 1) not in self.flag and (x + 1, y - 1) not in self.uncovered: 
			self.uncovered.append((x + 1, y - 1))
			self.amove = Action(AI.Action.UNCOVER, x + 1, y - 1)

			return self.amove
		

		#top 
		if self.tileinBounds(x, y + 1) and (x, y + 1) not in self.flag and (x, y + 1) not in self.uncovered: 
			self.uncovered.append((x, y + 1))
			self.amove = Action(AI.Action.UNCOVER, x, y + 1)

			return self.amove

		#bottom 
		if self.tileinBounds(x, y - 1) and (x, y - 1) not in self.flag and (x, y - 1) not in self.uncovered: 
			self.uncovered.append((x, y - 1))
			self.amove = Action(AI.Action.UNCOVER, x, y - 1)

			return self.amove
		

	def markedOrUnmarked(self, x, y):
		i = 0 # marked with a flag
		j = 0 # not marked with a flag
		# left side
		## left
		if self.tileinBounds(x - 1, y) and (x - 1, y) in self.flag and (x - 1, y) not in self.uncovered: # if valid move and flagged and not uncovered
			i +=1 
		
		if self.tileinBounds(x - 1, y) and (x - 1, y) not in self.flag and (x - 1, y) not in self.uncovered: #if valid move and unflagged and  not uncovered
			j +=1 


		## top left
		if self.tileinBounds(x - 1, y + 1) and (x - 1, y + 1) in self.flag and (x - 1, y + 1) not in self.uncovered: 
			i +=1 
		
		if self.tileinBounds(x - 1, y + 1) and (x - 1, y + 1) not in self.flag and (x - 1, y + 1) not in self.uncovered: 
			j +=1 
		## bottom left
		if self.tileinBounds(x - 1, y - 1) and (x - 1, y - 1) in self.flag and (x - 1, y - 1) not in self.uncovered: 
			i +=1 
		if self.tileinBounds(x - 1, y - 1) and (x - 1, y - 1) not in self.flag and (x - 1, y - 1) not in self.uncovered: 
			j +=1 

		# right side

		## right
		if self.tileinBounds(x + 1, y) and (x + 1, y) in self.flag and (x + 1, y) not in self.uncovered:
			i +=1 
		if self.tileinBounds(x + 1, y) and (x + 1, y) not in self.flag and (x + 1, y) not in self.uncovered:
			j +=1 
		
		## top right
		if self.tileinBounds(x + 1, y + 1) and (x + 1, y + 1) in self.flag and (x + 1, y + 1) not in self.uncovered: 
			i +=1 
		if self.tileinBounds(x + 1, y + 1) and (x + 1, y + 1) not in self.flag and (x + 1, y + 1) not in self.uncovered:
			j +=1 

		## bottom right
		if self.tileinBounds(x + 1, y - 1) and (x + 1, y - 1) in self.flag and (x + 1, y - 1) not in self.uncovered:
			i +=1 
		if self.tileinBounds(x + 1, y - 1) and (x + 1, y - 1) not in self.flag and (x + 1, y - 1) not in self.uncovered: 
			j +=1 


		#top 
		if self.tileinBounds(x, y + 1) and (x, y + 1) in self.flag and  (x, y + 1) not in self.uncovered: 
			i +=1 
		if self.tileinBounds(x, y + 1) and (x, y + 1) not in self.flag and (x, y + 1) not in self.uncovered:
			j +=1 

		#bottom 
		if self.tileinBounds(x, y - 1) and (x, y - 1) in self.flag and (x, y - 1) not in self.uncovered: 
			i +=1 
		if self.tileinBounds(x, y - 1) and (x, y - 1) not in self.flag and (x, y - 1) not in self.uncovered:
			j +=1 

		return i, j

	
	



	#check if tile is in Bounds or not 
	def tileinBounds(self, x, y):
		if x < 0 or x >= self.row or y < 0 or y>= self.col:
			return False
		else:
			return True

	def chooseRandom(self):
		
		randx = randint(0, self.row - 1) # bounds for x 
		randy = randint(0, self.col - 1) # bounds for y

		while((randx,randy) in self.unTiles or (randx == self.amove.getX() and randy == self.amove.getY()) ):
			randx = randint(0, self.row - 1) # bounds for x 
			randy = randint(0, self.col - 1) # bounds for y
		
		randomTup = [randx,randy]

		self.numUncoveredtiles += 1
		
		return randomTup
		#self.action = Action(AI.Action.UNCOVER, randx, randy)
		
		
	