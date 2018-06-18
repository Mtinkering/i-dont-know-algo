

def cal_coin_number(array, change):
	p = [0]*(change+1)

	p[0] = 0

	for i in range(1,change+1):
		minCoin = None
		for coin in [c for c in array if c <= i]:
			nCoin = 1 + p[i-coin]
			if minCoin == None or minCoin > nCoin:
				minCoin = nCoin
		p[i] = minCoin


	print p

	return p[-1]



print cal_coin_number([1,3,5],11)

