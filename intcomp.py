#This is the computer that runs Intcode (see Day2)

def compute(data):
	step = 0
	nextstep = 4
	optcode = data[step]

	while optcode != 99:
		if optcode == 1:
			temp = data[data[step+1]]+data[data[step+2]]
			data[data[step+3]] = temp
			nextstep = 4
		elif optcode == 2:
			temp = data[data[step+1]]*data[data[step+2]]
			data[data[step+3]] = temp
			nextstep = 4
		else:
			return -999
		step += nextstep
		optcode = data[step]

	return data[0]

def getData(path):
	file = open(path, "r")
	data = []

	content = file.readline().split(',')
	for i in range(0, len(content)):
		data.append(int(content[i]))
	return data