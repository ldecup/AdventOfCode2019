#Status : Done


min = 156218
max = 652527

def checkDecr(pwd):
	for i in range(1,6):
		if pwd[i-1]>pwd[i]:
			return False
	return True

def isDbl(pwd):
	for i in range(1,6):
		if pwd[i-1]==pwd[i]:
			if i<5 and i>1:
				if pwd[i]!=pwd[i+1] and pwd[i-2]!=pwd[i-1]:
					return True
			elif i==5:
				if pwd[3]!=pwd[4]:
					return True
			elif i<2:
				if pwd[i]!=pwd[i+1]:
					return True
		
	return False

#Main
count = 0
for i in range(min,max+1):
	pwd = [int(x) for x in str(i)]
	if checkDecr(pwd):
		if isDbl(pwd):
			count += 1

print(count)
