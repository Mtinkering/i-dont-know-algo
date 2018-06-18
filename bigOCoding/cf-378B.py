n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))

k = n//2

firstSemifinal = [0]*n
secondSemifinal = [0]*n

# Take k
for i in range(k):
    firstSemifinal[i] = 1
    secondSemifinal[i] = 1


# Take 0
a = 0
b = 0
for i in range(n):
    if arr[a][0] < arr[b][1]:
        firstSemifinal[a] = 1
        a += 1
    else:
        secondSemifinal[b] = 1
        b += 1


print(''.join(map(str, firstSemifinal)))
print(''.join(map(str, secondSemifinal)))
