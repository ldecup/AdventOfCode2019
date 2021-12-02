#Library handling the orbital maps
import anytree
from anytree import Node, RenderTree
from anytree.walker import Walker

def getData(IN):
	OUT = []
	file = open(IN, "r")
	line = file.readline().split("\n")[0]
	while line:
		temp = line.split(")")
		OUT.append(temp)
		line = file.readline().split("\n")[0]
	return OUT

def findNode(nodes,target):
	for i in range(len(nodes)):
		if nodes[i].name == target:
			return nodes[i]
	return False

def mapOrb(IN):
	nodes = []
	com = Node("COM")
	nodes.append(com)
	newRun = True
	error = False
	while newRun:
		numNewNodes = 0
		for i in range (len(IN)):
			if findNode(nodes,IN[i][0]) != False: #if the parent exists
				if findNode(nodes,IN[i][1]) == False: #and if the node does not already exist
					newNode = Node(IN[i][1], parent = findNode(nodes,IN[i][0]))
					nodes.append(newNode)
					#print("new node : " + newNode.name)
					numNewNodes += 1
			else: error = True #parent does not exist, skip this node and start again
		if error == True:
			error = False
			newRun = True
		else:
			newRun = False
		print("end of run, "+str(numNewNodes)+" new nodes")
	return com

def findCommonPoint(map,origin,target):
	originAnc = origin.ancestors
	targetAnc = target.ancestors

	#print(originAnc)
	#print(targetAnc)

	i = 0
	while True:
		if originAnc[i] == targetAnc[i]:
			i += 1
		else:
			common = originAnc[i-1]
			return common

	return False

def orbDist(map,node1,node2):
	return Walker().walk(node1,node2)