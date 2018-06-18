#this is bullshit. not using graph theory
def findTheNextMax(array, excludeList):
	maxDiff = -1
	indexMax = -1
	for i in range(0,len(array)):
		if (array[i] > maxDiff and i not in excludeList):
			indexMax = i
			maxDiff = array[i]
	return indexMax

for _ in range(0,input()):
	N = input()
	H = [0]*N

	ladderBtm = [0]*N
	ladderTop = [0]*N
	for i in range(0,N):
		jmin, jmax = [int(x) for x in raw_input().split()]
		h = jmax - jmin
		ladderBtm.append(jmin)
		ladderTop.append(jmax)
		H.append(h)

	M = input()

	snakeHigh = [0]*M
	for j in range(0,M):
		jmax,jmin = [int(x) for x in raw_input().split()]
		snakeHigh.append(jmax)

	excludeList = []

	findMin()
	initial = 1
	def findMin():
		index = findTheNextMax(H, excludeList)
		excludeList.append(index)
		if (index == -1):
			print -1
			return
		else:
			step = 0
			while (initial)






