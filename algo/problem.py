
N, Q, k = [int(x) for x in raw_input().split()]

arr = [int(x) for x in raw_input().split()]

def mergeSort(arr):
	n = len(arr)
	if (n == 1):
		return

	middle = n//2

	left = arr[0:middle]
	right = arr[middle:]
	mergeSort(left)
	mergeSort(right)
	l = 0
	r = 0

	for i in range(0,n):
		if (r == len(right) or (l != len(left) and left[l] < right[r])):
			arr[i] = left[l]
			l += 1
		else:
			arr[i] = right[r]
			r += 1

for q in range(0,Q):
	l, r = [int(x) for x in raw_input().split()]

	newArr = arr[l:r+1]
	mergeSort(newArr)
	arr = arr[:l] + newArr + arr[r+1:]

print arr[k]

# N  = input()
# x1, y1 = [int(x) for x in raw_input().split()]

# if (x1 == 0 and y1 == 0):
# 		x

# # b = y1 - x1*k

# if (N == 2):
# 	print 'YES'

# else:
# 	anwser = 'YES'
# 	for i in range(0,N-2):
# 		x, y = [int(x) for x in raw_input().split()]
# 		newK = (y-y1)/(x-x1)
# 		if ( newK != k):
# 			anwser = 'NO'
# 			break

# 	print anwser