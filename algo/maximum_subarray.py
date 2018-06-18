∫
# DISCLAIMER: this answer is wrong. it was my first brainstorm, so i would like to keep it

# Use Kadana's algorithm instead
nTests = int(raw_input())

def printResult(array,n):

	def max_subarray(array,n):
		a = sum([x for x in array])
		# b = max(array)
		answer = a

		for i in range(n,1,-1):

			maxValue = 0
			if (a - array[0] < a - array[i-1]):
				maxValue = a - array[i-1]
				array.pop(i-1)
			else:
				maxValue = a - array[0]
				array.pop(0)
			# if maxValue < a:
				# break
			answer = max(maxValue,answer)
			# print answer
			# else:
			a = maxValue
		return answer


	def max_value(array):

		a = [x for x in array if x >= 0]
		if (len(a) == 0): return max(array)
		else: return sum(a)


	maximum = max_value(array)
	print max_subarray(array,n), maximum


for test in range(nTests):
	n = int(raw_input())
	array = [int(x) for x in raw_input().split()]

	printResult(array,n)

