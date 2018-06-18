
def insertionSort(ar,size):
	e = ar[-1]

	if size == 1:
		print " ".join(map(str,arr))
		return

	for i in range(size-1,0,-1):
		if arr[i-1] > e:
			
			arr[i] = arr[i-1]
			print " ".join(map(str,arr))
			if i == 1:
				arr[i-1] = e
				print " ".join(map(str,arr))
		else:
			arr[i] = e
			print " ".join(map(str,arr))
			return




size = int(raw_input())

arr = map(int, raw_input().strip().split())

insertionSort(arr,size)

