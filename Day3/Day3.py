import wiregrid as wg

size = 40

grid = wg.iniGrid(size)
input1 = "R8,D3,R8,U8,L10,D5,R7,U10,L7"
input2 = "U6,R7,U6,R3,D7,R6,D6,R8"

grid = wg.parseCom(input1, grid)
grid = wg.parseCom(input2, grid)
wg.printGrid(grid)

cross = wg.findX(grid)
print(cross)

for i in range(len(cross)):
	print(wg.cabDistance(cross[i][0],cross[i][1],size))

