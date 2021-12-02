#Status : Done
import math

input = "Day1\InputDay1.txt"
file = open(input, "r")
data = []
fuel = 0
fuelMod = 0
fuelTotal = 0
addFuel = 0
addFuelTotal = 0

line = file.readline().split('\n')[0]
while line:
	data.append(int(line))
	line = file.readline().split('\n')[0]

#For each module
for i in range(0, len(data)):
	addFuelTotal = 0
	value = data[i]
	fuel = math.floor(value/3)-2 #Fuel needed for the module
	addFuel = math.floor(fuel/3)-2 #Additional fuel needed for the module fuel
	while addFuel > 0: #Fuel needed for the additional fuel and itself
		addFuelTotal += addFuel
		addFuel = math.floor((addFuel)/3)-2
	fuelMod += fuel
	fuelTotal += fuel
	fuelTotal += addFuelTotal

print(fuelMod)
print(fuelTotal)