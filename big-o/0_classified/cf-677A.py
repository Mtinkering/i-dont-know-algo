n, h = map(int, input().split())
arr = list(map(int, input().split()))

minWidth = 0

for a in arr:
    if (a > h):
        minWidth += 2
    else:
        minWidth += 1


print(minWidth)
