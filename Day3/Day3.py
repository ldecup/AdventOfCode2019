#Status : does not work
import wiregrid as wg

input = "Day3\InputDay3.txt"
file = open(input, "r")

input1 = file.readline().split('\n')[0]
input2 = file.readline().split('\n')[0]
input3 = file.readline().split('\n')[0]
input4 = file.readline().split('\n')[0]

parse1 = wg.parseComLin(input1)
sortedParse1 = sorted(parse1, key=lambda tup: tup[0])
print("input 1 done")
grid = wg.parseCom(input4, grid,orX,orY)
print("input 2 done")
#wg.printGrid(grid)

print("finding crossroads...")
cross = wg.findX(grid)

print(cross)

print("processing distances...")
dists = []

for i in range(len(cross)):
	dist = wg.cabDistance(cross[i][0],cross[i][1],size,orX,orY)
	if dist>0:
		dists.append(dist)
	#print(wg.cabDistance(cross[i][0],cross[i][1],size))

print(dists)

