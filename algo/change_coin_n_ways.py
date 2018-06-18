# Enter your code here. Read input from STDIN. Print output to STDOUT
coins = sorted([int(i) for i in input()])
n = int(input())

def coinChange(n, coins):
    #print coins, n
    counts = [1] + [0] * n
    for c in coins:
        for i in range(len(counts)):
            if c + i <= n:
                counts[i + c] += counts[i]
    return counts[-1]

print coinChange(n, coins)
# # N,M = [int(x) for x in raw_input().split()]
# # coins = [int(x) for x in raw_input().split()]

# # coins.sort(reverse=True)
# # # totalWays = 0
# # # cache = {}

# # # def totalWays(n, array):
# # # 	key = str(n) + str(array)
# # # 	if (key in cache): return cache[key]

# # # 	if (n == 0): return 1
# # # 	if (len(array) == 1):
# # # 		if (n%array[0] == 0): return 1
# # # 		else: return 0

# # # 	maxValue = array.pop(0)
# # # 	nLoop = int(n/maxValue) + 1

# # # 	maxWays = 0
# # # 	for i in range(nLoop):
# # # 		currentArray = list(array)
# # # 		maxWays += totalWays(n - i*maxValue, currentArray)
		
# # # 	cache[key] = maxWays
# # # 	return maxWays
# # # print totalWays(N,coins)


# # def coinChange(n, coins):
# #     #print coins, n
# #     counts = [1] + [0] * n
# #     for c in coins:
# #         for i in range(len(counts)):
# #             if c + i <= n:
# #                 counts[i + c] += counts[i]
# #     return counts[-1]

# # print coinChange(N, coins)

# # import sys
# # import string
# # import fileinput
# # import pprint

# # inputs = fileinput.input()
# # coins = [int(num) for num in inputs[0].rstrip().split(', ')]
# # total = int(inputs[1])
# # # coins = [int(num) for num in numbers[:-1]]

# # coin_changes = [[0 for i in range(0, total + 1)] for j in range(0, len(coins))]

# # # pprint.pprint(coin_changes)

# # for j in range(0, len(coins)):
# # 	for i in range(0, total + 1):
# # 		if i == 0:
# # 			coin_changes[j][i] = 1
# # 		elif i - coins[j] >= 0:
# # 			coin_changes[j][i] = coin_changes[j][i-coins[j]] + coin_changes[j-1][i]
# # 		# elif i - coins[j] == 0:
# # 		# 	coin_changes[j][i] = 1 + coin_changes[j-1][i]
# # 		else:
# # 			coin_changes[j][i] = coin_changes[j-1][i]
# # # pprint.pprint(coin_changes)
# # print coin_changes[j][i]


# # Dynamic Programming Python implementation of Coin Change problem
# def count(S, m, n):
#     # We need n+1 rows as the table is consturcted in bottom up
#     # manner using the base case 0 value case (n = 0)
#     table = [[0 for x in range(m)] for x in range(n+1)]
 
#     # Fill the enteries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
 
#     # Fill rest of the table enteries in bottom up manner
#     for i in range(1, n+1):
#         for j in range(m):
#             # Count of solutions including S[j]
#             x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
#             # Count of solutions excluding S[j]
#             y = table[i][j-1] if j >= 1 else 0
 
#             # total count
#             table[i][j] = x + y
#  	print
#     return table[n][m-1]
# count([2,3,5,6], 4, 10)