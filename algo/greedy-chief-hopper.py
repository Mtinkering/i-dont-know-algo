N = input()
lists = [int(x) for x in raw_input().split()]
minE = 0
total = 0

for i in range(N-1,-1,-1):

	total = (minE + lists[i])
	if (total%2 == 1):
		total += 1

	minE = total/2




print minE