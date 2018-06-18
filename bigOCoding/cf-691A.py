n = int(input())  # 3
arr = [int(i) for i in input().split(' ')]
arr = list(map(int, input().split(' ')))

answer = 'NO'


if (n == 1):
    if (arr[0] == 1):
        answer = 'YES'
else:
    # make sure there is at least len(arr) - 2
    numberOfFastenedButtons = 0
    for button in arr:
        if (button == 1):
            numberOfFastenedButtons += 1  # 3

    if (numberOfFastenedButtons == (n-1)):
        answer = 'YES'


print(answer)
