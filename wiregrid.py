#This module handles wire grids (see day 3)


#Initialize a grid
def iniGrid(size,orX,orY):
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
def parseCom(input,grid,orX,orY):
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

#Parse a list of commands as positions
def parseComLin(input):
	output = [[0,0]]
	commands = input.split(',')
	for i in range(len(commands)):
		pos = output[len(output)-1]
		com = list(commands[i])[0]
		val = int(commands[i][1:])
		if com == "U":
			for a in range(1,val+1):
				pos = output[-1]
				newpos = [pos[0],pos[1]+1]
				output.append(newpos)
		if com == "D":
			for a in range(1,val+1):
				pos = output[-1]
				newpos = [pos[0],pos[1]-1]
				output.append(newpos)
		if com == "L":
			for a in range(1,val+1):
				pos = output[-1]
				newpos = [pos[0]-1,pos[1]]
				output.append(newpos)
		if com == "R":
			for a in range(1,val+1):
				pos = output[-1]
				newpos = [pos[0]+1,pos[1]]
				output.append(newpos)
	return output

#Find crossroads
def findX(grid):
	values = []
	for y in range(len(grid)):
		for x in range(len(grid)):
			if grid[y][x] == "X":
				values.append([y,x])
	return values

#Find the distance between a point and the origin
def cabDistance(y,x,size,orX,orY):
	distY = abs(size-1-orY - y)
	distX = abs(orX - x)
	return distX+distY