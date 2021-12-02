#This module handles wire grids (see day 3)

orY = 10000
orX = 10000

#Initialize a grid
def iniGrid(size):
	grid = []
	for i in range(size):
		temp = []
		for j in range(size):
			temp.append('.')
		grid.append(temp)
	grid[len(grid)-1-orY][orX] = '0'
	return grid

#Print a grid
def printGrid(grid):
	for i in range(len(grid)):
		print(grid[i])

#Print a char
def addChar(y,x,grid):
	if grid[y][x] == ".":
		grid[y][x] = "+"
	elif grid[y][x] == "+":
		grid[y][x] = "X"
	return grid

#Parse a list of commands onto a grid
def parseCom(input,grid):
	commands = input.split(",")
	y = len(grid)-1-orY
	x = orX
	for i in range(len(commands)):
		com = list(commands[i])[0]
		val = int(commands[i][1:])
		if com == "U":
			for a in range(y-val, y):
				  grid = addChar(a,x,grid)
			y -= val
		if com == "D":
			for a in range(y+1, y+1+val):
				  grid = addChar(a,x,grid)
			y += val
		if com == "L":
			for a in range(x-val, x):
				  grid = addChar(y,a,grid)
			x -= val
		if com == "R":
			for a in range(x+1, x+1+val):
				  grid = addChar(y,a,grid)
			x += val
	
				  
	return grid

#Find crossroads
def findX(grid):
	values = []
	for y in range(len(grid)):
		for x in range(len(grid)):
			if grid[y][x] == "X":
				values.append([y,x])
	return values

#Find the distance between a point and the origin
def cabDistance(y,x,size):
	distY = abs(size-1-orY - y)
	distX = abs(orX - x)
	return distX+distY