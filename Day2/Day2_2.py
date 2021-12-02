#Status : Done
import intcomp

for i in range(0,99):
	for j in range(0,99):
		data = intcomp.getData("Day2\InputDay2.txt")
		data[1] = i
		data[2] = j
		result = intcomp.compute(data)
		if result == 19690720:
			print(i)
			print(j)
			input("end")
print("No answer found")

