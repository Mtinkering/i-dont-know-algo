# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
	#Compute and return final answer over here
	sorted_prices = sorted(prices)
	i = 0
	item = sorted_prices[i]
	while rupees >= item:
		rupees -= item
		i += 1
		item = sorted_prices[i]
		


	return i

if __name__ == '__main__':
	n, k = map(int, raw_input().split())
	prices = map(int, raw_input().split())
	print max_toys(prices, k)
