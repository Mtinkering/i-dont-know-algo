#probability of random discrete variable

#value in the long run

N = input()

P = {}

nCases = 1
counter = 1
for i in raw_input().split():

	nCases *= counter
	counter += 1
	if i not in P:
		P[i] = 1

	else:
		P[i] += 1

def factorial(n):
	if (n==1): return 1

	return n*factorial(n-1)
	
for key in P:
	if (P[key] > 1):
		nCases /= factorial(P[key])



print "%.6f" % nCases
