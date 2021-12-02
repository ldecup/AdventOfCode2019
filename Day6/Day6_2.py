#Status : Done
from anytree import Node, RenderTree
import orbmap as om

data = om.getData("Day6\InputDay6.txt")
map = om.mapOrb(data)

print(RenderTree(map))



youNode = om.findNode(map.descendants,"YOU")
sanNode = om.findNode(map.descendants,"SAN")

commonNode = om.findCommonPoint(map,youNode,sanNode)

print("common node :")
print(commonNode)

print("walk from You to Common:")
print(om.orbDist(map,commonNode,youNode))
distYou = len(om.orbDist(map,commonNode,youNode)[2]) - 1
print("number of steps:")
print(distYou)

print("walk from Common to San:")
print(om.orbDist(map,commonNode,sanNode))
distSan = len(om.orbDist(map,commonNode,sanNode)[2]) - 1
print("number of steps:")
print(distSan)

print("total steps:")
print(str(distYou+distSan))










