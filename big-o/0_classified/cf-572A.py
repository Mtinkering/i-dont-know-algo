a, b = map(int, input().split())

k, m = map(int, input().split())
maxArrayA = int((input().split())[k-1])
minArrayB = int((input().split())[b-m])


if (maxArrayA < minArrayB):
    print('YES')
else:
    print('NO')
