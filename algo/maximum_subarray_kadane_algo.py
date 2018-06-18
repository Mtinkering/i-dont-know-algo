

def printResult(array,n):

	positiveMembers = [x for x in array if x >= 0]
	MSS = 0
	MNCS = 0
	if(len(positiveMembers) == 0):
		MSS = max(array)
		MNCS = MSS
	else:
		MNCS = sum(positiveMembers)
		currentMax = 0
		for number in array:
			currentMax = currentMax + number
			if (currentMax < 0):
				currentMax = 0
			elif (currentMax > MSS):
				MSS = currentMax

	print MSS, MNCS

for test in range(int(raw_input())):
	n = int(raw_input())
	array = [int(x) for x in raw_input().split()]

	printResult(array,n)