#Status : WiP

width = 25
height = 6

file = open("Day8\InputDay8.txt", "r")
data = str(file.readline())
data = [int(x) for x in data]
nLayers = int(len(data)/(height*width))
lLayers = int(len(data)/nLayers)

img = []

for i in range(0,nLayers):
	temp = []
	for j in range(0,lLayers):
		temp.append(data[i+j])
	img.append(temp)

zeros = []
out = 0
min = 999
for i in range(0,nLayers):
	count = img[i].count(0)
	zeros.append(count)
	if count < min:
		out = i
		min = count
		print("newmin : "+str(min))

count1 = 0
count2 = 0
for i in range(0,lLayers):
	if img[out][i] == 1:
			count1 += 1
	if img[out][i] == 2:
			count2 += 1



print(zeros)
print(str(len(zeros)))
print("layers : "+str(nLayers)+", "+str(lLayers)+" points per layer")
print("1 : "+str(count1)+", 2 : "+str(count2)+", out = "+str(count1*count2))