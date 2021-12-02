#This is the computer that runs Intcode (see Day2)

import numpy as np

def compute(data,IN):
	step = 0
	nextstep = 4
	optcode = 0
	paraModes = []
	result = 0
	OUT = "0"
	
	instruction = [x for x in str(data[step])] #Init first instruction at step 0
	optcode = "".join(instruction[(len(instruction)-2):]) #Optcode : 2 rightmost digits of the instruction

	while optcode != "99":
		
		#Parameter modes : the rest of the instruction, in reverse order (right to left) (with a bunch of zeros at the end
		#temp = instruction[:(len(instruction)-2)][::-1]
		#paraModes = [str(int(x)) for x in np.zeros(10)]
		#for i in range(0,len(temp)-1):
		#	paraModes[i] = str(int(temp[i]))
		paraModes = instruction[:(len(instruction)-2)][::-1]
		for i in range(0,10):
			paraModes.append("0")


		#Init the values
		value = [str(int(x)) for x in np.zeros(10)]

		#Process the optcodes
		if optcode == "01" or optcode == "1": #Addition
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]
			
			result = str( int(value[0]) + int(value[1]) )
			
			if paraModes[2] == "0":
				data[int(data[step+3])] = result
			elif paraModes[0] == "1":
				data[step+3] = result

			nextstep = 4

		elif optcode == "02" or optcode == "2": #Multiplication
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]
			
			result = str( int(value[0]) * int(value[1]) )
			
			if paraModes[2] == "0":
				data[int(data[step+3])] = result
			elif paraModes[0] == "1":
				data[step+3] = result
			
			nextstep = 4
				
		elif optcode == "03" or optcode == "3": #Save an input
			if paraModes[0] == "0":
				data[int(data[step+1])] = str(IN)
			elif paraModes[0] == "1":
				data[step+1] = str(IN)
			
			nextstep = 2

		elif optcode == "04" or optcode == "4": #Read to an output
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			
			OUT = value[0] #Sent in the return
			print("output: " + str(OUT))
			#if OUT != "0":
			#	print(data[step-nextstep] + " at " + str(step-nextstep))
			#	input("Press Enter to continue...")

			nextstep = 2

		elif optcode == "05" or optcode == "5": #Jump if true
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]

			if value[0] != "0":
				step = int(value[1])
				nextstep = 0
			else:
				nextstep = 3


		elif optcode == "06" or optcode == "6": #Jump if false
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]

			if value[0] == "0":
				step = int(value[1])
				nextstep = 0
			else: 
				nextstep = 3

		elif optcode == "07" or optcode == "7": #Less than
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]

			if int(value[0])<int(value[1]):
				value[2] = "1"
			else: value[2] = "0"

			if paraModes[2] == "0":
				data[int(data[step+3])] = value[2]
			elif paraModes[2] == "1":
				data[step+3] = value[2]

			nextstep = 4

		elif optcode == "08" or optcode == "8": #Equals
			if paraModes[0] == "0":
				value[0] = data[int(data[step+1])]
			elif paraModes[0] == "1":
				value[0] = data[step+1]
			if paraModes[1] == "0":
				value[1] = data[int(data[step+2])]
			elif paraModes[1] == "1":
				value[1] = data[step+2]

			if value[0]==value[1]:
				value[2] = "1"
			else: value[2] = "0"

			if paraModes[2] == "0":
				data[int(data[step+3])] = value[2]
			elif paraModes[2] == "1":
				data[step+3] = value[2]

			nextstep = 4

		else: #No optcode recognized
			return -999

		step += nextstep
		instruction = [x for x in str(data[step])] #Read new instruction
		optcode = "".join(instruction[(len(instruction)-2):]) #Read new optcode

	return "Done"









def getData(path):
	file = open(path, "r")
	data = []

	content = file.readline().split(',')
	for i in range(0, len(content)):
		data.append(content[i])
	return data

