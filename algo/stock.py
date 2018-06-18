# T = int(raw_input())




# def maximizeProfit(array,N):
# 	if(N == 1): return 0

# 	if(N == 2):
# 		if(array[0] > array[1]):
# 			return 0
# 		else:

# 			return array[1] - array[0]


# 	cost = sum(array[0:N-1])

# 	profit = array[N-1]*(N-1) - cost

# 	return profit 
	



# def findRangeOfProfit(array,N):

# 	index = array.index(max(array))
# 	newRange = array[0:index+1]
# 	profit = 0
# 	if (index+1 == N):
# 		profit = maximizeProfit(newRange,len(newRange))
# 	else:
# 		profit =  maximizeProfit(newRange,len(newRange)) + findRangeOfProfit(array[index+1:N],len(array[index+1:N]))
# 	return profit		



# for i in range(T):

# 	N = int(raw_input())
# 	array = [int(x) for x in raw_input().split()]
# 	print findRangeOfProfit(array,N)

#method 2: not need to slice the array
for _ in xrange(input()):
    n, a = input(), map(int, raw_input().split())
    sufs = [-1]*n
    sufs[n-1] = a[n-1]

    for i in xrange(n-2,-1,-1):
        sufs[i] = max(a[i], sufs[i+1])
    print sufs
    res = shares = 0
    for i, x in enumerate(a):
    	print i,x
    	print sufs[i+1]
        if i == n-1 or x > sufs[i+1]:
            res += shares * x
            shares = 0
        else:
            res -= x
            shares += 1
    print res