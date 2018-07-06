def selectionSort(arr):
  n = len(arr)

  for i in range(n):
    indexOfMin = i
    for j in range(i+1, n):
      if arr[j] < arr[indexOfMin]:
        indexOfMin = j

    # swap with the beginning
    arr[indexOfMin], arr[i] = arr[i], arr[indexOfMin]
    print(arr)


selectionSort([3, 1, 5, 4])
selectionSort([1])
selectionSort([5, 4, 3, 2, 1])
