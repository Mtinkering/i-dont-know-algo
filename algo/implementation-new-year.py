def checkIfChao(arr, N):
	for i in range(0,N):
		original = arr[i] - 1
		if(original > i + 2):
			# print arr[i]
			return True
	return False

def countIS(arr):
	n = len(arr)
	if (n == 1):
		return 0

	middle = n//2

	left = arr[0:middle]
	right = arr[middle:]
	countLeft = countIS(left)
	countRight =  countIS(right)
	countInter = 0
	l = 0
	r = 0

	for i in range(0,n):
		if (r == len(right) or (l != len(left) and left[l] < right[r])):
			arr[i] = left[l]
			l += 1
		else:
			arr[i] = right[r]
			countInter += len(left) - l
			r += 1
	return countLeft + countRight + countInter

def main(arr, N):

	if checkIfChao(arr, N):
		print 'Too chaotic'
	else:
		print countIS(arr)

for _ in range(0,input()):
	N = input()
	lists = [int(x) for x in raw_input().split()]
	main(lists, N)










