n = int(input())
arr = list(map(int, input().split()))


def minWatchingGame(arr, n):
    arr = [0] + arr + [90]
    for i in range(len(arr) - 1):
        if (arr[i] + 15 < arr[i+1]):
            return min(90, arr[i] + 15)


print(minWatchingGame(arr, n))
