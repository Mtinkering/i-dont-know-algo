def insertion_sort(arr, size):
	if size == 1: return arr
	
	for i in range(1,size):
		e = arr[i]
		for j in range(i-1,-1,-1):
			if arr[j] > e:
				arr[j+1] = arr[j] 
				
				arr[j] = e

		print " ".join(map(str,arr))



size = int(raw_input())

arr = map(int, raw_input().strip().split())

insertion_sort(arr,size)