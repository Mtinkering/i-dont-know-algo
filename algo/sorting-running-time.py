def insertion_sort(arr, size):
	if size == 1: print 0
	answer = 0	
	for i in range(1,size):
		e = arr[i]
		for j in range(i-1,-1,-1):
			if arr[j] > e:
				arr[j+1] = arr[j] 
				
				arr[j] = e
				answer += 1
	print answer
		# print " ".join(map(str,arr))



size = int(raw_input())

arr = map(int, raw_input().strip().split())

insertion_sort(arr,size)