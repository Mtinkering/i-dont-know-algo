n, m = map(int, input().split())

opTable = {}
answer = 'Yes'
for r in range(n):
    row = input()
    black = set()

    for i in range(m):
        if (row[i] == '#'):
            black.add(i)
            if (i not in opTable):
                opTable[i] = black

    for b in black:
        diff = black.symmetric_difference(opTable[b])
        if (len(diff) != 0):
            answer = 'No'
            break

    if (answer == 'No'):
        break
print(answer)