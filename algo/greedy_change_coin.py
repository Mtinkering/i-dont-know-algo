
def greedyCoinChanging(M, k):
	n = len(M)
	result = []
	for i in xrange(n - 1, -1, -1):
		result += [(M[i], k // M[i])]
		k %= M[i]
	return result
print greedyCoinChanging([2,3,5,6],10)