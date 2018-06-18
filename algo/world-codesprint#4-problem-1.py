



# n1,n2,n3 = [int(x) for x in raw_input().split()]

# arr1 = [int(x) for x in raw_input().split()]
# arr2 = [int(x) for x in raw_input().split()]
# arr3 = [int(x) for x in raw_input().split()]

# sum1 = sum(arr1)
# sum2 = sum(arr2)
# sum3 = sum(arr3)
# listSum = [sum1,sum2,sum3]
# maxValue = max(listSum)
# minValue = min(listSum)

# while (maxValue != minValue):
# 	if (maxValue == 0):
# 		break
# 	maxIndex = listSum.index(maxValue)
# 	val = 0
# 	if (maxIndex == 0):
# 		val = arr1.pop(0)
		
# 	elif (maxIndex == 1):
# 		val = arr2.pop(0)
# 	else:

# 		val = arr3.pop(0)

# 	listSum[maxIndex] -= val
# 	maxValue = max(listSum)
# 	minValue = min(listSum)

# print listSum[0]

# N = input()
# table = {}
# i = 0
# answer = 10000
# for x in raw_input().split():
# 	if x not in table:
# 		table[x] = [i]
# 	else:
# 		table[x].append(i)
# 	i += 1
# for key in table:
# 	value = table[key]
# 	n = len(value)

# 	if (n > 1):
# 		for j in range(0,n-1):
# 			d = value[j+1] - value[j]
# 			answer = min(d,answer)





# if (answer == 10000):
# 	print -1
# else:
# 	print answer
