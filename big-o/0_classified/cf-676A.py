n = int(input())
arr = list(map(int, input().split()))

minA = arr.index(1)
maxA = arr.index(n)

print(max(maxA, n - 1 - maxA, minA, n - 1 - minA))
