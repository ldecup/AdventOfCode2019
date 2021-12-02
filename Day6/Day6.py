#Status : Done
from anytree import Node, RenderTree
import orbmap as om

data = om.getData("Day6\InputDay6.txt")
map = om.mapOrb(data)

#print(RenderTree(map))



total = 0
for i in range (len(map.descendants)):
	total += len(map.descendants[i].ancestors)
	#print(str(map.descendants[i]) + " : " + str(len(map.descendants[i].ancestors)))
print(total)





